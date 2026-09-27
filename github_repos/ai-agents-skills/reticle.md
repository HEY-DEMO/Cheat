# 🎯 Reticle

> **Runtime test & verification engine for AI coding agents.** Your AI agent says "done." Reticle drives your real running application, inspects what actually happened, and returns pass / fail verdicts with the exact `file:line` to fix.

[![npm](https://img.shields.io/npm/v/@reticlehq/server?color=8b7bff&labelColor=15131f&logo=npm)](https://www.npmjs.com/package/@reticlehq/server)
[![License](https://img.shields.io/badge/license-Apache--2.0%20%2B%20FSL-46d6a0?labelColor=15131f)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/reticlehq/reticle?color=ff9f87&labelColor=15131f&logo=github)](https://github.com/reticlehq/reticle)
[![Upstream Repository](https://img.shields.io/badge/upstream-reticlehq%2Freticle-blueviolet.svg)](https://github.com/reticlehq/reticle)

---

## 🚀 Overview

When AI coding agents (Claude Code, Cursor, Windsurf, Copilot, Gemini CLI) claim a task is completed, they typically rely on unit tests or superficial static analysis. Subtle runtime bugs, state mutations, failed network calls, and UI glitches frequently slip through.

**Reticle** closes this gap by:
1. Connecting directly to your running dev server.
2. Automating browser interactions and observing app internals (DOM, network requests, state store).
3. Providing clear **pass · fail · couldn't tell** verdicts with exact source code references (`file:line`) directly inside your agent session.

---

## ⚡ Key Features

- **Agent-First Verification**: Exposes MCP tools and the `/reticle` skill so coding agents can test their own work before reporting completion.
- **Deep Runtime Inspection**: Monitors the live DOM, application state store (Redux, Zustand, Pinia, etc.), and network payloads rather than just relying on visual snapshots.
- **Broad Agent Support**: Seamlessly registers with Claude Code, Cursor, Windsurf, VS Code, Zed, Gemini CLI, Copilot CLI, OpenCode, Warp, Kiro, and Continue.
- **Zero-Syntax Instructions**: Instruct your agent in plain natural language (e.g., *"Verify checkout with Reticle before saying done"*).
- **Local & Privacy-Preserving**: Runs 100% locally on your machine without requiring an external cloud account.

---

## 📦 Installation & Setup

### 1. Run the Global Installer

**macOS / Linux:**
```bash
curl -fsSL https://raw.githubusercontent.com/reticlehq/reticle/main/install/install.sh | sh
```

**Windows (PowerShell):**
```powershell
irm https://raw.githubusercontent.com/reticlehq/reticle/main/install/install.ps1 | iex
```

This places `reticle` on your `PATH` and registers the MCP server with all installed coding agents automatically.

### 2. Connect Your Project

Inside your application repository root:

```bash
npx @reticlehq/server init
```

This configures the dev-only SDK, restarts your development server, connects to your running app, and proves the session is active.

### 3. Verify Connection

```bash
npx @reticlehq/server doctor
```

Or ask your coding agent directly: *"Is Reticle connected to my app?"*

---

## 🛠️ Usage Workflows

You never have to manually author test files; you instruct your coding agent in natural language:

### Verify New Features
> *"I updated the shopping cart checkout logic. Verify it with Reticle before reporting that you are done."*

### Pinpoint Hidden Bugs
> *"The landing page renders, but form submission fails silently. Use Reticle to inspect the network calls and state to find what broke."*

### Prove Bug Fixes
> *"Reproduce the bug where empty search returns 500, implement the fix, and prove the fix passes using the same flow."*

### Prevent Regressions
> *"Lock the authentication flow with Reticle so subsequent refactorings cannot break login."*

---

## 🔌 Claude Code & MCP Integration

### Claude Code Plugin
```text
/plugin marketplace add reticlehq/reticle
/plugin install reticle@reticlehq
```

### Manual MCP Server Configuration
For custom MCP environments, add to your `mcpServers` configuration:

```json
{
  "mcpServers": {
    "reticle": {
      "command": "npx",
      "args": ["@reticlehq/server", "mcp"]
    }
  }
}
```

---

## 🔗 Official Links

- **GitHub Repository**: [reticlehq/reticle](https://github.com/reticlehq/reticle)
- **Documentation**: [docs.reticle.sh](https://docs.reticle.sh)
- **Official Website**: [reticle.sh](https://reticle.sh)
