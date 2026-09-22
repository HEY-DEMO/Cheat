---
name: add_github_repo
description: "Ingests a GitHub repository's README documentation into github_repos/<repo_name>.md and systematically updates folder-level and root-level indexes."
version: "1.0.0"
author: "Antigravity Engineering"
triggers:
  - command: "/add-repo"
  - command: "/add_github_repo"
  - natural_language:
      - "add github repo <url|name>"
      - "index github repository"
      - "add repo to github_repos"
inputs:
  repo_name:
    type: string
    description: "The name or slug of the repository (e.g., 'trailhq/Graft', 'Graft', or 'graft')."
    required: true
  repo_summary:
    type: string
    description: "A concise 1-2 sentence description of what the project does, formatted for index tables."
    required: true
  readme_content:
    type: string
    description: "The complete raw Markdown content of the repository's README or documentation."
    required: true
  repo_url:
    type: string
    description: "Upstream GitHub URL (e.g., 'https://github.com/owner/repo'). Inferred if owner/slug provided in repo_name."
    required: false
  overwrite:
    type: boolean
    description: "Explicit flag allowing overwrite if github_repos/<repo_name>.md already exists."
    default: false
---

# Skill: `add_github_repo`

A production-grade agent instruction workflow to persist third-party GitHub repository documentation into the local knowledge hub and maintain referential integrity across all project indexes.

---

## 1. Architectural Overview & Context

This repository maintains an organized developer knowledge hub. Third-party repository documentation lives under `github_repos/`:
- **Repository Documentation**: `github_repos/<sanitized_repo_name>.md`
- **Folder Index**: `github_repos/README.md`
- **Root Master Index**: `README.md`
- **Automated Validation**: `scripts/validate-index.py` (enforced via GitHub Actions CI)

When adding a GitHub repository, an autonomous agent must adhere to strict sanitization, idempotency, and link validation standards to prevent corrupting tables or failing CI builds.

---

## 2. Input Specification & Sanitization Rules

Before executing any file system operation, parse and validate the input arguments.

