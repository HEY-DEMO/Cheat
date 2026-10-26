> 🔗 **GitHub Repository**: [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design)

---

# 📊 Diagram Design

> **Editorial-quality technical and business diagrams for AI coding agents.** Built by Cathryn Lavery to eliminate generic "Mermaid slop" by generating self-contained, publication-ready HTML + SVG diagrams with custom typography, brand palette extraction, and modern layout aesthetics.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![GitHub Stars](https://img.shields.io/github/stars/cathrynlavery/diagram-design?style=social)](https://github.com/cathrynlavery/diagram-design)
[![Website](https://img.shields.io/badge/website-diagramdesign.dev-purple)](https://diagramdesign.dev)
[![Upstream Repository](https://img.shields.io/badge/upstream-cathrynlavery%2Fdiagram--design-indigo.svg)](https://github.com/cathrynlavery/diagram-design)

---

## 🚀 Overview

Standard automated diagramming utilities like default Mermaid, Graphviz, or PlantUML produce mechanical, heavily bordered, or pastel-colored charts that lack visual hierarchy and polish.

**Diagram Design** is an agent skill that enables AI coding assistants (Claude Code, Cursor, Codex, Windsurf, Copilot, Gemini CLI) to output publication-grade technical and business diagrams. It emits portable, single-file HTML + SVG artifacts that look professionally handcrafted for pitch decks, architectural RFCs, documentation, and executive presentations.

---

## ⚡ Core Features

- **No Mermaid Slop**: Replaces low-contrast lines and boxy flowcharts with balanced typographic hierarchy, refined padding, and modern colorways.
- **Single-File Self-Contained Deliverables**: Every generated diagram is an independent `.html` file with embedded inline SVG that opens immediately in any browser with zero build steps.
- **Brand Palette Ingestion**: Can inspect an existing product website or brand guideline URL to extract color codes and typography, ensuring generated diagrams match corporate identity.
- **Rich Diagram Topologies**:
  - System architecture maps & cloud topologies
  - Microservice event flows & sequence flows
  - 2x2 Impact-Effort & prioritization quadrants
  - User journey maps & funnel flows
  - Multi-tier dependency trees and tech stacks
- **Import Compatibility**: Easily converts and upgrades existing Mermaid, draw.io, or Excalidraw definitions into editorial-grade presentations.

---

## 📦 Installation & Setup

### Via the Universal Skills CLI

```bash
# Add globally to all detected AI coding agents
npx skills add cathrynlavery/diagram-design -g

# Or add locally to the current workspace
npx skills add cathrynlavery/diagram-design
```

### Manual Configuration

- **Claude Code**:
  ```bash
  mkdir -p ~/.claude/skills/diagram-design
  git clone https://github.com/cathrynlavery/diagram-design.git ~/.claude/skills/diagram-design
  ```

- **Cursor**:
  Place the rules file into `.cursor/rules/diagram-design.mdc`.

- **Codex / Gemini CLI**:
  Add the skill folder to your agent configuration directory under `skills/diagram-design`.

---

## 🛠️ Example Agent Prompts

```text
# Architecture diagram with brand styling
"Create a system architecture diagram for an event-driven payment processing pipeline. Extract the color palette from https://stripe.com and save it as an HTML/SVG diagram."

# Upgrading existing Mermaid code
"Take this Mermaid sequence diagram and redesign it using diagram-design into an editorial presentation diagram."

# Business prioritization quadrant
"Generate a 2x2 Impact vs. Effort matrix diagram comparing Q3 engineering roadmap initiatives."
```

---

## 🔗 Official Links

- **GitHub Repository**: [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design)
- **Official Documentation & Gallery**: [diagramdesign.dev](https://diagramdesign.dev)

---

*← Back to [AI Agents & Skills](./README.md) · [GitHub Repos Hub](../README.md) · [Root Index](../../README.md)*
