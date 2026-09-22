# Agent Skills

> **Category**: `tools/free` · **Last Updated**: `2026-09-21` · **Difficulty**: `Intermediate`

---

## TL;DR

Agent Skills (by Addy Osmani) is a collection of 25 production-grade engineering skills and 9 lifecycle slash commands designed to make AI coding agents follow senior engineering practices across Define, Plan, Build, Test, Review, and Ship phases.

---

## 📋 Overview

- **What**: Reusable skills, prompts, and quality gates packaged for 70+ AI coding agents (Claude Code, Cursor, Windsurf, Copilot, Codex, Cline, Antigravity) via the open `skills` CLI.
- **Why**: Left unguided, AI agents skip specs, write speculative code without tests, ignore accessibility and web performance, and generate brittle monolith diffs. Agent Skills enforces senior engineering workflows automatically.
- **When**: Full-cycle software development—from initial PRD requirements gathering to TDD implementation, code reviews, and production deployment.

---

## 🔑 Key Concepts & Lifecycle Commands

```
  DEFINE          PLAN           BUILD          VERIFY         REVIEW          SHIP
 ┌──────┐      ┌──────┐      ┌──────┐      ┌──────┐      ┌──────┐      ┌──────┐
 │ Idea │ ───► │ Spec │ ───► │ Code │ ───► │ Test │ ───► │  QA  │ ───► │  Go  │
 │Refine│      │  PRD │      │ Impl │      │Debug │      │ Gate │      │ Live │
 └──────┘      └──────┘      └──────┘      └──────┘      └──────┘      └──────┘
  /spec          /plan          /build        /test         /review       /ship
```

| Command | Phase | Core Principle |
|---|---|---|
| `/spec` | Define | Spec before code; interrogation of requirements. |
| `/plan` | Plan | Small, atomic, verifiable task slices. |
| `/build` | Build | Incremental slice implementation; test-driven. |
| `/test` | Verify | Tests are proof; red-green-refactor loop. |
| `/constraints` | Governance | Decide constraints once, enforce everywhere. |
| `/review` | Review | Five-axis code health and quality review. |
| `/webperf` | Audit | Measure Core Web Vitals before optimizing. |
| `/code-simplify`| Refactor | Clarity over cleverness; eliminate tech debt. |
| `/ship` | Deploy | Safe, verified, continuous deployment. |

---

## 💻 Installation

Install into your current coding agent using the open [skills CLI](https://github.com/vercel-labs/skills):

```bash
# Install all 25 skills into your current workspace/agent
npx skills add addyosmani/agent-skills

# Or install individual high-impact skills
npx skills add addyosmani/agent-skills --skill code-review-and-quality
npx skills add addyosmani/agent-skills --skill test-driven-development
npx skills add addyosmani/agent-skills --skill interview-me
```

---

## ⚠️ Anti-Patterns

| ❌ Anti-Pattern | ✅ Better Approach |
|---|---|
| Prompting an agent to "build an entire feature" in one shot | Use `/spec` to define acceptance criteria, `/plan` to slice atomic tasks, and `/build` to execute incrementally. |
| Committing code without automated regression proofs | Run `/test` to enforce verifiable test suites before triggering `/review`. |
| Merging without auditing performance or accessibility | Run `/webperf` and `/review` across performance, accessibility, security, and maintainability axes. |

---

## 🌍 Real-World Use Case

**Scenario**: A tech lead wants junior engineers and AI coding agents to follow consistent, rigorous software engineering standards without needing constant micromanagement.

**Solution**: The team configures `addyosmani/agent-skills` across their `.claude/` and `.cursor/` repository configurations.

**Result**: Every agent-assisted pull request includes verifiable test coverage, structured commit slices, and automated 5-axis code quality reviews.

---

## 🔗 Related Topics

- [Agent Skills Repository Documentation](../../github_repos/ai-agents-skills/agent-skills.md) — Upstream GitHub repository.
- [Ponytail](./ponytail.md) — Senior dev code minimization skill.

---

## 📚 References

- [GitHub Repository](https://github.com/addyosmani/agent-skills)
- [Addy Osmani's Engineering Blog](https://addyosmani.com)

---

*← Back to [Free Tools](./README.md) · [Root Index](../../README.md)*
