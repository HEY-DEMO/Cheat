# Cap

> **Category**: `tools/free` · **Last Updated**: `2026-09-21` · **Difficulty**: `Beginner`

---

## TL;DR

Cap is an open-source, lightweight alternative to Loom for recording and sharing beautiful screen captures with complete data ownership.

---

## 📋 Overview

- **What**: A desktop screen recorder built with Tauri, Rust, and Next.js that lets users record their screen, camera, and audio, and instantly share or store recordings locally.
- **Why**: Traditional recording tools lock recordings behind monthly limits, watermark video exports, or store sensitive business discussions on third-party servers.
- **When**: Async standups, bug reproduction recordings for GitHub issues, product walkthroughs, and internal engineering documentation.

---

## 🔑 Key Concepts

| Concept | Description |
|---|---|
| **Local-First Recording** | Videos can be saved locally on your device without uploading to any cloud server. |
| **Instant Shareable Links** | Option to sync with Cap Cloud or your own custom S3/Cloudflare R2 bucket. |
| **Tauri + Rust Core** | Minimal resource consumption and fast startup time compared to heavy Electron apps. |
| **Self-Hostable** | Host your own Cap web sharing and storage service. |

---

## ⌨️ Common Controls & Shortcuts

| Action | Shortcut |
|---|---|
| **Start / Stop Recording** | `Cmd+Shift+R` (macOS) / `Ctrl+Shift+R` (Windows) |
| **Pause / Resume** | `Cmd+Shift+P` (macOS) / `Ctrl+Shift+P` (Windows) |
| **Toggle Camera Bubble** | `Cmd+Shift+C` (macOS) / `Ctrl+Shift+C` (Windows) |

---

## ⚠️ Anti-Patterns

| ❌ Anti-Pattern | ✅ Better Approach |
|---|---|
| Uploading customer data or confidential API keys in unlisted public Loom links | Record with Cap locally or host recordings on private S3 buckets with restricted IAM roles. |
| Writing multi-paragraph text explanations for subtle frontend animation bugs | Record a 15-second Cap video demonstrating the exact reproduction flow. |

---

## 🌍 Real-World Use Case

**Scenario**: A distributed engineering team needs to communicate asynchronous bug reports and feature demos without incurring per-seat SaaS costs or leaking customer telemetry.

**Solution**: The team standardizes on Cap, connecting it to an enterprise Cloudflare R2 bucket for zero-egress cost video hosting.

**Result**: Engineers record and share high-resolution product walkthroughs instantly while maintaining total custody of their video files.

---

## 🔗 Related Topics

- [Cap Repository Documentation](../../github_repos/cap.md) — Full upstream GitHub repository and architecture.
- [Upscayl](./upscayl.md) — Open-source AI image upscaler.

---

## 📚 References

- [Cap Official Website](https://cap.so)
- [Cap Documentation](https://cap.so/docs)
- [GitHub Repository](https://github.com/CapSoftware/Cap)

---

*← Back to [Free Tools](./README.md) · [Root Index](../../README.md)*
