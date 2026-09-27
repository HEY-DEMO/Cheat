> 🔗 **GitHub Repository**: [obra/superpowers](https://github.com/obra/superpowers)

---

# Superpowers

[![GitHub Stars](https://img.shields.io/github/stars/obra/superpowers?style=flat-square&color=111111&label=stars)](https://github.com/obra/superpowers)
[![License: MIT](https://img.shields.io/badge/License-MIT-111111.svg?style=flat-square)](LICENSE)

**An agentic skills framework and comprehensive software development methodology for AI coding agents.**

Superpowers (by Jesse Vincent / `@obra`) is a complete, structured development framework designed to turn AI coding agents into disciplined, autonomous software engineers.

---

## 📋 Overview

- **What**: An extensible framework providing workflows, git worktree isolation, test-driven iterations, systematic planning, and automated pull-request generation for AI agents.
- **Why**: AI agents frequently make uncoordinated edits directly on main working trees, miss regression testing, and struggle with multi-step implementations. Superpowers introduces isolated git worktrees, strict planning phases, and automated verification loops.
- **Key Philosophy**: Comprehensive methodology over ad-hoc prompting—giving agents structured "superpowers" for every step of software delivery.

---

## 🔑 Core Features & Methodology

```
 ┌────────────────┐     ┌────────────────┐     ┌────────────────┐     ┌────────────────┐
 │ 1. Git Worktree│ ──► │ 2. Structured  │ ──► │ 3. Test-Driven │ ──► │ 4. Automated   │
 │   Isolation    │     │    Planning    │     │   Execution    │     │  PR Creation   │
 └────────────────┘     └────────────────┘     └────────────────┘     └────────────────┘
```

| Feature | Description |
|---|---|
| **Git Worktree Isolation** | Automatically creates clean git worktrees for feature work, preventing working directory contamination. |
| **Systematic Planning** | Forces step-by-step breakdown and architectural review before code generation begins. |
| **Test-Driven Iteration** | Requires failing test reproduction (Red) before writing fixes/features (Green), followed by refactoring. |
| **Automated PR Generation** | Summarizes changes, verifies CI test suites, and constructs comprehensive pull requests. |
| **Multi-Agent Ecosystem** | Integrates with `superpowers-marketplace` and `superpowers-lab` for custom agent skills and plugins. |

---

## 🚀 Quick Start & Installation

### Claude Code Plugin Setup

Install Superpowers natively in Claude Code:

```bash
/plugin marketplace add obra/superpowers
/plugin install superpowers@obra-superpowers
```

### Antigravity CLI / Gemini CLI

Install as an extension/plugin:

```bash
agy plugin install https://github.com/obra/superpowers.git
```

### Manual / Workspace Installation

Clone into your workspace's `.agents/` or `~/.gemini/config/plugins/` directory:

```bash
git clone https://github.com/obra/superpowers.git .agents/plugins/superpowers
```

---

## 🛠️ Usage & Commands

| Command | Purpose |
|---|---|
| `/superpowers:plan` | Initiate systematic feature planning and spec breakdown. |
| `/superpowers:worktree` | Create and switch to a dedicated git worktree for the current task. |
| `/superpowers:test-drive` | Run strict TDD iteration cycle (write test -> verify failure -> fix -> verify pass). |
| `/superpowers:pr` | Generate structured PR summary and verify all quality checks. |

---

## 📚 Related Repositories & Ecosystem

- **[obra/superpowers-marketplace](https://github.com/obra/superpowers-marketplace)**: Curated repository of community skills and plugins for Superpowers.
- **[obra/superpowers-lab](https://github.com/obra/superpowers-lab)**: Experimental techniques and bleeding-edge agent workflows.

---

## 📚 References

- **GitHub Repository**: [obra/superpowers](https://github.com/obra/superpowers)
- **Author**: [Jesse Vincent (@obra)](https://github.com/obra)

---

*← Back to [AI Agents & Skills](./README.md) · [GitHub Repos Hub](../README.md) · [Root Index](../../README.md)*
