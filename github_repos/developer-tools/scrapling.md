> 🔗 **GitHub Repository**: [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling)

---

# 🕷️ Scrapling

> **Undetectable, adaptive web scraping and crawler library for Python.** Built by Karim 'D4Vinci' Shoair with automated anti-bot protection bypass, stealth headless browser integration, and intelligent self-healing selectors that survive website redesigns.

[![License: BSD-3-Clause](https://img.shields.io/badge/License-BSD--3--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)
[![GitHub Stars](https://img.shields.io/github/stars/D4Vinci/Scrapling?style=social)](https://github.com/D4Vinci/Scrapling)
[![PyPI version](https://img.shields.io/pypi/v/scrapling.svg?color=orange)](https://pypi.org/project/scrapling/)
[![Python: 3.9+](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Upstream Repository](https://img.shields.io/badge/upstream-D4Vinci%2FScrapling-green.svg)](https://github.com/D4Vinci/Scrapling)

---

## 🚀 Overview

Traditional web scraping scripts break constantly when web developers rename CSS classes, alter DOM hierarchies, or deploy anti-bot systems like Cloudflare Turnstile, Datadome, or Kasada. Developers end up spending hours debugging broken selectors and blocked HTTP requests.

**Scrapling** is an all-in-one scraping engine engineered for resilience:
- **Self-Healing Selectors**: If a CSS class or ID changes, Scrapling's adaptive parser uses structural heuristics and similarity algorithms to relocate target elements automatically.
- **Stealth Architecture**: Built-in evasive browser fingerprinting (integrating Playwright and Camoufox) to bypass modern bot-detection checkpoints.
- **High Performance**: Extremely fast HTTP response parsing combined with asynchronous parallel execution pipelines.

---

## ⚡ Key Features

| Feature | Description |
|---|---|
| **Adaptive Selectors** | Learns element characteristics on the first run; automatically adapts if classes or paths change. |
| **Stealth Fetchers** | Bypasses Cloudflare, PerimeterX, and Datadome challenges transparently. |
| **Hybrid Modes** | Fast HTTP requests for static endpoints; automatic fallback to stealth browser for dynamic SPAs. |
| **Unified Parser** | Supports CSS selectors, XPath expressions, regex extraction, and text queries with a clean API. |
| **Async Concurrency** | Fully asynchronous crawler capabilities for multi-thousand page harvesting jobs. |

---

## 📦 Installation & Setup

```bash
# Install core package
pip install scrapling

# Install browser automation dependencies (Playwright / Camoufox)
scrapling install
```

---

## 💻 Code Examples

### 1. Basic Fast Scraping

```python
from scrapling import Fetcher

fetcher = Fetcher()
page = fetcher.get("https://quotes.toscrape.com")

# Extract using CSS selectors
quotes = page.css(".quote span.text::text")
authors = page.css(".quote small.author::text")

for quote, author in zip(quotes, authors):
    print(f'"{quote}" — {author}')
```

### 2. Stealth Scraping (Bypassing Anti-Bot Walls)

```python
from scrapling import StealthyFetcher

# StealthyFetcher mimics real user browser fingerprints and solves challenge gates
stealth_fetcher = StealthyFetcher()
page = stealth_fetcher.get("https://example-protected-site.com")

title = page.css("h1::text").first
print("Protected Page Title:", title)
```

### 3. Self-Healing Adaptive Selectors

```python
from scrapling import Adaptor

# When elements shift their classes or attributes, adapt automatically
adaptor = Adaptor(page)
price = adaptor.find("price-tag", auto_match=True)
print("Extracted price:", price.text)
```

---

## ⚠️ Anti-Patterns vs. Best Practices

| ❌ Fragile Approach | ✅ Scrapling Best Practice |
|---|---|
| Rigid, deeply nested selectors like `div > div:nth-child(3) > p.text-gray-500` | Use semantic, adaptive selectors with fallback text patterns. |
| Hardcoded, plain `requests` headers easily blocked by Cloudflare | Use `StealthyFetcher` with randomized browser signatures and fingerprint rotation. |
| Launching full heavy browsers for simple HTML payloads | Use lightweight `Fetcher` first; escalate to `StealthyFetcher` only when client-side JS or bot gates are detected. |

---

## 🔗 Official Links

- **GitHub Repository**: [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling)
- **PyPI Package**: [pypi.org/project/scrapling](https://pypi.org/project/scrapling/)

---

*← Back to [Developer Tools](./README.md) · [GitHub Repos Hub](../README.md) · [Root Index](../../README.md)*
