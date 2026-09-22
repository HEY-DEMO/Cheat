# Fish Audio (Fish Speech)

> **Category**: `tools/free` · **Last Updated**: `2026-09-21` · **Difficulty**: `Advanced`

---

## TL;DR

Fish Speech is an open-source, multilingual text-to-speech and zero-shot voice cloning engine developed by Fish Audio. It uses a Dual-Autoregressive architecture supporting 80+ languages and natural emotion control.

---

## 📋 Overview

- **What**: An open-source speech generation model capable of cloning any voice from a short 10–30 second reference audio sample without fine-tuning.
- **Why**: Traditional voice cloning pipelines require hours of clean training audio, multi-GPU fine-tuning runs, and complex phoneme preprocessing. Fish Speech treats audio tokens as a language modeling problem, delivering zero-shot cloning with human prosody.
- **When**: Voiceover generation for video productions, multilingual dubbing, interactive conversational agents, audiobook production, and customized voice assistant avatars.

---

## 🔑 Key Concepts

| Concept | Description |
|---|---|
| **Zero-Shot Voice Cloning** | Clone any speaker's voice timbre and cadence using only 10 to 30 seconds of clean reference audio. |
| **Dual-Autoregressive (Dual-AR)** | Two-stage architecture: Slow AR (4B parameters) handles semantic/linguistic structure; Fast AR (400M parameters) handles acoustic detail. |
| **80+ Languages Out-of-the-Box** | Supports English, Chinese, Japanese, Korean, Spanish, French, German, and more without language-specific phoneme pipelines. |
| **Emotion & Prosody Tags** | Control vocal mood directly via inline prompt tags (e.g., `[whisper]`, `[excited]`, `[laughing]`). |
| **SGLang Acceleration** | Production-ready inference engine achieving sub-100ms Time-to-First-Audio (TTFA) and 3,000+ audio tokens/sec. |

---

## 💻 Python Quickstart

### CLI Inference

```bash
# Clone a voice from a reference audio clip
python -m tools.llama.generate \
    --text "Welcome to Fish Audio. This voice was cloned using only 15 seconds of audio." \
    --prompt-text "Sample speaker reference transcript." \
    --prompt-tokens "reference_sample.wav" \
    --output "cloned_output.wav"
```

### Emotion Control Example

```python
# Natural prosody and emotion tags can be injected directly into text
prompt = "[excited] I have incredible news to share with the team today! [whisper] Don't tell anyone yet."
```

---

## ⚠️ Anti-Patterns

| ❌ Anti-Pattern | ✅ Better Approach |
|---|---|
| Using noisy, reverberant background audio as reference samples | Provide dry, clean, isolated vocal clips (10–30s) recorded with minimal background noise. |
| Re-encoding existing phoneme dictionaries | Feed raw text directly; Fish Speech uses byte/token-level representations across all 80+ languages. |

---

## 🌍 Real-World Use Case

**Scenario**: A global media company needs to dub an English documentary into Spanish, Japanese, and French while preserving the original narrator's unique vocal identity and timbre.

**Solution**: The team isolates 20 seconds of clean English narration, translating the transcript into target languages and running inference through Fish Speech.

**Result**: High-fidelity, localized audio tracks generated with the exact vocal characteristics of the original narrator across all languages.

---

## 🔗 Related Topics

- [Fish Speech Repository Documentation](../../github_repos/fish-speech.md) — Upstream GitHub repository.
- [Kokoro TTS](./kokoro-tts.md) — Ultra-lightweight (82M) open-source TTS.

---

## 📚 References

- [GitHub Repository](https://github.com/fishaudio/fish-speech)
- [Hugging Face Model Hub](https://huggingface.co/fishaudio)
- [Fish Audio Official Website](https://fish.audio)

---

*← Back to [Free Tools](./README.md) · [Root Index](../../README.md)*
