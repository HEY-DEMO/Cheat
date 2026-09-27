> 🔗 **GitHub Repository**: [Nutlope/hallmark](https://github.com/Nutlope/hallmark)

---

# 🏛️ Hallmark

> **A design skill for Claude Code, Cursor, and Codex that refuses to look AI-generated.** Built by Together AI to eradicate generic aesthetic "slop" using 21 curated themes, 21 macrostructures, and 57 automated slop-test gates.

[![Demo](https://img.shields.io/badge/demo-usehallmark.com-blue)](https://www.usehallmark.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/Nutlope/hallmark?style=social)](https://github.com/Nutlope/hallmark)
[![Upstream Repository](https://img.shields.io/badge/upstream-Nutlope%2Fhallmark-purple.svg)](https://github.com/Nutlope/hallmark)

---

## 🚀 Overview

Most AI models trained on standard web code default to predictable, homogeneous layouts: centered hero text, three identical card columns, standard rounded borders, and purple gradient accents. 

**Hallmark** changes this paradigm:
- Analyzes the specific project brief and selects an intentional macrostructure.
- Implements one of **21 bespoke aesthetic themes** (such as Cold Snap, Bubble, Distil, Cobalt, Carnival, Lumen).
- Runs **57 rigorous slop-test gates** and executes a pre-emission self-critique pass.
- Ensures two applications built for different briefs look completely distinct rather than color-swapped clones of each other.

---

## ⚡ The Four Core Verbs

Hallmark structures its capabilities around four purposeful verbs:

| Command / Verb | Action & Purpose |
|---|---|
| *(default prompt)* | **Build New UI**: Selects an optimal macrostructure, applies designated design tokens, and runs 57 slop tests before outputting code. |
| `hallmark audit <target>` | **Audit & Score**: Evaluates existing frontend files against AI anti-patterns and outputs an actionable punch list without modifying code. |
| `hallmark redesign <target>` | **Rebuild & Refresh**: Retains existing copywriting, brand identity, and information architecture, but discards generic structures to rebuild with distinct craft. |
| `hallmark study <url \| image>` | **Extract Design DNA**: Extracts macrostructures, typography pairings, and color anchors from inspiration sites or screenshots, emitting a portable `design.md` for handoff. |

---

## 📦 Installation & Setup

### Option 1: Via the Skills CLI (Recommended)

```bash
npx skills add nutlope/hallmark
```

*This automatically configures the skill for detected agents (Claude Code, Cursor, Codex).*

### Option 2: Manual Configuration

- **Claude Code**:
  Copy the skill files into your global or project skills directory:
  ```bash
  mkdir -p ~/.claude/skills/hallmark
  cp SKILL.md references/ ~/.claude/skills/hallmark/
  ```

- **Cursor**:
  Place the rule contents into your project's Cursor rules:
  ```bash
  mkdir -p .cursor/rules
  cp SKILL.md .cursor/rules/hallmark.mdc
  ```

- **Codex CLI**:
  ```bash
  mkdir -p ~/.codex/skills/hallmark
  cp SKILL.md references/ ~/.codex/skills/hallmark/
  ```

---

## 🛠️ Example Usage Prompts

```text
# Create a distinctive SaaS landing page
"Use hallmark to build a landing page for a distributed database monitoring tool. Avoid generic SaaS cards."

# Audit existing components for AI tropes
"hallmark audit src/components/DashboardOverview.tsx"

# Redesign an interface with fresh character
"hallmark redesign src/pages/Pricing.tsx with an editorial typography focus."

# Extract aesthetics from an existing site
"hallmark study https://example.com/inspiration and produce a design.md"
```

---

## 🔗 Official Links

- **GitHub Repository**: [Nutlope/hallmark](https://github.com/Nutlope/hallmark)
- **Live Interactive Showcase**: [usehallmark.com](https://www.usehallmark.com)
