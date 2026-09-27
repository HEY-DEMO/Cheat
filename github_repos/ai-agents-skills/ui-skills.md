# 🎨 UI Skills

> **Skills for Design Engineers.** A curated registry, CLI, and Model Context Protocol (MCP) server providing opinionated frontend design constraints, micro-interactions, layout principles, and accessibility rules to AI coding agents.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![npm version](https://img.shields.io/npm/v/ui-skills?style=flat-square&color=8b5cf6)](https://www.npmjs.com/package/ui-skills)
[![Website](https://img.shields.io/badge/website-ui--skills.com-purple)](https://www.ui-skills.com/)
[![GitHub Stars](https://img.shields.io/github/stars/ibelick/ui-skills?style=social)](https://github.com/ibelick/ui-skills)
[![Upstream Repository](https://img.shields.io/badge/upstream-ibelick%2Fui--skills-violet.svg)](https://github.com/ibelick/ui-skills)

---

## 🚀 Overview

AI agents are proficient at generating functional code but frequently struggle with the subtle nuances of interface craft: inconsistent spacing, awkward responsive breakpoints, generic typography choices, jarring animation curves, and missing accessibility tags.

**UI Skills** equips AI coding agents (Claude Code, Cursor, Codex, OpenCode) with high-craft design engineering heuristics. It acts as an active design guide, ensuring generated components feel bespoke, polished, and production-grade.

---

## ⚡ Core Skills Included

The registry provides focused skills that agents can activate on demand:

- **`baseline-ui`**: Enforces strict rules on spacing rhythm, typographic scales, color contrast, and component hierarchy.
- **`create-design-md`**: Automatically generates and maintains a comprehensive `DESIGN.md` in your project root, providing continuous design tokens and stylistic constraints across agent sessions.
- **`fixing-accessibility`**: Audits interactive elements for ARIA landmarks, keyboard navigation, focus indicators, and screen reader compatibility.
- **`fixing-motion-performance`**: Optimizes CSS transitions, Framer Motion springs, and ensures GPU acceleration (`transform`, `opacity`) without layout thrashing.
- **`fixing-metadata`**: Standardizes OpenGraph tags, semantic document structure, viewport settings, and SEO meta tags.

---

## 📦 Installation & Setup

### CLI Usage

Explore, browse, and download individual skills directly from your terminal:

```bash
# Launch interactive skill browser
npx ui-skills start

# List all available skill categories (motion, typography, layout, a11y)
npx ui-skills categories

# List skills in a specific category
npx ui-skills list --category motion

# Fetch and install a specific skill into your current repository
npx ui-skills get baseline-ui
```

### Direct Agent Skill Addition

Using the universal `skills` manager:

```bash
npx skills add ibelick/ui-skills
```

### Model Context Protocol (MCP) Integration

Connect your coding assistant directly to the UI Skills registry via MCP:

```json
{
  "mcpServers": {
    "ui-skills": {
      "command": "npx",
      "args": ["-y", "ui-skills", "mcp"]
    }
  }
}
```

---

## 🛠️ Typical Agent Prompt Workflows

Once installed, your agent can leverage the skills during development:

```text
# Establishing Design Foundations
"Run create-design-md to document our current design system, color palette, and component patterns."

# Polishing Components
"Apply the baseline-ui skill to refactor the navigation bar and hero section with consistent spacing and typography."

# Animation & Motion Polish
"Use fixing-motion-performance to refine our modal entrance animations and prevent layout reflow."

# Accessibility Pass
"Audit this form using fixing-accessibility to guarantee full keyboard and screen-reader compliance."
```

---

## 🔗 Official Links

- **GitHub Repository**: [ibelick/ui-skills](https://github.com/ibelick/ui-skills)
- **Official Website & Catalog**: [ui-skills.com](https://www.ui-skills.com)
