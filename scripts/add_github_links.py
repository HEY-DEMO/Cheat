#!/usr/bin/env python3
"""
scripts/add_github_links.py

Adds the upstream GitHub repository link at the top of all <github_repo_name>.md
files located in github_repos/*/.
"""

import re
import sys
from pathlib import Path

# UTF-8 stdout configuration for Windows
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

REPO_ROOT = Path(__file__).resolve().parent.parent
HUB_README = REPO_ROOT / "github_repos" / "README.md"


def main():
    hub_content = HUB_README.read_text(encoding="utf-8")
    table_pattern = re.compile(
        r"\|\s*\d+\s*\|\s*\*\*([^*]+)\*\*\s*\|\s*\[([^\]]+)\]\(([^)]+)\)\s*\|\s*([^|]+)\|\s*\[([^\]]+)\]\(([^)]+)\)\s*\|"
    )
    matches = table_pattern.findall(hub_content)
    print(f"Found {len(matches)} repository mappings in {HUB_README.name}")

    updated_count = 0
    skipped_count = 0

    for name, gh_label, gh_url, desc, ref_label, ref_file in matches:
        target_path = REPO_ROOT / "github_repos" / ref_file
        if not target_path.exists():
            print(f"  ✗ Warning: Target file missing: {target_path}")
            continue

        content = target_path.read_text(encoding="utf-8")
        if content.startswith("> 🔗 **GitHub Repository**:"):
            print(f"  - Already present in: {ref_file}")
            skipped_count += 1
            continue

        header = f"> 🔗 **GitHub Repository**: [{gh_label.strip()}]({gh_url.strip()})\n\n---\n\n"
        new_content = header + content.lstrip("\r\n")
        target_path.write_text(new_content, encoding="utf-8")
        print(f"  ✓ Added GitHub link to: {ref_file} -> {gh_url.strip()}")
        updated_count += 1

    print(f"\nDone! Updated: {updated_count}, Skipped: {skipped_count}, Total: {len(matches)}")


if __name__ == "__main__":
    main()
