# Graphify

> **Category**: `tools/free` · **Last Updated**: `2026-09-21` · **Difficulty**: `Intermediate`

---

## TL;DR

Graphify is a multimodal knowledge graph skill for Claude Code that extracts concepts and relationships across codebases, PDFs, markdown, whiteboard photos, and diagrams—reducing query tokens by 71.5x.

---

## 📋 Overview

- **What**: A CLI and Claude Code skill (`/graphify`) that reads unstructured directories and generates an interactive, persistent knowledge graph.
- **Why**: Feeding entire raw repositories and research archives into agent context windows repeatedly wastes thousands of tokens per query. Graphify precomputes entities, communities, and relationships into a structured graph that persists across sessions.
- **When**: Exploring unfamiliar codebases, analyzing research folders (e.g., Karpathy's `/raw` dump of papers and diagrams), auditing architecture dependencies, and structuring Obsidian vaults.

---

## 🔑 Key Concepts

| Concept | Description |
|---|---|
| **Multimodal Ingestion** | Uses Claude vision to extract semantic relationships from code, markdown, PDFs, whiteboard photos, and diagrams. |
| **71.5x Token Efficiency** | Queries against the synthesized graph require 71.5x fewer tokens than reading raw multi-file corpora. |
| **Interactive Graph (`graph.html`)**| Visual, searchable network graph rendered in the browser with community clustering and node filtering. |
| **Obsidian Vault Export** | Automatically creates an `obsidian/` folder with linked markdown notes and bidirectional wikilinks. |
| **SHA256 Incremental Cache** | Subsequent `/graphify` runs only parse modified or newly added files. |

---

## 💻 Installation & Usage

### 1. Install via pip

```bash
pip install graphifyy && graphify install
```

### 2. Run in Claude Code

Open Claude Code in any directory and type:

```
/graphify .
```

### Generated Output Structure

```
graphify-out/
├── graph.html       # Interactive visual graph (search, filter, explore communities)
├── obsidian/        # Ready-to-open Obsidian vault with bidirectional links
├── wiki/            # Wikipedia-style reference articles for agent navigation
├── GRAPH_REPORT.md  # Key hubs ("god nodes"), surprising connections, and questions
├── graph.json       # Persistent graph representation for future query caching
└── cache/           # SHA256 file hashes for fast incremental updates
```

---

## ⚠️ Anti-Patterns

| ❌ Anti-Pattern | ✅ Better Approach |
|---|---|
| Re-ingesting entire 50MB PDF folders on every prompt | Run `/graphify .` once; query against the generated `graph.json` and `GRAPH_REPORT.md`. |
| Ignoring visual system diagrams in documentation | Feed image files directly into the folder; Graphify uses vision models to incorporate diagrams into node graphs. |

---

## 🌍 Real-World Use Case

**Scenario**: A newly hired engineer needs to understand a 40,000-line legacy microservices codebase consisting of Python, Go, architecture diagrams, and RFC documents.

**Solution**: The engineer runs `/graphify .` in Claude Code.

**Result**: An interactive `graph.html` visualizes service boundaries, god nodes, and inter-module dependencies, allowing the engineer to become productive on day one.

---

## 🔗 Related Topics

- [Graphify Repository Documentation](../../github_repos/graphify.md) — Upstream GitHub repository.
- [codebase-memory-mcp](../../github_repos/codebase-memory-mcp.md) — Persistent code intelligence engine.

---

## 📚 References

- [GitHub Repository](https://github.com/Graphify-Labs/graphify)

---

*← Back to [Free Tools](./README.md) · [Root Index](../../README.md)*
