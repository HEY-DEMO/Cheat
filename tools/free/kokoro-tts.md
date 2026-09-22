# Kokoro TTS

> **Category**: `tools/free` · **Last Updated**: `2026-09-21` · **Difficulty**: `Intermediate`

---

## TL;DR

Kokoro-82M is an ultra-lightweight, open-weight text-to-speech (TTS) model with only 82 million parameters that achieves audio fidelity comparable to models 10x–100x its size, running smoothly on CPUs, GPUs, and WebGPU.

---

## 📋 Overview

- **What**: An open-source speech synthesis model created by Hexgrad, combining StyleTTS 2 and ISTFTNet under the permissive Apache-2.0 license.
- **Why**: Traditional high-quality neural TTS models (e.g., Tortoise, XTTS) require heavy VRAM footprints, high inference latencies, and costly GPUs. Kokoro delivers state-of-the-art voice naturalness on commodity consumer hardware and in-browser WebAssembly/WebGPU.
- **When**: On-device voice assistants, podcast narration, accessibility screen readers, video game dialogue, and interactive voice agents.

---

## 🔑 Key Concepts

| Concept | Description |
|---|---|
| **82M Architecture** | Compact parameter footprint enabling near-instant cold starts and sub-second generation times. |
| **StyleTTS 2 + ISTFTNet** | Hybrid neural vocoder and style diffusion architecture for expressive, human-like cadence. |
| **Apache 2.0 License** | 100% free for both personal and commercial production deployments. |
| **Client-Side WebGPU** | Runs directly in web browsers via `transformers.js` without any backend audio streaming servers. |
| **Multilingual Voices** | Built-in high-quality voice profiles for American English, British English, Spanish, French, Hindi, Japanese, and Mandarin. |

---

## 💻 Python Quickstart

### 1. Installation

```bash
pip install kokoro soundfile
```

### 2. Generate Audio

```python
from kokoro import KPipeline
import soundfile as sf

# Initialize English pipeline (uses CPU or CUDA automatically)
pipeline = KPipeline(lang_code='a') # 'a' for American English, 'b' for British

text = "Hello! Kokoro is a lightweight, open-weight text to speech model running locally."

# Generate audio chunks
generator = pipeline(text, voice='af_heart', speed=1.0)

for i, (gs, ps, audio) in enumerate(generator):
    sf.write(f'output_{i}.wav', audio, 24000)
    print(f"Saved audio segment {i}")
```

---

## ⚠️ Anti-Patterns

| ❌ Anti-Pattern | ✅ Better Approach |
|---|---|
| Renting expensive A100 GPU clusters for standard TTS | Run Kokoro on standard CPUs, local consumer GPUs, or edge devices; 82M parameters is extremely lightweight. |
| Streaming audio over unreliable mobile connections | Compile Kokoro via ONNX / WebGPU to synthesize voice directly on the client's browser. |
| Ignoring phonetic pronunciation tags | Use IPA phoneme dictionaries or phoneme input when domain-specific jargon or uncommon names mispronounce. |

---

## 🌍 Real-World Use Case

**Scenario**: A mobile educational reading app needs to read textbook excerpts aloud to students without incurring per-character cloud API charges from ElevenLabs or Azure.

**Solution**: The engineering team bundles Kokoro-82M in an ONNX runtime directly into their offline desktop and mobile client apps.

**Result**: Zero recurring API bills, total offline student privacy, and sub-100ms time-to-first-audio latency.

---

## 🔗 Related Topics

- [Kokoro Repository Documentation](../../github_repos/media-productivity/kokoro.md) — Upstream GitHub repository.
- [Fish Audio](./fish-audio.md) — Zero-shot voice cloning and multilingual TTS.

---

## 📚 References

- [Hugging Face Model Card](https://huggingface.co/hexgrad/Kokoro-82M)
- [GitHub Repository](https://github.com/hexgrad/kokoro)

---

*← Back to [Free Tools](./README.md) · [Root Index](../../README.md)*