### 2.1 Argument Normalization
| Argument | Validation & Transformation Rules |
| :--- | :--- |
| `repo_name` | 1. If an upstream URL or full identifier is provided (e.g., `trailhq/Graft` or `https://github.com/trailhq/Graft`), extract the base repo name (`Graft`).<br/>2. Derive the file stem: lowercase, trim whitespace, replace spaces and underscores with hyphens (`-`).<br/>3. Strip dangerous filesystem characters (`<>:"/\|?*`).<br/>4. Ensure trailing `.md` is omitted for the stem: `sanitized_stem = "graft"`. File path becomes `github_repos/{sanitized_stem}.md`. |
| `repo_url` | 1. If omitted, check if `repo_name` contains `github.com` or `owner/name`. If so, format as `https://github.com/{owner}/{name}`.<br/>2. If unavailable, default to upstream repository link or search URL. |
| `repo_summary` | 1. Must be 1–2 plain-text sentences (max ~150 chars).<br/>2. Strip raw line breaks (`\n` or `\r`) to ensure it does not break Markdown table row layout. |
| `readme_content` | Raw string. Must not be truncated. Must preserve fenced blocks (` ``` `), badges, SVG tags, and HTML attributes. |
| `overwrite` | Boolean flag. Defaults to `false`. |

---

## 3. Step-by-Step Execution Protocol

```mermaid
flowchart TD
    A[Receive Trigger & Inputs] --> B[Sanitize repo_name & validate inputs]
    B --> C{File Exists?}
    C -- Yes and overwrite=false --> D[Abort with Warning]
    C -- No or overwrite=true --> E[Normalize Markdown & Resolve Broken Relative Links]
    E --> F[Write github_repos/{sanitized_name}.md]
    F --> G[Update Table in github_repos/README.md]
    G --> H[Update Quick-Reference & Tree in root README.md]
    H --> I[Run scripts/validate-index.py]
    I --> J{Validation Passed?}
    J -- Yes --> K[Return Success Report]
    J -- No --> L[Self-Correct Broken Links & Re-validate]
```

### Step 1: Safeguard Check (Pre-flight)
1. Verify target directory `github_repos/` exists. If not, create it.
2. Resolve target path: `github_repos/<sanitized_stem>.md`.
3. Check file existence:
   - If `github_repos/<sanitized_stem>.md` exists AND `overwrite == false`:
     - **Halt execution.**
     - Return warning to user:
       ```text
       File 'github_repos/<sanitized_stem>.md' already exists.
       Set 'overwrite: true' or specify an alternative repo_name to proceed.
       ```

### Step 2: Content Normalization & Resolution
Third-party README files frequently contain relative links (e.g., `[LICENSE](LICENSE)`, `[CONTRIBUTING](CONTRIBUTING.md)`) that break repository validation tools (`validate-index.py`).
1. **Convert Relative File Links**:
   - Inspect markdown links `[Title](relative_path)`.
   - If `relative_path` does not begin with `http://`, `https://`, `#`, or `mailto:`, rewrite it to point to the upstream GitHub repository:
     ```text
     [LICENSE](LICENSE) -> [LICENSE]({repo_url}/blob/main/LICENSE)
     [CREDITS.md](CREDITS.md) -> [CREDITS.md]({repo_url}/blob/main/CREDITS.md)
     ```
2. **Preserve Images and Badges**:
   - Do NOT modify raw image tags (`<img src="...">`) or badge URLs unless requested.
3. **Append Navigation Footer**:
   Ensure the following navigation block is appended to the bottom of the content:
   ```markdown
   ---

   *← Back to [GitHub Repos](./README.md) · [Root Index](../README.md)*
   ```
4. **Write File**:
   Persist the normalized content into `github_repos/<sanitized_stem>.md` using UTF-8 encoding.

### Step 3: Folder-Level Index Update (`github_repos/README.md`)
1. Read `github_repos/README.md`.
2. Inspect the Table of Contents table:
   ```markdown
   | #  | Repository | GitHub Link | Description | Local Reference |
   |----|-----------|-------------|-------------|-----------------|
   ```
3. Check for duplicates:
   - If `sanitized_stem.md` is already in the table and `overwrite == true`, update the existing row.
   - If not present, calculate the next sequential index number `$N = count + 1`.
   - Append the new entry:
     ```markdown
     | $N | **<Display Name>** | [<owner/repo>](<repo_url>) | <repo_summary> | [<sanitized_stem>.md](<sanitized_stem>.md) |
     ```
4. Preserve markdown formatting, header text, and back-links.

### Step 4: Root Master Index Update (`README.md`)
1. Read root `README.md`.
2. **Quick-Reference Table**:
   Verify that `github_repos/` is listed in the `## 🗂️ Quick-Reference Index` table.
   If missing, add:
   ```markdown
   | 16 | 📁 GitHub Repos            | Curated open-source repositories and agent tooling  | [github_repos/](github_repos/README.md)                     |
   ```
3. **Directory Tree**:
   Ensure the directory tree under `## 📁 Full Directory Tree` includes `github_repos/` and the newly added file:
   ```text
   ├── github_repos/
   │   ├── README.md
   │   └── <sanitized_stem>.md
   ```

### Step 5: Automated Verification
Execute the local integrity checker:
```bash
python scripts/validate-index.py
```
- **Exit code 0**: All directories contain READMEs, all relative links resolve, and root index coverage is 100%.
- **Exit code 1**: Parse validation errors. If relative links in `<sanitized_stem>.md` failed, fix the URLs and re-test.

---

## 4. Edge Cases & Safeguards

| Scenario | Risk | Mitigation Strategy |
| :--- | :--- | :--- |
| **Path Traversal Attack** | Inputs like `../../etc/passwd` or `../tools` could overwrite critical files. | Strip all leading `.` and `/` or `\` characters. Constrain writing strictly to `REPO_ROOT / "github_repos" / f"{sanitized_stem}.md"`. |
| **Special Characters** | Characters like `?`, `*`, `:`, `|` cause OS write failures on Windows. | Apply strict regex replace: `re.sub(r'[^a-zA-Z0-9_\-\.]', '-', raw_name)`. |
| **Unescaped Pipes in Tables** | Pipes `\|` in `repo_summary` split Markdown table columns. | Escape pipe symbols: replace `\|` with `\|` in `repo_summary`. |
| **Multi-line Summaries** | Newlines break GitHub Markdown table rows into separate paragraphs. | Replace `\r\n` and `\n` with a single space. |
| **Large README Files** | Documents > 100KB can trigger token or memory issues. | Use streaming or chunked read/writes when interacting via filesystem tools. |

---

## 5. Reference Implementation / Tool Invocations

### Example Scenario: Ingesting `trailhq/Graft`
```json
{
  "repo_name": "trailhq/Graft",
  "repo_url": "https://github.com/trailhq/Graft",
  "repo_summary": "Open-source context layer for large codebases — turbocharges coding agents.",
  "readme_content": "<div align=\"center\">\n\n# Graft\n... full markdown body ...",
  "overwrite": false
}
```

### Generated Files & Diffs:
1. **Target Document**: `github_repos/graft.md`
2. **Folder Index Entry**:
   ```markdown
   | 1 | **Graft** | [trailhq/Graft](https://github.com/trailhq/Graft) | Open-source context layer for large codebases — turbocharges coding agents | [graft.md](graft.md) |
   ```
3. **Root Index Entry**:
   ```markdown
   | 16 | 📁 GitHub Repos | Curated open-source repositories and agent tooling | [github_repos/](github_repos/README.md) |
   ```

---

## 6. Definition of Done
A repository ingestion task is complete only when:
1. `github_repos/<sanitized_stem>.md` is saved with intact markup and valid links.
2. `github_repos/README.md` includes the repository in its table of contents.
3. Root `README.md` references the `github_repos/` section.
4. `python scripts/validate-index.py` exits with code 0 (`All checks passed!`).
