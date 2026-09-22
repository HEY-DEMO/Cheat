# Harper

> **Category**: `tools/free` · **Last Updated**: `2026-09-21` · **Difficulty**: `Beginner`

---

## TL;DR

Harper is an open-source, privacy-first, offline grammar and spell checker designed for developers and writers. It runs entirely on-device in Rust with sub-10ms latency and zero telemetry.

---

## 📋 Overview

- **What**: A blazing-fast local grammar and spell checker available as an LSP server (`harper-ls`), browser extension, Obsidian plugin, and desktop app.
- **Why**: Cloud grammar checkers (e.g., Grammarly) send every keystroke over the internet, introduce network latency, and train AI models on private proprietary code and communications.
- **When**: Writing technical documentation, composing emails, writing markdown notes, and linting code comments/docstrings in Neovim, VS Code, or Helix.

---

## 🔑 Key Concepts

| Concept | Description |
|---|---|
| **Zero Cloud Telemetry** | 100% on-device deterministic processing; no text ever leaves your local machine. |
| **No Generative AI** | Uses high-speed linguistic and grammatical algorithms in pure Rust; never hallucinates or modifies your original tone. |
| **Code & Markdown Awareness** | Specifically ignores variable names, functions, and syntax tags while parsing docstrings and comments. |
| **LSP Architecture (`harper-ls`)** | Exposes standard Language Server Protocol endpoints compatible with any modern code editor. |
| **Multi-Dialect English** | Native dictionary and dialect support for American, British, Canadian, Australian, and Indian English. |

---

## ⚙️ Editor & LSP Setup

### 1. Install `harper-ls` (Language Server)

```bash
# Using Cargo (Rust)
cargo install harper-ls

# Or using Homebrew (macOS/Linux)
brew install harper-ls
```

### 2. Neovim Configuration (`nvim-lspconfig`)

```lua
require('lspconfig').harper_ls.setup {
  settings = {
    ["harper-ls"] = {
      userDictPath = "~/dict.txt",
      dialect = "American", -- Options: "American", "British", "Canadian", "Australian", "Indian"
      linters = {
        SpellCheck = true,
        SpelledNumbers = false,
        AnA = true,
        SentenceCapitalization = true,
        UnclosedQuotes = true,
      }
    }
  }
}
```

### 3. VS Code

Install the official **Harper** extension from the Visual Studio Marketplace. It activates automatically on Markdown and code files, highlighting grammatical errors and typos via standard editor squiggles.

---

## ⚠️ Anti-Patterns

| ❌ Anti-Pattern | ✅ Better Approach |
|---|---|
| Sending proprietary company code to cloud grammar extensions | Use Harper for offline, air-gapped linting where confidential IP remains strictly on-device. |
| Disabling grammar linting because tools flag code identifiers | Configure Harper's dialect and custom user dictionary (`userDictPath`) to ignore domain jargon. |
| Expecting Harper to rewrite sentences from scratch like ChatGPT | Use Harper as a precise proofreader; it catches real grammatical errors without changing your voice. |

---

## 🌍 Real-World Use Case

**Scenario**: A healthcare fintech team works in an air-gapped, HIPAA-regulated environment with strict prohibitions against sending clipboard or editor text to external cloud APIs.

**Solution**: The team standardizes on `harper-ls` in their development containers and VS Code editors.

**Result**: Developers and technical writers get real-time spelling and grammar validation across thousands of lines of markdown documentation and code comments with 0 byte egress.

---

## 🔗 Related Topics

- [Harper Repository Documentation](../../github_repos/harper.md) — Full upstream GitHub repository and architecture.
- [VS Code](./vscode.md) — Free extensible code editor.

---

## 📚 References

- [Harper Official Website](https://writewithharper.com)
- [Harper Documentation](https://writewithharper.com/docs/about)
- [GitHub Repository](https://github.com/automattic/harper)

---

*← Back to [Free Tools](./README.md) · [Root Index](../../README.md)*
