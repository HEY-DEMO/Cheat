# Penpot

> **Category**: `tools/free` · **Last Updated**: `2026-09-21` · **Difficulty**: `Intermediate`

---

## TL;DR

Penpot is the leading open-source design and prototyping platform built on native web standards (SVG, CSS Grid, Flexbox), offering full self-hosting and zero vendor lock-in.

---

## 📋 Overview

- **What**: A browser-based and self-hostable UI/UX design tool that natively speaks the language of web developers (CSS layout models, design tokens, and SVGs).
- **Why**: Proprietary design tools (like Figma) enforce per-seat subscription models and proprietary auto-layout abstractions that require complex translation during developer handoff.
- **When**: Cross-functional product teams building scalable design systems, organizations with on-premise security requirements, and teams integrating AI workflows via MCP servers.

---

## 🔑 Key Concepts

| Concept | Description |
|---|---|
| **Web Standards First** | Native SVG canvas format; shapes, colors, and typography map directly to standard CSS properties. |
| **CSS Grid & Flexbox Layouts** | Autolayout matches CSS flexbox and grid specifications rather than proprietary design heuristics. |
| **Design Tokens** | Integrated design tokens serve as a single source of truth between UI designers and codebases. |
| **Penpot MCP Server** | Model Context Protocol integration enabling AI coding agents to inspect, query, and modify design assets. |
| **Self-Hostable** | Free community edition deployable via Docker with complete data sovereignty. |

---

## 💰 Pricing & Editions Breakdown

| Tier | Price | Ideal For | Highlights |
|---|---|---|---|
| **Professional (Free)** | **$0** / user / mo | Individuals & small teams | Full design suite, up to 8 members, 10 GB storage, 7-day version history. |
| **Unlimited** | **$7** / editor / mo *(Capped at $175/mo)* | Growing teams & studios | Unlimited team size, 25 GB storage, 30-day version history. |
| **Enterprise** | **$25** / member / mo | Scaled organizations | SAML SSO, SCIM provisioning, audit logs, team governance, unlimited storage. |
| **Self-Hosted Community**| **$0 (MPL-2.0)** | Self-managed infrastructure | 100% open source, run in your own VPC/Docker with unlimited users. |

---

## 💻 Self-Hosting with Docker Compose

Deploy a private Penpot instance on a Linux server:

```bash
# 1. Download official configuration files
wget https://raw.githubusercontent.com/penpot/penpot/main/docker/images/docker-compose.yaml
wget https://raw.githubusercontent.com/penpot/penpot/main/docker/images/config.env

# 2. Start the services (PostgreSQL, Redis, Backend, Frontend)
docker compose -p penpot -f docker-compose.yaml up -d
```

Access the web interface at `http://localhost:9001`.

---

## ⚠️ Anti-Patterns

| ❌ Anti-Pattern | ✅ Better Approach |
|---|---|
| Hand-drawing responsive layouts using absolute coordinates | Use Penpot's native CSS Flexbox and Grid containers to make interfaces responsive by design. |
| Exporting PNGs for developer handoff | Direct developers to Penpot's built-in Code Inspector and direct SVG/CSS export. |
| Storing design values as hardcoded hex codes | Use native Penpot Design Tokens for colors, spacing, and typography. |

---

## 🌍 Real-World Use Case

**Scenario**: An enterprise engineering team needs to adhere to European data residency requirements and cannot host UI mockups on US-based commercial cloud design tools.

**Solution**: The team deploys self-hosted Penpot behind their private VPN using Docker, configuring SSO and PostgreSQL storage on their own cluster.

**Result**: Designers and frontend engineers collaborate in real time with 100% data residency compliance, eliminating external SaaS subscription fees.

---

## 🔗 Related Topics

- [Excalidraw](./excalidraw.md) — Sketch-style collaborative whiteboard.
- [Penpot Repository Documentation](../../github_repos/media-productivity/penpot.md) — Full upstream GitHub repository.

---

## 📚 References

- [Penpot Official Site](https://penpot.app)
- [Penpot Documentation](https://help.penpot.app)
- [Penpot Pricing Guide](https://penpot.app/pricing)
- [GitHub Repository](https://github.com/penpot/penpot)

---

*← Back to [Free Tools](./README.md) · [Root Index](../../README.md)*
