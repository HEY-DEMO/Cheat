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
| 1  | 📁 Design Patterns        | 19 GoF patterns: Creational, Structural, Behavioral | [design-patterns/](design-patterns/README.md)               |
| 2  | 📁 Architecture            | System design, microservices, AI agent patterns, etc.| [architecture/](architecture/README.md)                     |
| 3  | 📁 Tools                   | Developer tools — free and paid                     | [tools/](tools/README.md)                                   |
| 4  | 🏷️ └─ Free Tools          | Open-source and free-tier tools                      | [tools/free/](tools/free/README.md)                         |
| 5  | 🏷️ └─ Paid Tools          | Commercial and premium tools                         | [tools/paid/](tools/paid/README.md)                         |
| 6  | 📁 Best Practices          | Code quality, reviews, testing strategies           | [best-practices/](best-practices/README.md)                 |
| 7  | 📁 Security                | AppSec, OWASP, authentication, encryption           | [security/](security/README.md)                             |
| 8  | 📁 Databases               | SQL, NoSQL, query optimization, migrations          | [databases/](databases/README.md)                           |
| 9  | 📁 Testing                 | Unit, integration, E2E, TDD, interactive debugging  | [testing/](testing/README.md)                               |
| 10 | 📁 Networking              | Protocols, addressing, OSI model, ports, subnets, VPN | [networking/](networking/README.md)                         |
| 11 | 📁 System Design           | Scalable architectures, core concepts & scenarios   | [system-design/](system-design/README.md)                   |
| 12 | 🏷️ └─ Concepts             | Scalability building blocks (caching, sharding, CAP) | [system-design/concepts/](system-design/concepts/README.md) |
| 13 | 🏷️ └─ Scenarios            | End-to-end design problems (URL shortener, chat)     | [system-design/scenarios/](system-design/scenarios/README.md)|
| 14 | 📁 GitHub Repos            | Curated open-source repositories and agent tooling  | [github_repos/](github_repos/README.md)                     |

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
│   ├── composite.md
│   ├── decorator.md
│   ├── facade.md
│   ├── flyweight.md
│   ├── proxy.md
│   ├── chain-of-responsibility.md # Behavioral
│   ├── command.md
│   ├── iterator.md
│   ├── observer.md
│   ├── state.md
│   ├── strategy.md
│   └── template-method.md
├── architecture/
│   ├── README.md
│   ├── microservices.md
│   ├── event-driven.md
│   ├── backend-architecture.md
│   └── ai-agent-patterns.md
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
│   │   ├── interactive-debugging.md
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
├── security/
│   ├── README.md
│   ├── owasp-top-10.md
│   ├── secret-scanning.md
│   └── vibe-coded-saas-security.md
├── databases/
│   ├── README.md
│   ├── kuzu.md
│   └── sql-optimization.md
├── testing/
│   ├── README.md
│   ├── interactive-debugging.md
│   └── unit-testing.md
├── networking/
│   ├── README.md
│   └── networking-concepts.md
├── system-design/
│   ├── README.md
│   ├── concepts/
│   │   ├── README.md
│   │   ├── traffic-and-routing.md
│   │   ├── scaling-and-deployment.md
│   │   ├── resiliency-and-fault-tolerance.md
│   │   ├── asynchronous-and-realtime.md
│   │   ├── database-and-storage.md
│   │   ├── concurrency-and-compute.md
│   │   ├── observability-and-sre.md
│   │   ├── security-and-protection.md
│   │   └── protocols-and-network.md
│   └── scenarios/
│       └── README.md
└── github_repos/
    ├── README.md
    ├── ai-agents-skills/
    │   ├── README.md
    │   ├── agency-agents.md
    │   ├── agent-skills.md
    │   ├── andrej-karpathy-skills.md
    │   ├── awesome-claude-code.md
    │   ├── chisle.md
    │   ├── claude-code-best-practice.md
    │   ├── claude-code-system-prompts.md
    │   ├── codebase-memory-mcp.md
    │   ├── crewai.md
    │   ├── diagram-design.md
    │   ├── everything-claude-code.md
    │   ├── graft.md
    │   ├── graphify.md
    │   ├── gsd-core.md
    │   ├── hallmark.md
    │   ├── headroom.md
    │   ├── hyperresearch.md
    │   ├── last30days-skill.md
    │   ├── mattpocock-skills.md
    │   ├── pentagi.md
    │   ├── ponytail.md
    │   ├── ralph.md
    │   ├── rea.md
    │   ├── reticle.md
    │   ├── security-audit-skill.md
    │   ├── skillspector.md
    │   ├── superpowers.md
    │   ├── ui-skills.md
    │   ├── ui-ux-pro-max-skill.md
    │   └── understand-anything.md
    ├── curated-lists/
    │   ├── README.md
    │   ├── awesome-python.md
    │   ├── awesome.md
    │   ├── free-programming-books.md
    │   └── public-apis.md
    ├── developer-tools/
    │   ├── README.md
    │   ├── ackee.md
    │   ├── anti-slop.md
    │   ├── betterleaks.md
    │   ├── bun.md
    │   ├── gitleaks.md
    │   ├── harper.md
    │   ├── kanbn.md
    │   ├── needle.md
    │   ├── omniroute.md
    │   ├── onyx.md
    │   ├── scrapling.md
    │   ├── the-book-of-secret-knowledge.md
    │   └── vercel.md
    ├── learning-resources/
    │   ├── README.md
    │   ├── build-your-own-x.md
    │   ├── coding-interview-university.md
    │   ├── developer-roadmap.md
    │   ├── freecodecamp.md
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

