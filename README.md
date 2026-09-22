<!-- markdownlint-disable MD033 MD041 -->
<div align="center">

# 🧠 Developer Knowledge Hub & Cheat Sheet

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Link Validation](https://img.shields.io/badge/links-validated-success.svg)](#automation--maintenance)
[![Topics](https://img.shields.io/badge/topics-50%2B-orange.svg)](#quick-reference-index)

**A highly structured, open-source collection of developer cheat sheets, design patterns, architecture guides, best practices, and tool references.**

[Getting Started](#quick-reference-index) · [Contributing](CONTRIBUTING.md) · [Templates](_templates/) · [Report Issue](../../issues)

</div>

---

## 📖 How to Use This Repository

1. **Browse the Index** — Use the [Quick-Reference Index](#quick-reference-index) below to jump to any topic.
2. **Navigate by Category** — Each top-level directory has its own `README.md` with a category-specific table of contents.
3. **Use the Template** — When contributing, follow the [Cheat Sheet Template](_templates/cheatsheet-template.md) for consistency.
4. **Search** — Use GitHub's built-in search (`Ctrl+K` / `Cmd+K`) or `grep` locally.

---

## 🗂️ Quick-Reference Index

> **Legend**: 📁 = Category Directory · 📄 = Topic File · 🏷️ = Sub-category

| #  | Category                  | Description                                         | Path                                                       |
|----|---------------------------|-----------------------------------------------------|-------------------------------------------------------------|
| 1  | 📁 Design Patterns        | 14 GoF patterns: Creational, Structural, Behavioral | [design-patterns/](design-patterns/README.md)               |
| 2  | 📁 Architecture            | System design, microservices, event-driven, etc.    | [architecture/](architecture/README.md)                     |
| 3  | 📁 Tools                   | Developer tools — free and paid                     | [tools/](tools/README.md)                                   |
| 4  | 🏷️ └─ Free Tools          | Open-source and free-tier tools                      | [tools/free/](tools/free/README.md)                         |
| 5  | 🏷️ └─ Paid Tools          | Commercial and premium tools                         | [tools/paid/](tools/paid/README.md)                         |
| 6  | 📁 Best Practices          | Code quality, reviews, testing strategies           | [best-practices/](best-practices/README.md)                 |
| 7  | 📁 Coding Standards        | Style guides, linting, naming conventions           | [coding-standards/](coding-standards/README.md)             |
| 8  | 📁 Use Cases               | Real-world implementation walkthroughs              | [use-cases/](use-cases/README.md)                           |
| 9  | 📁 Data Structures         | Arrays, trees, graphs, hash maps, and more          | [data-structures/](data-structures/README.md)               |
| 10 | 📁 Algorithms              | Sorting, searching, dynamic programming, etc.       | [algorithms/](algorithms/README.md)                         |
| 11 | 📁 DevOps & CI/CD          | Pipelines, containers, infrastructure as code       | [devops/](devops/README.md)                                 |
| 12 | 📁 Security                | AppSec, OWASP, authentication, encryption           | [security/](security/README.md)                             |
| 13 | 📁 Databases               | SQL, NoSQL, query optimization, migrations          | [databases/](databases/README.md)                           |
| 14 | 📁 API Design              | REST, GraphQL, gRPC, versioning, documentation      | [api-design/](api-design/README.md)                         |
| 15 | 📁 Testing                 | Unit, integration, E2E, TDD, property-based         | [testing/](testing/README.md)                               |
| 16 | 📁 GitHub Repos            | Curated open-source repositories and agent tooling  | [github_repos/](github_repos/README.md)                     |

---

## 📐 Taxonomy Conventions

All content in this repository follows these structural rules:

| Rule                          | Details                                                              |
|-------------------------------|----------------------------------------------------------------------|
| **Directory Naming**          | `kebab-case`, lowercase only (e.g., `design-patterns/`)             |
| **File Naming**               | `kebab-case.md` for topics (e.g., `singleton-pattern.md`)           |
| **Every Directory Has**       | A `README.md` that acts as TOC for that directory                    |
| **Cheat Sheet Schema**        | Follow [`_templates/cheatsheet-template.md`](_templates/cheatsheet-template.md) |
| **Max Nesting Depth**         | 3 levels recommended (e.g., `tools/free/vscode.md`)                 |
| **Cross-references**          | Use relative paths only (e.g., `../design-patterns/singleton.md`)   |

---

## 🤝 Contributing

We welcome contributions! Please read [CONTRIBUTING.md](CONTRIBUTING.md) before submitting a PR.

### Quick Steps

1. **Fork** this repository.
2. **Create a branch**: `git checkout -b add/topic-name`.
3. **Add your content** using the [cheat sheet template](_templates/cheatsheet-template.md).
4. **Ensure every new directory** has a `README.md`.
5. **Run the link validator** before pushing:
   ```bash
   python scripts/validate-index.py
   ```
6. **Submit a Pull Request** with a clear description.

---

## 🔧 Automation & Maintenance

| Tool                        | Purpose                                              | Location                                      |
|-----------------------------|------------------------------------------------------|-----------------------------------------------|
| `validate-index.py`        | Validates relative links & checks directory READMEs  | [`scripts/validate-index.py`](scripts/validate-index.py) |
| GitHub Actions CI           | Runs validation on every PR                          | [`.github/workflows/validate.yml`](.github/workflows/validate.yml) |

Run validation locally:

```bash
python scripts/validate-index.py
```

---

## 📁 Full Directory Tree

```
.
├── README.md                          # ← You are here (Master Index)
├── CONTRIBUTING.md                    # Contribution guidelines
├── LICENSE                            # MIT License
├── _templates/
│   └── cheatsheet-template.md         # Reusable cheat sheet schema
├── scripts/
│   └── validate-index.py             # Link & index validator
├── .github/
│   └── workflows/
│       └── validate.yml               # CI pipeline for validation
├── design-patterns/
│   ├── README.md
│   ├── singleton.md               # Creational
│   ├── factory-method.md
│   ├── abstract-factory.md
│   ├── builder.md
│   ├── prototype.md
│   ├── adapter.md                 # Structural
│   ├── bridge.md
│   ├── decorator.md
│   ├── facade.md
│   ├── flyweight.md
│   ├── proxy.md
│   ├── observer.md                # Behavioral
│   ├── strategy.md
│   └── state.md
├── architecture/
│   ├── README.md
│   ├── microservices.md
│   └── event-driven.md
├── tools/
│   ├── README.md
│   ├── free/
│   │   ├── README.md
│   │   ├── ackee.md
│   │   ├── agent-skills.md
│   │   ├── bun.md
│   │   ├── cap.md
│   │   ├── crewai.md
│   │   ├── excalidraw.md
│   │   ├── fish-audio.md
│   │   ├── graphify.md
│   │   ├── gsd-core.md
│   │   ├── handy.md
│   │   ├── harper.md
│   │   ├── kanbn.md
│   │   ├── kokoro-tts.md
│   │   ├── meetily.md
│   │   ├── mattpocock-skills.md
│   │   ├── microthinker.md
│   │   ├── omniroute.md
│   │   ├── open-notebook.md
│   │   ├── penpot.md
│   │   ├── ponytail.md
│   │   ├── ralph.md
│   │   ├── superpowers.md
│   │   ├── the-book-of-secret-knowledge.md
│   │   ├── upscayl.md
│   │   └── vscode.md
│   └── paid/
│       ├── README.md
│       ├── jetbrains.md
│       ├── krea.md
│       └── vercel.md
├── best-practices/
│   ├── README.md
│   ├── code-reviews.md
│   └── seo-checklist.md
├── coding-standards/
│   ├── README.md
│   └── naming-conventions.md
├── use-cases/
│   ├── README.md
│   └── e-commerce-checkout.md
├── data-structures/
│   ├── README.md
│   └── hash-maps.md
├── algorithms/
│   ├── README.md
│   └── sorting.md
├── devops/
│   ├── README.md
│   └── docker.md
├── security/
│   ├── README.md
│   └── owasp-top-10.md
├── databases/
│   ├── README.md
│   └── sql-optimization.md
├── api-design/
│   ├── README.md
│   └── rest-best-practices.md
├── testing/
│   ├── README.md
│   └── unit-testing.md
└── github_repos/
    ├── README.md
    ├── ai-agents-skills/
    │   ├── README.md
    │   ├── agency-agents.md
    │   ├── agent-skills.md
    │   ├── codebase-memory-mcp.md
    │   ├── crewai.md
    │   ├── graft.md
    │   ├── graphify.md
    │   ├── gsd-core.md
    │   ├── hyperresearch.md
    │   ├── mattpocock-skills.md
    │   ├── ponytail.md
    │   ├── ralph.md
    │   └── superpowers.md
    ├── developer-tools/
    │   ├── README.md
    │   ├── ackee.md
    │   ├── bun.md
    │   ├── harper.md
    │   ├── kanbn.md
    │   ├── omniroute.md
    │   ├── the-book-of-secret-knowledge.md
    │   └── vercel.md
    ├── learning-resources/
    │   ├── README.md
    │   ├── coding-interview-university.md
    │   ├── javascript-algorithms.md
    │   ├── project-based-learning.md
    │   └── system-design-primer.md
    └── media-productivity/
        ├── README.md
        ├── cap.md
        ├── excalidraw.md
        ├── fish-speech.md
        ├── handy.md
        ├── kokoro.md
        ├── meetily.md
        ├── open-notebook.md
        ├── penpot.md
        └── upscayl.md
```

---

## 📜 License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute.

---

<div align="center">

**⭐ Star this repo if you find it useful! ⭐**

Built with ❤️ by the developer community.

</div>

