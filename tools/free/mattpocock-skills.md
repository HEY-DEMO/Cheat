# Matt Pocock's Skills

> **Category**: `tools/free` · **Last Updated**: `2026-09-22` · **Difficulty**: `Intermediate`

---

## TL;DR

Matt Pocock's Skills (`mattpocock/skills`) is a collection of structured, opinionated engineering workflows designed to replace unstructured "vibe coding" with high-discipline software development practices across 70+ AI coding agents.

---

## 📋 Overview

- **What**: Reusable skills, prompts, and runbooks covering TDD, code review, bug diagnosis, domain modeling, and spec breakdown.
- **Why**: AI agents left without structure tend to jump straight into writing code without understanding context, checking docs, or writing tests. Matt Pocock's skills enforce process-driven quality gates.
- **When**: All agentic coding sessions where you want structured, reproducible engineering workflows (from scoping requirements to PR reviews).

---

## 🔑 Key Concepts & Workflow

| Concept | Description |
|---|---|
| **Engineering Discipline** | Replaces unstructured code generation with explicit process phases (Spec -> Plan -> Build -> Verify -> Review). |
| **Type-Driven Modeling** | Enforces clean TypeScript domain models, clear module interfaces, and explicit type safety checks. |
| **Doc-Grounded Verification** | Stress-tests proposed implementations against official framework documentation via `grill-with-docs`. |
| **TDD Enforcement** | Strict Red-Green-Refactor execution loops to guarantee software correctness. |

---

## 💻 Quick Start & Agent Setup

Install into your AI coding agent using the open [skills CLI](https://github.com/vercel-labs/skills):

```bash
# Install specific skills
npx skills add mattpocock/skills --skill tdd
npx skills add mattpocock/skills --skill code-review
npx skills add mattpocock/skills --skill to-spec
```

### Claude Code Setup

```bash
/plugin marketplace add mattpocock/skills
/plugin install skills@mattpocock-skills
```

### Antigravity / Gemini CLI Setup

```bash
agy plugin install https://github.com/mattpocock/skills.git
```

---

## ⚠️ Anti-Patterns

| ❌ Anti-Pattern | ✅ Better Approach |
|---|---|
| Asking an agent to build a feature without a written spec | Use `to-spec` to generate an explicit requirement specification first. |
| Accepting untested code diffs | Run the `tdd` skill loop to ensure failing tests pass before accepting code changes. |
| Guessing third-party API behavior | Use `grill-with-docs` to verify framework and library interfaces against official docs. |

---

## 🌍 Real-World Use Case

**Scenario**: A team wants to prevent AI agents from generating speculative, un-typed JavaScript/TypeScript code that breaks in production.

**Solution**: The team configures `mattpocock/skills` across their `.claude/` and `.agents/` repository configs.

**Result**: AI agents automatically follow `to-spec`, `domain-modeling`, and `tdd` workflows, delivering well-typed, thoroughly tested pull requests.

---

## 🔗 Related Topics

- [Matt Pocock's Skills Repository Documentation](../../github_repos/ai-agents-skills/mattpocock-skills.md) — Upstream GitHub repository.
- [Agent Skills](./agent-skills.md) — Production-grade SDLC engineering skills.
- [Superpowers](./superpowers.md) — Agentic development methodology framework.

---

## 📚 References

- [GitHub Repository](https://github.com/mattpocock/skills)
- [Matt Pocock's Twitter/X](https://x.com/mattpocockuk)

---

*← Back to [Free Tools](./README.md) · [Root Index](../../README.md)*
