# Ackee

> **Category**: `tools/free` · **Last Updated**: `2026-09-21` · **Difficulty**: `Intermediate`

---

## TL;DR

Ackee is a free, self-hosted, privacy-focused web analytics platform built on Node.js and MongoDB. It provides clean insights without tracking personal identifiable information (PII) or storing cookies.

---

## 📋 Overview

- **What**: A lightweight, self-hosted analytics server and client tracker providing an open-source alternative to Google Analytics.
- **Why**: Traditional analytics platforms violate user privacy, track individuals across websites with third-party cookies, and complicate GDPR/CCPA compliance. Ackee uses multi-step anonymization to deliver essential traffic data without surveillance.
- **When**: Personal blogs, developer documentation, indie SaaS products, and enterprise applications requiring strictly private, self-hosted traffic analytics.

---

## 🔑 Key Concepts

| Concept | Description |
|---|---|
| **Cookie-Free Tracking** | Generates non-reversible, daily-changing unique visitor hashes; zero cookies placed in the visitor's browser. |
| **Self-Hosted & Own Your Data** | Runs as a Docker container with MongoDB; full database custody with zero third-party data broker sharing. |
| **GraphQL API** | Server exposes a flexible GraphQL endpoint for querying visitor numbers, page views, and referrers. |
| **Lightweight Tracker** | The `tracker.js` script weighs only ~4 KB, minimizing page load impact and eliminating render blocking. |
| **Clean, Modern UI** | Minimalist dashboard showing views, unique visitors, durations, referrers, and operating systems at a glance. |

---

## 💻 Quickstart Deployment (Docker Compose)

```yaml
# docker-compose.yml
services:
  ackee:
    image: electerious/ackee:latest
    ports:
      - "3000:3000"
    environment:
      - WAIT_HOSTS=mongo:27017
      - MONGODB_URI=mongodb://mongo:27017/ackee
      - ACKEE_USERNAME=admin
      - ACKEE_PASSWORD=your_secure_password
    depends_on:
      - mongo

  mongo:
    image: mongo:latest
    volumes:
      - mongo_data:/data/db

volumes:
  mongo_data:
```

### Embed Tracker Script in Website

```html
<script 
  async 
  src="https://analytics.yourdomain.com/tracker.js" 
  data-ackee-server="https://analytics.yourdomain.com" 
  data-ackee-domain-id="your-domain-uuid">
</script>
```

---

## ⚠️ Anti-Patterns

| ❌ Anti-Pattern | ✅ Better Approach |
|---|---|
| Exposing unauthenticated MongoDB ports to the internet | Restrict MongoDB to Docker internal networking (`depends_on`); expose only port 3000 behind a reverse proxy (e.g., Caddy or Nginx with SSL). |
| Expecting deep user behavioral funnels and cross-session tracking | Use Ackee for aggregate page views, referrers, and durations; it intentionally does not track individual user identity. |

---

## 🌍 Real-World Use Case

**Scenario**: An open-source developer wants to monitor traffic, top referring sites, and operating system distributions for their project documentation without displaying an intrusive cookie consent banner.

**Solution**: The developer self-hosts Ackee on a $5/month VPS using Docker Compose and embeds `tracker.js`.

**Result**: Complete visibility into traffic spikes and referral sources with 100% GDPR compliance and zero cookie banner prompts.

---

## 🔗 Related Topics

- [Ackee Repository Documentation](../../github_repos/developer-tools/ackee.md) — Upstream GitHub repository and architecture.
- [Docker DevOps Guide](../../devops/docker.md) — Containerization best practices.

---

## 📚 References

- [Ackee Official Website](https://ackee.electerious.com)
- [Ackee Documentation](https://github.com/electerious/Ackee/tree/master/docs)
- [GitHub Repository](https://github.com/electerious/Ackee)

---

*← Back to [Free Tools](./README.md) · [Root Index](../../README.md)*
