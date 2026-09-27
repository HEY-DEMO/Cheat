> 🔗 **GitHub Repository**: [open-gsd/gsd-core](https://github.com/open-gsd/gsd-core)

---

<div align="center">

# GSD Core

**Git. Ship. Done.**

**English** · [Português](https://github.com/open-gsd/gsd-core/blob/main/README.pt-BR.md) · [简体中文](https://github.com/open-gsd/gsd-core/blob/main/README.zh-CN.md) · [日本語](https://github.com/open-gsd/gsd-core/blob/main/README.ja-JP.md) · [한국어](https://github.com/open-gsd/gsd-core/blob/main/README.ko-KR.md)

**A light-weight meta-prompting, context engineering, and spec-driven development system for Claude Code, OpenCode, Antigravity CLI, Kimi CLI, Kilo, Codex, Copilot, Cursor, Windsurf, and more.**

[![npm version](https://img.shields.io/npm/v/%40opengsd%2Fgsd-core?style=for-the-badge&logo=npm&logoColor=white&color=CB3837)](https://www.npmjs.com/package/@opengsd/gsd-core)
[![npm downloads](https://img.shields.io/npm/dm/%40opengsd%2Fgsd-core?style=for-the-badge&logo=npm&logoColor=white&color=CB3837)](https://www.npmjs.com/package/@opengsd/gsd-core)
[![Tests](https://img.shields.io/github/actions/workflow/status/open-gsd/gsd-core/test.yml?branch=main&style=for-the-badge&logo=github&label=Tests)](https://github.com/open-gsd/gsd-core/actions/workflows/test.yml)
[![Discord](https://img.shields.io/badge/Discord-Join-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/mYgfVNfA2r)
[![GitHub stars](https://img.shields.io/github/stars/open-gsd/gsd-core?style=for-the-badge&logo=github&color=181717)](https://github.com/open-gsd/gsd-core)
[![License](https://img.shields.io/badge/license-MIT-blue?style=for-the-badge)](LICENSE)

</div>

---

## What is GSD Core

GSD Core is a context-engineering and spec-driven development framework that drives AI coding agents (Claude Code, Codex, Antigravity CLI, Kimi CLI, Copilot, Cursor, and more) through a disciplined phase loop. It solves [context rot](https://github.com/open-gsd/gsd-core/blob/main/docs/explanation/context-engineering.md) — the quality degradation that accumulates as an AI fills its context window — by running all heavy research, planning, and execution work in fresh-context subagents while keeping your main session lean.

---

## How it works

Each milestone repeats the same five-step loop, one phase at a time:

1. **Discuss** — capture implementation decisions before anything is planned
2. **Plan** — research, decompose, and verify the plan fits a fresh context window
3. **Execute** — run plans in parallel waves; each executor starts with a clean 200k-token context
4. **Verify** — walk through what was built; diagnose and fix before declaring done
5. **Ship** — create the PR, archive the phase, repeat for the next one

---

## Quickstart

```bash
npx @opengsd/gsd-core@latest
```

The installer prompts for your runtime (Claude Code, OpenCode, Antigravity CLI, Kimi CLI, Kilo, Codex, Copilot, Cursor, Windsurf, and more) and whether to install globally or locally. The installer is required for cross-runtime compatibility — do not copy files from `agents/` or `commands/` directly.

On another runtime or without Node.js? See [Install on your runtime](https://github.com/open-gsd/gsd-core/blob/main/docs/how-to/install-on-your-runtime.md).

Once installed, start a new project or onboard an existing repo:

```bash
/gsd-new-project   # greenfield project
/gsd-onboard       # existing codebase
```

New here? Follow [Your first project](https://github.com/open-gsd/gsd-core/blob/main/docs/tutorials/your-first-project.md) for a guided walkthrough from install to first shipped phase, or [Onboarding an existing codebase](https://github.com/open-gsd/gsd-core/blob/main/docs/tutorials/onboarding-an-existing-codebase.md) for brownfield setup.

---

## Documentation

**What's new in 1.7.0** → [docs/whats-new-1.7.0.md](https://github.com/open-gsd/gsd-core/blob/main/docs/whats-new-1.7.0.md)

**Tutorials** — learning by doing:
- [Your first project](https://github.com/open-gsd/gsd-core/blob/main/docs/tutorials/your-first-project.md)
- [Onboarding an existing codebase](https://github.com/open-gsd/gsd-core/blob/main/docs/tutorials/onboarding-an-existing-codebase.md)

**How-to guides** — task-focused recipes:
- [Install on your runtime](https://github.com/open-gsd/gsd-core/blob/main/docs/how-to/install-on-your-runtime.md)
- [Plan a phase](https://github.com/open-gsd/gsd-core/blob/main/docs/how-to/plan-a-phase.md)
- [Verify and ship](https://github.com/open-gsd/gsd-core/blob/main/docs/how-to/verify-and-ship.md)
- … [see all how-to guides](https://github.com/open-gsd/gsd-core/blob/main/docs/README.md#how-to-guides)

**Reference** — authoritative facts:
- [Commands](https://github.com/open-gsd/gsd-core/blob/main/docs/COMMANDS.md)
- [Configuration](https://github.com/open-gsd/gsd-core/blob/main/docs/CONFIGURATION.md)
- [CLI tools](https://github.com/open-gsd/gsd-core/blob/main/docs/CLI-TOOLS.md)

**Explanation** — concepts and design decisions:
- [Context engineering](https://github.com/open-gsd/gsd-core/blob/main/docs/explanation/context-engineering.md)
- [The phase loop](https://github.com/open-gsd/gsd-core/blob/main/docs/explanation/the-phase-loop.md)
- [Architecture](https://github.com/open-gsd/gsd-core/blob/main/docs/ARCHITECTURE.md)

Full index: [docs/README.md](https://github.com/open-gsd/gsd-core/blob/main/docs/README.md). Other languages: [日本語](https://github.com/open-gsd/gsd-core/blob/main/README.ja-JP.md) · [한국어](https://github.com/open-gsd/gsd-core/blob/main/README.ko-KR.md) · [Português](https://github.com/open-gsd/gsd-core/blob/main/README.pt-BR.md) · [简体中文](https://github.com/open-gsd/gsd-core/blob/main/README.zh-CN.md).

---

## Why it works

Most AI-coding setups fail at scale because context bloat silently degrades output quality, there is no shared memory between sessions, and nothing verifies that code actually works. GSD Core solves all three: heavy work runs in fresh subagents, structured artifacts like `STATE.md` and `CONTEXT.md` survive session boundaries, and the verify step walks through what was built and generates fix plans before a phase is declared done. See [docs/explanation/context-engineering.md](https://github.com/open-gsd/gsd-core/blob/main/docs/explanation/context-engineering.md) for the full reasoning.

Troubleshooting? See [docs/how-to/recover-and-troubleshoot.md](https://github.com/open-gsd/gsd-core/blob/main/docs/how-to/recover-and-troubleshoot.md).

---

## Community

| Project | Platform |
|---------|----------|
| [gsd-opencode](https://github.com/rokicool/gsd-opencode) | Original OpenCode port |
| [Discord](https://discord.gg/mYgfVNfA2r) | Community support |

---

## Star History

<a href="https://star-history.com/#open-gsd/gsd-core&Date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=open-gsd/gsd-core&type=Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=open-gsd/gsd-core&type=Date" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=open-gsd/gsd-core&type=Date" />
 </picture>
</a>

---

## License

MIT License. See [LICENSE](https://github.com/open-gsd/gsd-core/blob/main/LICENSE) for details.

---

<div align="center">

**Claude Code is powerful. GSD Core makes it reliable.**

</div>

---

*← Back to [AI Agents & Skills](./README.md) · [GitHub Repos Hub](../README.md) · [Root Index](../../README.md)*
