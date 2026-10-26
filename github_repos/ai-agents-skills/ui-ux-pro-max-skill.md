> 🔗 **GitHub Repository**: [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)

---

# 🎨 UI/UX Pro Max

> **Design intelligence and local design-system search engine for AI coding agents.** Equips agents like Claude Code, Cursor, Windsurf, and Cline with a comprehensive, offline-searchable database of 50+ UI styles, harmonious color palettes, Google font pairings, and accessibility guidelines before they write code.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![GitHub Stars](https://img.shields.io/github/stars/nextlevelbuilder/ui-ux-pro-max-skill?style=social)](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)
[![Platform: Cross-Agent](https://img.shields.io/badge/Platform-Claude_Code_|_Cursor_|_Cline-blueviolet.svg)](#-installation--setup)
[![Upstream Repository](https://img.shields.io/badge/upstream-nextlevelbuilder%2Fui--ux--pro--max--skill-fuchsia.svg)](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)

---

## 🚀 Overview

AI coding assistants frequently generate repetitive, generic user interfaces—often defaulting to standard shades of blue and gray with formulaic 3-card grids. 

**UI/UX Pro Max** fixes this by serving as a dedicated design intelligence layer. Before generating UI code, the agent queries an embedded, 100% local database using an integrated BM25 search engine (`search.py`) to discover domain-tailored color schemes, typography pairings, and modern design archetypes (e.g., Bento Grid, Glassmorphism, Brutalism, Minimalist Luxury).

---

## ⚡ Core Capabilities

- **Zero-Dependency Local BM25 Search**: Includes a standalone Python search utility (`search.py`) powered entirely by Python standard library modules with no external pip requirements or network latency.
- **50+ Curated UI Styles**: Comprehensive style guides for Bento Grid, Glassmorphism, Dark Neumorphism, High-Tech Cyberpunk, Minimalist Scandinavian, Retro Terminal, and more.
- **Industry & Domain Palettes**: Tailored color palettes with emotional and psychological rationale for FinTech, Healthcare, E-Commerce, Developer Tools, CyberSec, and Web3.
- **Font Pairings**: Curated header/body typography pairings ready for immediate Google Fonts or `@font-face` import.
- **Component Blueprinting (`MASTER.md`)**: Guides the agent to produce a foundational design token and component architecture document before writing implementation code.
- **Framework Agnostic**: Includes implementation recipes for Tailwind CSS, shadcn/ui, React, Next.js, Vue, Svelte, Flutter, and SwiftUI.

---

## 📦 Installation & Setup

### Claude Code Plugin Marketplace

```bash
# Add the marketplace source
/plugin marketplace add nextlevelbuilder/ui-ux-pro-max-skill

# Install the skill
/plugin install ui-ux-pro-max@ui-ux-pro-max-skill
```

### Universal Skills CLI

```bash
# Install globally for all supported coding agents
npx skills add nextlevelbuilder/ui-ux-pro-max-skill -g
```

### Manual Installation (Cursor / Windsurf / Cline)

Clone directly into your project's agent skills directory:

```bash
# For Cursor rules
mkdir -p .cursor/rules
git clone https://github.com/nextlevelbuilder/ui-ux-pro-max-skill.git .cursor/skills/ui-ux-pro-max

# For agent workspaces
mkdir -p .agents/skills/ui-ux-pro-max
git clone https://github.com/nextlevelbuilder/ui-ux-pro-max-skill.git .agents/skills/ui-ux-pro-max
```

---

## 🛠️ Typical Agent Workflows

```text
# 1. Search for design inspiration by industry
"Search UI/UX Pro Max for FinTech dashboard styles, recommended dark palettes, and typography pairings."

# 2. Generate a design system blueprint
"Create a MASTER.md design specification for a developer analytics platform using the Bento Grid style."

# 3. Build components adhering to the blueprint
"Implement the analytics dashboard homepage in Next.js and Tailwind CSS matching the MASTER.md specification."
```

---

## 🔗 Official Links

- **GitHub Repository**: [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)

---

*← Back to [AI Agents & Skills](./README.md) · [GitHub Repos Hub](../README.md) · [Root Index](../../README.md)*
