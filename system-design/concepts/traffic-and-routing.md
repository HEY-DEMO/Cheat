# 🚦 Traffic, Routing & Caching

> **Category**: `system-design / concepts` · **Last Updated**: `2026-10-25` · **Difficulty**: `Intermediate`

---

## 📋 Overview

Managing user requests at scale requires traffic conditioning, intelligent load distribution, edge acceleration, and multi-tier caching to prevent backend service exhaustion and ensure sub-second response times.

---

## 1. Rate Limiting

- **What**: A mechanism that caps the number of requests a client, IP, or API key can make within a given time window (e.g., 100 req/min). Common algorithms include Token Bucket, Leaky Bucket, Fixed Window Counter, and Sliding Window Log.
- **Why**: Prevents server overload, protects against brute-force/DDoS attacks, curbs web scraping, and enforces SaaS tiered monetization limits.
- **Where we use it**:
  - API gateways (Kong, AWS API Gateway) protecting public endpoints.
  - Redis-backed distributed token buckets across microservices.
  - Authentication endpoints (login, password reset, OTP requests) to thwart credential stuffing.

---

## 2. Caching

- **What**: Storing copies of frequently accessed, expensive-to-compute data in high-speed, volatile storage (e.g., RAM) so future requests are served orders of magnitude faster.
- **Why**: Slashes database read load, reduces response latency from hundreds of milliseconds to microseconds, and absorbs sudden traffic spikes.
- **Where we use it**:
  - In-memory data stores (Redis, Memcached) caching user sessions, hot database rows, or catalog items.
  - Application-level local memory (LRU caches, Guava, Caffeine).
  - Browser/client caching via HTTP `Cache-Control` and `ETag` headers.

---

## 3. Load Balancing

- **What**: Distributing incoming network traffic evenly across a pool of backend servers using algorithms such as Round Robin, Least Connections, IP Hash, or Weighted Response Time.
- **Why**: Eliminates single points of failure (high availability), scales throughput horizontally, and seamlessly routes around unhealthy nodes.
- **Where we use it**:
  - Layer 4 (Transport) load balancers (AWS NLB, HAProxy) distributing raw TCP/UDP packets.
  - Layer 7 (Application) load balancers (AWS ALB, NGINX, Envoy) inspecting HTTP headers, cookies, and URL paths.
  - DNS-based load balancing (Route 53 latency/geo-routing) distributing requests across global regions.

---

## 4. Reverse Proxies

- **What**: An intermediary server placed in front of web servers that intercepts client requests, forwards them to backend servers, and returns the response to the client on their behalf.
- **Why**: Hides backend topology and internal IP addresses, handles SSL/TLS termination, provides centralized logging, and compresses responses (Gzip/Brotli).
- **Where we use it**:
  - NGINX, Traefik, or Caddy serving as the ingress point for Docker/Kubernetes clusters.
  - Terminating HTTPS certificates so backend services only communicate over fast internal HTTP.
  - Static asset serving directly from disk without hitting application runtimes.

---

## 5. API Gateways

- **What**: A specialized reverse proxy acting as the single front-door entry point for all client requests in a microservices architecture.
- **Why**: Centralizes cross-cutting concerns (authentication, rate limiting, logging, request validation, CORS, circuit breaking) so individual microservices don't duplicate them.
- **Where we use it**:
  - Kong, Apigee, AWS API Gateway, or KrakenD sitting between mobile/web clients and internal microservices.
  - Protocol translation (e.g., translating external HTTP/JSON into internal gRPC/Protobuf).
  - Aggregating responses from multiple backend microservices into a single client payload (BFF pattern).

---

## 48. CDN (Content Delivery Network)

- **What**: A geographically distributed network of proxy servers and data centers that cache content physically close to end-users.
- **Why**: Drastically reduces round-trip time (RTT) and latency, reduces origin server bandwidth costs by 70–90%, and provides built-in DDoS absorption.
- **Where we use it**:
  - Cloudflare, CloudFront, Fastly, or Akamai serving JavaScript bundles, CSS, images, and videos.
  - Live video streaming (HLS/DASH chunk delivery) to global audiences.
  - Software binary and firmware distribution downloads.

---

## 49. Edge Caching

- **What**: Storing computed application responses and dynamic content at edge POPs (Points of Presence) instead of only at the central origin datacenter.
- **Why**: Moves computational verification and dynamic response delivery directly to the user's nearest telecom node, avoiding cross-continental fiber round-trips.
- **Where we use it**:
  - Vercel Edge Network, Cloudflare Workers KV, and Fastly Compute@Edge.
  - Serving personalized homepage shells and localized e-commerce catalog data directly from edge points.
  - Stale-While-Revalidate caching strategies for dynamic headless CMS content.

---

## 50. Cache Invalidation

- **What**: The process of declaring cached data stale or purged when the underlying source of truth changes in the primary database.
- **Why**: Prevents serving outdated, incorrect, or corrupt data to users while retaining cache performance benefits.
- **Where we use it**:
  - **Write-Through**: Writing to cache and DB simultaneously.
  - **Write-Behind (Write-Back)**: Writing to cache immediately, deferring DB write asynchronously.
  - **Cache-Aside**: Application invalidates/deletes the key on write; the next read repopulates it.
  - Purging CDN URLs via webhooks when a CMS article or product price is updated.

---

## 102. API Versioning

- **What**: The practice of managing changes to an API contract across iterations to allow evolution of endpoints, schemas, and behavior without breaking existing client integrations.
- **Why**: Breaking changes (renaming fields, changing data types, removing endpoints) immediately crash mobile apps, third-party partner integrations, and older web clients. Versioning establishes explicit lifecycle management and backward compatibility windows.
- **Where we use it**:
  - **URI Path Versioning**: `https://api.example.com/v1/orders` (most common, easiest to route at API Gateway/load balancer).
  - **Header/Content Negotiation**: `Accept: application/vnd.company.v2+json` (RESTful, keeps URIs clean).
  - **Query Parameter Versioning**: `https://api.example.com/orders?version=2` (common in webhook definitions).
  - Routing rules in API Gateways (Kong, AWS API Gateway) to direct `/v1` to legacy clusters and `/v2` to new microservices.

---

## 🔗 Related Topics

- [Resiliency & Fault Tolerance](resiliency-and-fault-tolerance.md)
- [Protocols & Network Communication](protocols-and-network.md)
- [Security & Access Control](security-and-protection.md)

---

*← Back to [System Design Concepts](./README.md) · [System Design Index](../README.md)*
