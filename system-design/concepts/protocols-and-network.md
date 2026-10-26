# Protocols & Networking

> **Domain**: Transport Protocols, Network Topologies, Application Layer Protocols, RPC Frameworks  
> **Index Numbers**: 97, 98, 99, 100

---

## 97. DNS (Domain Name System)

### What
The hierarchical, decentralized global naming system that translates human-friendly domain names (e.g., `api.example.com`) into numerical, machine-routable IP addresses (e.g., IPv4 `198.51.100.1` or IPv6 `2001:db8::1`).

### Why
- Humans remember readable names, but network routers require IP addresses to direct packets across the internet.
- Serves as the first layer of global traffic routing, load distribution, and high-availability failover.

### Where We Use Them
- DNS Record types: `A` (IPv4), `AAAA` (IPv6), `CNAME` (canonical alias), `MX` (mail exchange), `TXT` (domain verification).
- Advanced routing: **Geo-DNS** (routing users to closest regional server), **Latency-based routing**, **DNS Round-Robin** load balancing, automated health checks with failover (Cloudflare, AWS Route 53).

---

## 98. TCP vs UDP (Transmission Control Protocol vs User Datagram Protocol)

### What
The two foundational Transport Layer (Layer 4) protocols of the Internet Protocol suite:
- **TCP**: A connection-oriented protocol that establishes a connection via a 3-way handshake (`SYN` -> `SYN-ACK` -> `ACK`), guaranteeing reliable, ordered, and error-checked delivery of byte streams with flow and congestion control.
- **UDP**: A lightweight, connectionless protocol that sends discrete packets (datagrams) without handshakes, ordering guarantees, or retransmissions ("fire and forget").

### Why
- Different applications demand fundamentally different tradeoffs between **reliability** (TCP) and **raw speed/low latency** (UDP).

### Where We Use Them
- **TCP**: Web browsing (HTTP/1.1, HTTP/2), file transfers (FTP, SFTP), database connections, email (SMTP/IMAP), where losing a single byte corrupts the data.
- **UDP**: Real-time multiplayer gaming, live video/audio streaming (WebRTC, VoIP), DNS queries, where receiving the latest packet immediately is far more important than retransmitting an obsolete lost packet.

---

## 99. HTTP/2 & HTTP/3

### What
Successive major evolutions of the Hypertext Transfer Protocol:
- **HTTP/2**: Introduced binary framing, header compression (HPACK), and **Multiplexing** (multiple concurrent bidirectional requests and responses over a single TCP connection, eliminating HTTP/1.1 head-of-line blocking).
- **HTTP/3**: Replaces the underlying TCP transport with **QUIC** (built on top of UDP), eliminating TCP-level head-of-line blocking during packet loss, integrating TLS 1.3 by default, and enabling connection migration when switching networks (e.g., Wi-Fi to 5G).

### Why
- HTTP/1.1 suffered from high connection overhead (browsers opening 6 TCP connections per domain) and application head-of-line blocking.
- HTTP/2 and HTTP/3 dramatically reduce page load times, bandwidth consumption, and handshake latency over lossy mobile networks.

### Where We Use Them
- Modern web delivery over CDNs (Cloudflare, Fastly, AWS CloudFront), modern mobile applications, RESTful APIs.

---

## 100. gRPC (Google Remote Procedure Call)

### What
A high-performance, open-source, universal RPC framework developed by Google that enables client applications to directly invoke methods on a server application running on a remote machine as if it were a local object, using **Protocol Buffers (Protobuf)** as its Interface Definition Language (IDL) and serialization mechanism over **HTTP/2**.

### Why
- Up to 7x–10x faster and uses up to 80% less bandwidth than traditional JSON-over-HTTP/1.1 REST APIs due to binary serialization and multiplexed HTTP/2 streams.
- Enforces strict compile-time typing, contract-first API development, and auto-generates client/server stubs across dozens of programming languages.
- Natively supports streaming: Unary, Server Streaming, Client Streaming, and Bidirectional Streaming.

### Where We Use Them
- High-throughput internal inter-service communication within microservices architectures and Kubernetes clusters.
- Low-latency data pipelines, real-time telemetry streaming, mobile-to-cloud backends.
