#!/usr/bin/env python3
"""
validate-index.py — Developer Knowledge Hub Link & Index Validator

This script performs three validation checks:
  1. Every directory (except excluded ones) contains a README.md.
  2. All relative markdown links in .md files resolve to existing files.
  3. The root README.md Quick-Reference Index references all top-level
     category directories.

Usage:
    python scripts/validate-index.py [--fix]

    --fix    Append missing categories to the root README.md index
             (prints a suggestion; does not auto-modify by default).

Exit codes:
    0  All checks passed.
    1  One or more checks failed.
"""

import os
import re
import sys
from pathlib import Path

# Fix Unicode output on Windows terminals (cp1252 → utf-8)
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

# ─── Configuration ──────────────────────────────────────────────────────────

REPO_ROOT = Path(__file__).resolve().parent.parent

EXCLUDED_DIRS = {
    ".git", ".github", "__pycache__", "node_modules",
    "_templates", "scripts", ".vscode", ".idea",
}

LINK_PATTERN = re.compile(
    r'\[([^\]]*)\]\(([^)]+)\)'  # Matches [text](path)
)

# ─── Helpers ────────────────────────────────────────────────────────────────

class Colors:
    """ANSI color codes for terminal output."""
    GREEN = "\033[92m"
    RED = "\033[91m"
    YELLOW = "\033[93m"
    CYAN = "\033[96m"
    RESET = "\033[0m"
    BOLD = "\033[1m"


def is_excluded(path: Path) -> bool:
    """Check if a directory should be skipped."""
    return any(part in EXCLUDED_DIRS for part in path.parts)


def collect_directories(root: Path) -> list[Path]:
    """Return all non-excluded directories under root (including root)."""
    dirs = []
    for dirpath, dirnames, _ in os.walk(root):
        # Prune excluded directories from walk
        dirnames[:] = [
            d for d in dirnames
            if d not in EXCLUDED_DIRS and not d.startswith(".")
        ]
        dp = Path(dirpath)
        if dp != root and not is_excluded(dp.relative_to(root)):
            dirs.append(dp)
    return dirs


def collect_markdown_files(root: Path) -> list[Path]:
    """Return all .md files in the repo (excluding excluded dirs)."""
    md_files = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [
            d for d in dirnames
            if d not in EXCLUDED_DIRS and not d.startswith(".")
        ]
        for f in filenames:
            if f.endswith(".md"):
                md_files.append(Path(dirpath) / f)
    return md_files


# ─── Check 1: Every directory has a README.md ──────────────────────────────

def check_readme_presence(directories: list[Path]) -> list[str]:
    """Verify every content directory contains a README.md."""
    errors = []
    for d in directories:
        readme = d / "README.md"
        if not readme.exists():
            rel = d.relative_to(REPO_ROOT)
            errors.append(f"Missing README.md in: {rel}/")
    return errors


# ─── Check 2: All relative links resolve ───────────────────────────────────

def check_relative_links(md_files: list[Path]) -> list[str]:
    """Validate that all relative markdown links point to existing files."""
    errors = []
    for md_file in md_files:
        content = md_file.read_text(encoding="utf-8", errors="replace")
        for line_num, line in enumerate(content.splitlines(), start=1):
            for match in LINK_PATTERN.finditer(line):
                link_text, link_target = match.group(1), match.group(2)

                # Skip external links, anchors, badges, and images
                if link_target.startswith(("http://", "https://", "#", "mailto:")):
                    continue
                if link_target.startswith("../../"):
                    continue  # GitHub relative issue/PR links

                # Strip anchor fragments
                clean_target = link_target.split("#")[0]
                if not clean_target:
                    continue

                # Resolve relative to the file's directory
                resolved = (md_file.parent / clean_target).resolve()
                if not resolved.exists():
                    rel_file = md_file.relative_to(REPO_ROOT)
                    errors.append(
                        f"{rel_file}:{line_num} — broken link "
                        f"[{link_text}]({link_target})"
                    )
    return errors


# ─── Check 3: Root index references all top-level categories ───────────────

def check_root_index_coverage(root: Path) -> list[str]:
    """Ensure root README.md references all top-level category directories."""
    errors = []
    root_readme = root / "README.md"
    if not root_readme.exists():
        return ["Root README.md is missing!"]

    content = root_readme.read_text(encoding="utf-8", errors="replace")

    # Find all top-level content directories
    top_level_dirs = sorted([
        d.name for d in root.iterdir()
        if d.is_dir()
        and d.name not in EXCLUDED_DIRS
        and not d.name.startswith(".")
        and not d.name.startswith("_")
        and (d / "README.md").exists()
    ])

    for dirname in top_level_dirs:
        # Check if the directory is referenced in root README
        pattern = rf'{dirname}/|{dirname}\\'
        if not re.search(pattern, content):
            errors.append(
                f"Root README.md does not reference category: {dirname}/"
            )

    return errors


# ─── Main ───────────────────────────────────────────────────────────────────

def main() -> int:
    print(f"\n{Colors.BOLD}{Colors.CYAN}{'='*60}")
    print("  Developer Knowledge Hub — Index Validator")
    print(f"{'='*60}{Colors.RESET}\n")

    all_errors: list[str] = []

    # Check 1
    print(f"{Colors.BOLD}[1/3] Checking README.md presence in all directories...{Colors.RESET}")
    directories = collect_directories(REPO_ROOT)
    readme_errors = check_readme_presence(directories)
    if readme_errors:
        for e in readme_errors:
            print(f"  {Colors.RED}✗ {e}{Colors.RESET}")
        all_errors.extend(readme_errors)
    else:
        print(f"  {Colors.GREEN}✓ All directories have README.md{Colors.RESET}")

    # Check 2
    print(f"\n{Colors.BOLD}[2/3] Validating relative links in markdown files...{Colors.RESET}")
    md_files = collect_markdown_files(REPO_ROOT)
    link_errors = check_relative_links(md_files)
    if link_errors:
        for e in link_errors:
            print(f"  {Colors.RED}✗ {e}{Colors.RESET}")
        all_errors.extend(link_errors)
    else:
        print(f"  {Colors.GREEN}✓ All relative links are valid ({len(md_files)} files scanned){Colors.RESET}")

    # Check 3
    print(f"\n{Colors.BOLD}[3/3] Checking root index coverage...{Colors.RESET}")
    index_errors = check_root_index_coverage(REPO_ROOT)
    if index_errors:
        for e in index_errors:
            print(f"  {Colors.YELLOW}⚠ {e}{Colors.RESET}")
        all_errors.extend(index_errors)
    else:
        print(f"  {Colors.GREEN}✓ Root index references all categories{Colors.RESET}")

    # Summary
    print(f"\n{Colors.BOLD}{'='*60}{Colors.RESET}")
    if all_errors:
        print(f"{Colors.RED}{Colors.BOLD}  ✗ {len(all_errors)} issue(s) found.{Colors.RESET}")
        print(f"{Colors.BOLD}{'='*60}{Colors.RESET}\n")
        return 1
    else:
        print(f"{Colors.GREEN}{Colors.BOLD}  ✓ All checks passed!{Colors.RESET}")
        print(f"{Colors.BOLD}{'='*60}{Colors.RESET}\n")
        return 0


if __name__ == "__main__":
    sys.exit(main())
