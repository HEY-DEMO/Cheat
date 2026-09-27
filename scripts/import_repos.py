#!/usr/bin/env python3
"""
scripts/import_repos.py

Fetches and formats new GitHub repository cheat sheets / guides into their
designated category folders, rewriting relative upstream links to avoid broken
link errors in local repository index validation.
"""

import os
import re
import sys
import urllib.request
from pathlib import Path

# UTF-8 stdout configuration for Windows
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

REPO_ROOT = Path(__file__).resolve().parent.parent

REPOS_CONFIG = [
    {
        "name": "build-your-own-x",
        "owner_repo": "codecrafters-io/build-your-own-x",
        "branch": "master",
        "url": "https://raw.githubusercontent.com/codecrafters-io/build-your-own-x/master/README.md",
        "dest": REPO_ROOT / "github_repos" / "learning-resources" / "build-your-own-x.md",
        "category_name": "Learning & Computer Science",
        "category_path": "./README.md",
    },
    {
        "name": "developer-roadmap",
        "owner_repo": "nilbuild/developer-roadmap",
        "branch": "master",
        "url": "https://raw.githubusercontent.com/nilbuild/developer-roadmap/master/readme.md",
        "dest": REPO_ROOT / "github_repos" / "learning-resources" / "developer-roadmap.md",
        "category_name": "Learning & Computer Science",
        "category_path": "./README.md",
    },
    {
        "name": "freecodecamp",
        "owner_repo": "freeCodeCamp/freeCodeCamp",
        "branch": "main",
        "url": "https://raw.githubusercontent.com/freeCodeCamp/freeCodeCamp/main/README.md",
        "dest": REPO_ROOT / "github_repos" / "learning-resources" / "freecodecamp.md",
        "category_name": "Learning & Computer Science",
        "category_path": "./README.md",
    },
    {
        "name": "awesome",
        "owner_repo": "sindresorhus/awesome",
        "branch": "main",
        "url": "https://raw.githubusercontent.com/sindresorhus/awesome/main/readme.md",
        "dest": REPO_ROOT / "github_repos" / "curated-lists" / "awesome.md",
        "category_name": "Curated Lists & Resources",
        "category_path": "./README.md",
    },
    {
        "name": "awesome-python",
        "owner_repo": "vinta/awesome-python",
        "branch": "master",
        "url": "https://raw.githubusercontent.com/vinta/awesome-python/master/README.md",
        "dest": REPO_ROOT / "github_repos" / "curated-lists" / "awesome-python.md",
        "category_name": "Curated Lists & Resources",
        "category_path": "./README.md",
    },
    {
        "name": "free-programming-books",
        "owner_repo": "EbookFoundation/free-programming-books",
        "branch": "main",
        "url": "https://raw.githubusercontent.com/EbookFoundation/free-programming-books/main/README.md",
        "dest": REPO_ROOT / "github_repos" / "curated-lists" / "free-programming-books.md",
        "category_name": "Curated Lists & Resources",
        "category_path": "./README.md",
    },
    {
        "name": "public-apis",
        "owner_repo": "public-apis/public-apis",
        "branch": "master",
        "url": "https://raw.githubusercontent.com/public-apis/public-apis/master/README.md",
        "dest": REPO_ROOT / "github_repos" / "curated-lists" / "public-apis.md",
        "category_name": "Curated Lists & Resources",
        "category_path": "./README.md",
    },
]


def transform_content(text: str, owner_repo: str, branch: str, category_name: str, category_path: str) -> str:
    # 1. Transform HTML <img ... src="..."> if relative
    def fix_html_img(m):
        full = m.group(0)
        src = m.group(1)
        if src.startswith(("http://", "https://", "data:", "//")):
            return full
        clean_src = src.lstrip("/")
        return full.replace(src, f"https://raw.githubusercontent.com/{owner_repo}/{branch}/{clean_src}")

    text = re.sub(r'<img\s+[^>]*?src=["\']([^"\']+)["\']', fix_html_img, text)

    # 2. Transform HTML <a ... href="..."> if relative
    def fix_html_a(m):
        full = m.group(0)
        href = m.group(1)
        if href.startswith(("http://", "https://", "#", "mailto:", "//")):
            return full
        clean_href = href.lstrip("/")
        return full.replace(href, f"https://github.com/{owner_repo}/blob/{branch}/{clean_href}")

    text = re.sub(r'<a\s+[^>]*?href=["\']([^"\']+)["\']', fix_html_a, text)

    # 3. Transform Markdown ![alt](url)
    def fix_md_img(m):
        alt = m.group(1)
        url = m.group(2)
        if url.startswith(("http://", "https://", "#", "data:")):
            return m.group(0)
        clean_url = url.lstrip("/")
        return f"![{alt}](https://raw.githubusercontent.com/{owner_repo}/{branch}/{clean_url})"

    text = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", fix_md_img, text)

    # 4. Transform Markdown [text](url)
    def fix_md_link(m):
        full = m.group(0)
        label = m.group(1)
        url = m.group(2)
        if url.startswith(("http://", "https://", "#", "mailto:")):
            return full
        parts = url.split("#", 1)
        rel_path = parts[0].lstrip("/")
        anchor = ("#" + parts[1]) if len(parts) > 1 else ""
        if not rel_path:
            return full
        return f"[{label}](https://github.com/{owner_repo}/blob/{branch}/{rel_path}{anchor})"

    text = re.sub(r"(?<!\!)\[([^\]]*)\]\(([^)]+)\)", fix_md_link, text)

    # 5. Append standard navigation footer
    footer = (
        f"\n\n---\n\n"
        f"*← Back to [{category_name}]({category_path}) · "
        f"[GitHub Repos Hub](../README.md) · "
        f"[Root Index](../../README.md)*\n"
    )
    return text.strip() + footer


def main():
    print("Creating category directories...")
    (REPO_ROOT / "github_repos" / "curated-lists").mkdir(parents=True, exist_ok=True)
    (REPO_ROOT / "github_repos" / "learning-resources").mkdir(parents=True, exist_ok=True)

    for config in REPOS_CONFIG:
        print(f"Fetching {config['name']} ({config['owner_repo']})...")
        req = urllib.request.Request(config["url"], headers={"User-Agent": "Mozilla/5.0"})
        raw_bytes = urllib.request.urlopen(req, timeout=30).read()
        raw_text = raw_bytes.decode("utf-8", errors="replace")
        processed = transform_content(
            raw_text,
            config["owner_repo"],
            config["branch"],
            config["category_name"],
            config["category_path"],
        )
        config["dest"].write_text(processed, encoding="utf-8")
        print(f"  ✓ Wrote {config['dest'].relative_to(REPO_ROOT)} ({len(processed)} chars)")

    print("\nAll 7 repositories successfully imported and formatted!")


if __name__ == "__main__":
    main()
