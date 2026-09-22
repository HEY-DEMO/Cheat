<![CDATA[# Contributing to Developer Knowledge Hub

Thank you for your interest in contributing! This guide will help you get started.

---

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How to Contribute](#how-to-contribute)
- [Content Standards](#content-standards)
- [Directory & File Naming](#directory--file-naming)
- [Pull Request Process](#pull-request-process)

---

## Code of Conduct

Be respectful, constructive, and inclusive. We follow the [Contributor Covenant](https://www.contributor-covenant.org/).

---

## How to Contribute

### Adding a New Topic to an Existing Category

1. Fork the repository and create a feature branch.
2. Copy `_templates/cheatsheet-template.md` into the target category directory.
3. Rename it using `kebab-case` (e.g., `strategy-pattern.md`).
4. Fill in all template sections.
5. Update the category's `README.md` to include your new topic in its table of contents.
6. Run `python scripts/validate-index.py` to ensure links are valid.
7. Submit a Pull Request.

### Adding a New Category

1. Create a new `kebab-case` directory at the appropriate nesting level.
2. Add a `README.md` inside it following the category README pattern (see `_templates/`).
3. Add at least one topic `.md` file.
4. Update the root `README.md` Quick-Reference Index table.
5. Run validation and submit a PR.

---

## Content Standards

- **Use the template**: All cheat sheets must follow `_templates/cheatsheet-template.md`.
- **Relative links only**: Never use absolute URLs for internal cross-references.
- **Code examples**: Must be runnable or clearly marked as pseudocode.
- **Language tags**: Always specify the language in fenced code blocks (` ```python `, ` ```javascript `, etc.).
- **Diagrams**: Use Mermaid syntax for inline diagrams where possible.

---

## Directory & File Naming

| Element      | Convention                                  | Example                    |
|-------------|---------------------------------------------|----------------------------|
| Directories | `kebab-case`, lowercase                     | `design-patterns/`         |
| Topic files | `kebab-case.md`                             | `singleton-pattern.md`     |
| README       | Always `README.md` (uppercase)              | `README.md`                |
| Max depth   | 3 levels recommended                        | `tools/free/vscode.md`     |

---

## Pull Request Process

1. Ensure your content follows all standards above.
2. Run `python scripts/validate-index.py` — all checks must pass.
3. Provide a clear PR title: `add: <category>/<topic-name>` or `fix: <description>`.
4. Fill in the PR template description.
5. A maintainer will review within 48 hours.

---

Thank you for helping build this knowledge hub! 🚀
]]>
