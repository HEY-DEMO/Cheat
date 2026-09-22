# Upscayl

> **Category**: `tools/free` · **Last Updated**: `2026-09-21` · **Difficulty**: `Beginner`

---

## TL;DR

Upscayl is a free, open-source AI image upscaler that enhances and enlarges low-resolution images using deep learning models powered by the Vulkan NCNN engine.

---

## 📋 Overview

- **What**: A desktop AI upscaling application and CLI tool that sharpens and enlarges images up to 4x (or more with double-upscale) without cloud uploads.
- **Why**: Traditional bicubic or bilinear interpolation leaves scaled-up images blurry and pixelated. Upscayl uses neural super-resolution models to realistically reconstruct missing high-frequency details.
- **When**: Upscaling low-resolution assets for modern 4K/retina displays, enhancing legacy photographs, sharpening AI-generated art, and preparing assets for print or web design.

---

## 🔑 Key Concepts & Model Selection

| Model | Best Used For | Notes |
|---|---|---|
| **Upscayl General** | General-purpose images, photos, and digital art | Balanced default for most standard images. |
| **High Fidelity (HFA2k)** | High-detail portraits, nature, and complex textures | Minimizes hallucinated artifacts while sharpening edges. |
| **Remacri** | Restoring older scans and degraded photographs | Smooths compression artifacts and reconstructs fine lines. |
| **UltraSharp** | Ultra-crisp architectural and graphic assets | Aggressive sharpening for textures, text, and hard contours. |
| **Digital Art** | Anime, 2D illustrations, cartoons, icons | Preserves solid color fills and cleans up color bleed. |

---

## 💻 CLI & Batch Processing (`upscayl-ncnn`)

Upscayl also offers a headless CLI tool ([`upscayl-ncnn`](https://github.com/upscayl/upscayl-ncnn)) for batch operations:

```bash
# Upscale an image 4x using the default model
upscayl-ncnn -i input.png -o output.png -m models/ -n remacri

# Batch process an entire directory
upscayl-ncnn -i ./raw-images -o ./upscaled-images -m models/ -n ultrasharp -s 4
```

---

## ⚙️ System Requirements

> [!IMPORTANT]
> Upscayl requires a **Vulkan-compatible GPU** (NVIDIA, AMD, Apple Silicon, or modern Intel Iris Xe / Arc). Most older integrated GPUs (iGPUs) are not supported.

---

## ⚠️ Anti-Patterns

| ❌ Anti-Pattern | ✅ Better Approach |
|---|---|
| Expecting Upscayl to fix motion-blurred or totally out-of-focus photos | Upscayl reconstructs resolution and pixelated edges; it cannot recover severely blurred focus. |
| Canceling batch upscale mid-flight | Let batch processing finish; post-processing passes happen after all images complete upscaling. |
| Running heavy 4x models on low-power battery | Plug into AC power; Vulkan GPU inference requires sustained GPU clock performance. |

---

## 🌍 Real-World Use Case

**Scenario**: A frontend team is redesigning a corporate marketing site for 4K monitors, but the archive of product screenshots and logos contains only 300x200 pixel images from 2012.

**Solution**: The team runs the assets through Upscayl using the **Digital Art** and **Remacri** models with 4x scaling.

**Result**: Pristine, crisp 1200x800 high-resolution assets generated locally in seconds without any cloud subscription fees.

---

## 🔗 Related Topics

- [Cap](./cap.md) — Open-source screen recording tool.
- [Upscayl Repository Documentation](../../github_repos/media-productivity/upscayl.md) — Full upstream GitHub repository and build instructions.

---

## 📚 References

- [Upscayl Official Website](https://upscayl.org)
- [Upscayl Documentation](https://docs.upscayl.org)
- [Custom Models Repository](https://github.com/upscayl/custom-models)
- [GitHub Repository](https://github.com/upscayl/upscayl)

---

*← Back to [Free Tools](./README.md) · [Root Index](../../README.md)*
