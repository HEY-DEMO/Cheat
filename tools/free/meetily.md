# Meetily

> **Category**: `tools/free` · **Last Updated**: `2026-09-21` · **Difficulty**: `Beginner`

---

## TL;DR

Meetily is a 100% local, open-source AI meeting assistant that records, transcribes, and summarizes meetings directly on your computer without inviting third-party bots into calls.

---

## 📋 Overview

- **What**: An offline desktop app built with Rust, Tauri, and Next.js that captures system and microphone audio to produce live transcripts, action items, and executive summaries.
- **Why**: Cloud meeting tools (Otter.ai, Fireflies, Read.ai) require meeting bots to join calls, causing awkwardness for clients, privacy concerns, and security compliance violations.
- **When**: Confidential customer interviews, internal architectural reviews, medical/legal client calls, and daily developer standups on Zoom, Google Meet, Teams, or Slack Huddles.

---

## 🔑 Key Concepts

| Concept | Description |
|---|---|
| **Zero Bot Infiltration** | Captures audio directly from your OS audio output and input devices; no external bot ever joins your calls. |
| **Local Transcription** | Transcribes spoken dialogue locally using Whisper or NVIDIA Parakeet models. |
| **Local LLM Summaries** | Integrates seamlessly with Ollama, LM Studio, or local models to generate action items and meeting minutes. |
| **Speaker Identification** | Distinguishes between your local microphone and remote conference participants via dual-channel audio separation. |
| **Markdown Export** | Exports structured meeting notes, agendas, decisions, and transcripts to Markdown files or Obsidian. |

---

## ⚙️ Architecture & Local Stack

```
[ Your Microphone ] ──┐
                      ├─► [ Meetily Audio Engine ] ──► [ Local Whisper / Parakeet ]
[ System / Call Audio ]─┘           (Rust/Tauri)                     │
                                                                     ▼
                                                             [ Raw Transcript ]
                                                                     │
[ Obsidian / Markdown ] ◄── [ Structured Summary ] ◄── [ Local LLM (Ollama) ]
```

---

## ⚠️ Anti-Patterns

| ❌ Anti-Pattern | ✅ Better Approach |
|---|---|
| Allowing third-party cloud bots to record client NDA calls | Use Meetily for internal-only loopback recording with zero notification or bot presence. |
| Storing sensitive corporate executive discussions in unmanaged SaaS clouds | Run Meetily with a local Ollama model (e.g., Llama 3 or Mistral) for 100% on-premise governance. |

---

## 🌍 Real-World Use Case

**Scenario**: A venture capital firm conducts technical due diligence calls with early-stage founders sharing proprietary codebases and trade secrets under strict non-disclosure agreements.

**Solution**: Partners run Meetily locally on their macOS and Windows laptops during Zoom calls.

**Result**: Automated executive summaries and action items generated within 30 seconds after the call ends, stored strictly on encrypted local NVMe drives.

---

## 🔗 Related Topics

- [Meetily Repository Documentation](../../github_repos/media-productivity/meetily.md) — Upstream GitHub repository.
- [Handy](./handy.md) — Global speech-to-text dictation.
- [Open Notebook](./open-notebook.md) — Local AI research and document synthesis.

---

## 📚 References

- [Meetily Official Site](https://meetily.ai)
- [GitHub Repository](https://github.com/Zackriya-Solutions/meetily)

---

*← Back to [Free Tools](./README.md) · [Root Index](../../README.md)*
