# Matt Pocock's Skills

[![GitHub Stars](https://img.shields.io/github/stars/mattpocock/skills?style=flat-square&color=111111&label=stars)](https://github.com/mattpocock/skills)
[![License: MIT](https://img.shields.io/badge/License-MIT-111111.svg?style=flat-square)](LICENSE)

**Portable, high-discipline engineering workflows and skills for AI coding agents.**

Created by Matt Pocock (TypeScript educator and engineer), `mattpocock/skills` is a public collection of structured, opinionated engineering workflows designed to replace unstructured "vibe coding" with rigorous, reproducible software development practices.

---

## 📋 Overview

- **What**: A curated set of agentic skills, prompts, and runbooks (packaged for 70+ AI coding agents including Claude Code, Cursor, Antigravity, Copilot, and Windsurf) emphasizing disciplined engineering habits.
- **Why**: AI agents tend to jump straight into writing code without understanding context, interrogating specs, or running tests. Matt Pocock's skills enforce process-driven gates such as TDD, PRD specification, and deep codebase research.
- **Key Philosophy**: Small, readable, highly composable process units that turn AI agents into disciplined pair-programming partners.

---

## 🔑 Core Skills & Workflows

The repository organizes skills into structured categories:

### 🛠️ Engineering Workflows

| Skill | Description | Primary Trigger / Use Case |
|---|---|---|
| `ask-matt` | Channel Matt Pocock's TypeScript and engineering judgment for complex architectural queries | Architectural guidance & TS patterns |
| `code-review` | Thorough multi-axis review focusing on type safety, readability, and performance | Before submitting or merging code |
| `codebase-design` | Systematic architectural evaluation and domain boundary mapping | Designing new features or refactoring modules |
| `diagnosing-bugs` | Root-cause analysis workflow (reproduce, isolate, test, fix) | Debugging unexpected test/runtime errors |
| `domain-modeling` | Type-driven domain modeling with clean interfaces and invariants | Defining domain data structures |
| `grill-with-docs` | Interactive interrogation of specs against official framework documentation | Validating tech stack integration |
| `implement` | Structured step-by-step implementation following verified specs | Building approved plan items |
| `improve-codebase-architecture` | Systematic identification and elimination of architectural debt | Refactoring complex codebases |
| `prototype` | Fast spike/prototype mode with explicit boundaries before production coding | Exploring unknown solutions |
| `research` | Targeted codebase research and dependency analysis before coding | Understanding existing code |
| `resolving-merge-conflicts` | Guided resolution of git merge conflicts preserving intent | Handling complex git merges |
| `setup-matt-pocock-skills` | Bootstrap and configure Matt Pocock's skills in any repository | Initial environment setup |
| `tdd` | Enforced Red-Green-Refactor test-driven development loop | Writing new logic or bug fixes |
| `to-spec` | Convert unstructured user requests into complete, actionable specifications | Scoping vague requirements |
| `to-tickets` | Break down high-level specs into small, verifiable issue tickets | Task planning & decomposition |
| `triage` | Rapid bug and issue triage workflow | Processing incoming bug reports |
| `wayfinder` | Codebase navigation helper for finding symbols, entry points, and contracts | Navigating large codebases |
| `wizard` | Interactive wizard guiding multi-phase feature development | Complex end-to-end features |

---

## 🚀 Quick Start & Installation

### Using the Open Skills CLI

Install directly into 70+ supported agents (Claude Code, Cursor, Antigravity, Copilot, etc.):

```bash
# Browse skills
npx skills add mattpocock/skills --list

# Install specific skills
npx skills add mattpocock/skills --skill tdd
npx skills add mattpocock/skills --skill code-review
```

### Native Agent Integrations

<details>
<summary><b>Claude Code</b></summary>

Install directly via plugin marketplace:

```bash
/plugin marketplace add mattpocock/skills
/plugin install skills@mattpocock-skills
```

Or copy skills locally into `.claude/skills/` or `.agents/skills/`.

</details>

<details>
<summary><b>Antigravity CLI / Gemini CLI</b></summary>

Install as native skills:

```bash
agy plugin install https://github.com/mattpocock/skills.git
```

Or place the skills in your workspace `.agents/skills/` directory for automatic discovery.

</details>

<details>
<summary><b>Cursor & Windsurf</b></summary>

Sync workflow skills into `.cursor/skills/` or `.windsurf/skills/`.

</details>

---

## 💡 Best Practices

1. **Spec Before Code**: Use `to-spec` before invoking `implement` or `tdd` to ensure full alignment on requirements.
2. **Stress-Test Assumptions**: Use `grill-with-docs` to stress-test proposed designs against actual documentation.
3. **Atomic Task Breakdown**: Use `to-tickets` to keep agent tasks small, testable, and verifiable.

---

## 📚 References & Resources

- **GitHub Repository**: [mattpocock/skills](https://github.com/mattpocock/skills)
- **Author**: [Matt Pocock](https://github.com/mattpocock)

---

*← Back to [AI Agents & Skills](./README.md) · [GitHub Repos Hub](../README.md) · [Root Index](../../README.md)*
