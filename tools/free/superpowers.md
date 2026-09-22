# Superpowers

> **Category**: `tools/free` · **Last Updated**: `2026-09-22` · **Difficulty**: `Intermediate`

---

## TL;DR

Superpowers (`obra/superpowers`) is an open-source agentic skills framework and software development methodology that provides AI coding agents with isolated git worktrees, systematic planning, TDD execution loops, and automated PR generation.

---

## 📋 Overview

- **What**: A comprehensive agent methodology and plugin suite for AI coding tools (Claude Code, Antigravity, Cursor, etc.).
- **Why**: AI agents often edit main working trees directly, skip regression testing, and lack structured lifecycle management. Superpowers enforces git worktree isolation, step-by-step planning, and verified pull request generation.
- **When**: Full-cycle software development—especially when working on complex multi-file features where worktree safety and systematic execution are required.

---

## 🔑 Key Concepts

| Concept | Description |
|---|---|
| **Git Worktree Isolation** | Automatically creates clean git worktrees for tasks, isolating edits from your main working tree. |
| **Systematic Planning** | Forces agents to outline steps and verify design decisions before touching code files. |
| **Test-Driven Loop** | Ensures failing test reproduction (Red) before writing implementation code (Green). |
| **Automated PR Creation** | Constructs detailed PR descriptions, verifies test suites, and checks change diffs. |

---

## 💻 Quick Start & Setup

### Claude Code Setup

```bash
/plugin marketplace add obra/superpowers
/plugin install superpowers@obra-superpowers
```

### Antigravity / Gemini CLI Setup

```bash
agy plugin install https://github.com/obra/superpowers.git
```

---

## ⚠️ Anti-Patterns

| ❌ Anti-Pattern | ✅ Better Approach |
|---|---|
| Letting an agent modify your active git working tree directly | Use `/superpowers:worktree` to isolate feature work in a dedicated worktree branch. |
| Coding without a structured plan | Run `/superpowers:plan` to decompose features into verifiable milestones. |
| Creating PRs manually after agent work | Use `/superpowers:pr` to automate PR generation with full test verification evidence. |

---

## 🌍 Real-World Use Case

**Scenario**: A developer is working on a critical production codebase and wants an AI agent to build a new feature without risking uncommitted local work or breaking main branch builds.

**Solution**: The developer activates Superpowers. The agent creates an isolated git worktree (`/superpowers:worktree`), drafts an approved execution plan (`/superpowers:plan`), writes TDD test suites, and opens a clean PR (`/superpowers:pr`).

**Result**: Zero contamination of the primary workspace and 100% test-verified PR submission.

---

## 🔗 Related Topics

- [Superpowers Repository Documentation](../../github_repos/ai-agents-skills/superpowers.md) — Upstream GitHub repository.
- [Matt Pocock's Skills](./mattpocock-skills.md) — High-discipline engineering workflows.
- [Agent Skills](./agent-skills.md) — Production-grade SDLC engineering skills.

---

## 📚 References

- [GitHub Repository](https://github.com/obra/superpowers)
- [Superpowers Marketplace](https://github.com/obra/superpowers-marketplace)

---

*← Back to [Free Tools](./README.md) · [Root Index](../../README.md)*
