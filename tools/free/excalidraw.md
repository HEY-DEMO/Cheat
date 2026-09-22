# Excalidraw

> **Category**: `tools/free` · **Last Updated**: `2026-09-21` · **Difficulty**: `Beginner`

---

## TL;DR

Excalidraw is a free, open-source virtual collaborative whiteboard with a signature hand-drawn aesthetic, infinite canvas, and diagrams-as-code capabilities.

---

## 📋 Overview

- **What**: A sketch-based whiteboard tool powered by Rough.js and React that lets users create architecture diagrams, user flows, wireframes, and mind maps.
- **Why**: Traditional diagramming tools often feel overly rigid or formal. Excalidraw's hand-drawn look encourages rapid prototyping, low-friction collaboration, and immediate communication.
- **When**: System architecture reviews, sprint design jams, quick visual documentation in pull requests, and real-time team brainstorms.

---

## 🔑 Key Concepts

| Concept | Description |
|---|---|
| **Rough.js Aesthetic** | Renders lines and shapes with organic, hand-drawn roughness and stroke jitter. |
| **Infinite Canvas** | Unlimited panning and zooming canvas space. |
| **End-to-End Encryption** | Real-time collaboration rooms are encrypted client-side using WebRTC and temporary symmetric keys. |
| **Diagrams-as-Code** | Native bidirectional support for Mermaid.js syntax and natural-language AI prompt generation. |
| **Metadata in SVG** | Exported `.svg` files contain embedded scene JSON, making them directly re-openable and editable in Excalidraw. |

---

## ⌨️ Essential Keyboard Shortcuts

| Action | Shortcut |
|---|---|
| **Selection Tool** | `V` or `1` |
| **Rectangle** | `R` or `2` |
| **Diamond** | `D` or `3` |
| **Ellipse / Circle** | `O` or `4` |
| **Arrow** | `A` or `5` |
| **Line** | `L` or `6` |
| **Freehand Draw** | `P` or `7` |
| **Text** | `T` or `8` |
| **Eraser** | `E` or `0` |
| **Pan Canvas** | `Space + Drag` or `H` |
| **Group / Ungroup** | `Ctrl+G` / `Ctrl+Shift+G` (`Cmd` on macOS) |
| **Lock Current Tool** | `Q` |

---

## 💻 Developer Usage

### 1. React Component Integration

Embed Excalidraw inside a React application using the official package:

```bash
npm install react react-dom @excalidraw/excalidraw
```

```tsx
import React from "react";
import { Excalidraw } from "@excalidraw/excalidraw";

export function DiagramEditor() {
  return (
    <div style={{ height: "600px", width: "100%" }}>
      <Excalidraw
        initialData={{
          appState: { viewBackgroundColor: "#1e1e1e", theme: "dark" }
        }}
        onChange={(elements, state) => {
          // Handle element state changes
        }}
      />
    </div>
  );
}
```

### 2. Docker Self-Hosting

Run a local or on-premise Excalidraw instance with zero external dependencies:

```bash
docker run -d --name excalidraw -p 8080:80 excalidraw/excalidraw:latest
```

---

## ⚠️ Anti-Patterns

| ❌ Anti-Pattern | ✅ Better Approach |
|---|---|
| Using Excalidraw for precise pixel-level UI mocks | Use tools like Penpot or Figma for hi-fi UI; use Excalidraw for architecture and user journeys. |
| Storing diagrams only as raster PNGs | Export as `.svg` with embedded scene data or `.excalidraw` JSON so diagrams can be modified later. |
| Manually redrawing common cloud components | Install official community libraries (AWS, GCP, Azure, Kubernetes) from the built-in Library tab. |

---

## 🌍 Real-World Use Case

**Scenario**: An engineering team is discussing a database migration from monolith Postgres to an event-driven architecture using Kafka.

**Solution**: During the design meeting, the architect opens an end-to-end encrypted Excalidraw session. The team collaboratively sketches services, topic partitions, and consumer groups in real time.

**Result**: The resulting `.svg` file is embedded directly into the architectural decision record (ADR) and pull request markdown, readable by all and editable anytime.

---

## 🔗 Related Topics

- [Penpot](./penpot.md) — Open-source UI/UX design and prototyping platform.
- [Excalidraw Repository Documentation](../../github_repos/media-productivity/excalidraw.md) — Full upstream GitHub repository and architecture.

---

## 📚 References

- [Excalidraw Official Web App](https://excalidraw.com)
- [Excalidraw Documentation](https://docs.excalidraw.com)
- [GitHub Repository](https://github.com/excalidraw/excalidraw)

---

*← Back to [Free Tools](./README.md) · [Root Index](../../README.md)*
