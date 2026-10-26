> 🔗 **GitHub Repository**: [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill)

---

# ⏱️ Last30Days Skill

> **Real-time research engine and community intelligence skill for AI agents.** Created by Michael Van Horn to bypass outdated model training cutoffs by scanning public discussions, code commits, and news from the past 30 days across Reddit, Hacker News, Polymarket, X, and YouTube with human-engagement filtering.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![GitHub Stars](https://img.shields.io/github/stars/mvanhorn/last30days-skill?style=social)](https://github.com/mvanhorn/last30days-skill)
[![Platform: Multi-Agent](https://img.shields.io/badge/Platform-Claude_Code_|_Cursor_|_Codex-blueviolet.svg)](#-installation--setup)
[![Upstream Repository](https://img.shields.io/badge/upstream-mvanhorn%2Flast30days--skill-teal.svg)](https://github.com/mvanhorn/last30days-skill)

---

## 🚀 Overview

Standard web searches and LLM retrieval often deliver stale documentation, SEO-manipulated blog posts, or outdated training data. When investigating newly released libraries, zero-day security advisories, or fast-moving framework updates, developers need what engineers are discussing *right now*.

**Last30Days Skill** (`/last30days`) queries multi-platform discussion boards and prediction markets in parallel. Rather than ranking by page rank or keyword density, it weights findings by verified human engagement (upvotes, comment density, and prediction market consensus) to generate citation-rich research summaries.

---

## ⚡ Core Capabilities

- **Zero-Config Data Sources**:
  - **Reddit**: Searches relevant subreddits, analyzing top-ranked posts and community comments.
  - **Hacker News**: Ingests algorithmic trends, Ask HN, and technical discussions via the Algolia HN API.
  - **Polymarket**: Surfaces live prediction market odds on political, technological, and economic outcomes.
  - **GitHub**: Scans recent repository releases, trending repos, and commit activity.
- **Optional Extended Sources**:
  - **X (Twitter)**: Real-time developer commentary and engineering threads.
  - **YouTube Transcripts**: Extracts and summarizes technical talks and video transcripts using `yt-dlp`.
  - **arXiv & Techmeme**: Gathers cutting-edge preprints and tech news aggregations.
- **Engagement-Scored Synthesis**: Discards AI content farms and low-signal noise by filtering for genuine community validation.
- **Strict Citation Backing**: Emits markdown reports with direct links to sources, comment threads, and timestamps.

---

## 📦 Installation & Setup

### Claude Code Plugin Marketplace

```bash
# Add repository source
/plugin marketplace add mvanhorn/last30days-skill

# Install the skill
/plugin install last30days
```

### Universal Skills CLI (Cursor, Codex, Gemini CLI, Windsurf)

```bash
# Install globally for all detected AI agents
npx skills add mvanhorn/last30days-skill -g

# Or install locally in current repository
npx skills add mvanhorn/last30days-skill
```

---

## 🛠️ Typical Agent Usage Prompts

```text
# Researching new framework breaking changes
"/last30days What are the biggest complaints and migration issues developers are facing with Next.js 15?"

# Checking library reliability
"/last30days Has anyone successfully deployed DeepSeek R1 locally on Apple Silicon M3 Max?"

# Tracking recent vulnerability exploits
"/last30days What is the current status and mitigation for the latest OpenSSH vulnerability?"

# Gauging tech sentiment
"/last30days What are engineers saying about Bun vs Node.js in production over the last month?"
```

---

## 🔗 Official Links

- **GitHub Repository**: [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill)

---

*← Back to [AI Agents & Skills](./README.md) · [GitHub Repos Hub](../README.md) · [Root Index](../../README.md)*
