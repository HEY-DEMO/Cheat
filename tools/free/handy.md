# Handy

> **Category**: `tools/free` · **Last Updated**: `2026-09-21` · **Difficulty**: `Beginner`

---

## TL;DR

Handy is an open-source, privacy-first, offline speech-to-text (STT) dictation app for Windows, macOS, and Linux. It transcribes spoken voice locally using Whisper and NVIDIA Parakeet, pasting text directly into active applications with a global hotkey.

---

## 📋 Overview

- **What**: A cross-platform desktop dictation tool built with Tauri, Rust, and local neural speech models.
- **Why**: Cloud voice dictation services capture audio buffers and send private conversations or proprietary code dictation to remote servers. Handy runs 100% locally with zero internet dependency.
- **When**: Hands-free coding, composing long emails, writing documentation, drafting PR descriptions, and accessibility workflows.

---

## 🔑 Key Concepts

| Concept | Description |
|---|---|
| **Global Push-to-Talk** | Hold or toggle a configurable keyboard shortcut anywhere in your OS to dictate. |
| **Direct Active Window Injection**| Automatically simulates keyboard paste into whatever application currently has cursor focus. |
| **Local Whisper & Parakeet** | Choose from OpenAI Whisper models (tiny, base, small, medium) or NVIDIA Parakeet V3 for speed. |
| **Silero VAD** | Voice Activity Detection automatically filters out background room noise and typing clicks. |
| **Tauri + Rust Backend** | Lightweight memory usage and fast startup compared to resource-heavy Electron apps. |

---

## ⌨️ How It Works

1. **Activate**: Press and hold `Ctrl+Space` (or your chosen hotkey).
2. **Speak**: Dictate code, commit messages, or notes naturally.
3. **Release**: Release the key; Handy transcribes speech via local neural weights and immediately inserts text at your cursor.

---

## ⚙️ Configuration & Model Selection

| Model | Size | Speed | Ideal For |
|---|---|---|---|
| **Whisper Tiny** | ~75 MB | Ultra Fast | Low-spec laptops, basic commands, rapid typing. |
| **Whisper Base** | ~140 MB | Fast | Everyday English dictation and general notes. |
| **Whisper Small** | ~460 MB | Medium | Technical terminology, accented English, high accuracy. |
| **Parakeet V3** | Varies | Near Instant | High-throughput English transcription on modern hardware. |

---

## ⚠️ Anti-Patterns

| ❌ Anti-Pattern | ✅ Better Approach |
|---|---|
| Using cloud OS dictation on confidential codebases | Use Handy for air-gapped transcription where microphone audio never leaves RAM. |
| Running heavy models without GPU acceleration | Use Whisper Base or Parakeet on CPU-only machines to maintain real-time responsiveness. |

---

## 🌍 Real-World Use Case

**Scenario**: A software engineer experiencing repetitive strain injury (RSI) needs to write code documentation, Jira tickets, and GitHub pull request reviews without typing every word manually.

**Solution**: The developer configures Handy with a global shortcut mapped to a mouse button, running Whisper Small locally.

**Result**: 150+ WPM voice typing directly into VS Code and browser inputs with zero cloud egress and 98%+ technical accuracy.

---

## 🔗 Related Topics

- [Handy Repository Documentation](../../github_repos/media-productivity/handy.md) — Upstream GitHub repository and build guides.
- [Meetily](./meetily.md) — Local meeting transcription and minutes summarization.

---

## 📚 References

- [Handy Official Website](https://handy.computer)
- [GitHub Repository](https://github.com/cjpais/Handy)

---

*← Back to [Free Tools](./README.md) · [Root Index](../../README.md)*
