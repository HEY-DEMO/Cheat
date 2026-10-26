# Asynchronous & Real-Time Communication

> **Domain**: Asynchronous Messaging, Event Pipelines, Real-Time Web Protocols  
> **Index Numbers**: 15, 16, 17, 18, 19, 21, 22, 23, 24, 101

---

## 15. Message Queues

### What
A point-to-point asynchronous communication buffer where producers send messages and one or more consumers pull/receive them. Each message is processed and consumed by exactly one consumer (competing consumers pattern), after which it is acknowledged and removed from the queue.

### Why
- **Decoupling**: Decouples producer execution and throughput from consumer processing availability and speed.
- **Load Leveling**: Smooths out traffic spikes; spikes are absorbed in the queue without crashing backend processors.
- **Guaranteed Delivery**: Durable queues persist messages to disk, surviving worker crashes or network interruptions.

### Where We Use Them
- Background task processing (video transcoding, PDF invoice generation, sending transactional emails).
- Technologies: RabbitMQ, AWS SQS, Celery, BullMQ (Redis-backed), ActiveMQ.

---

## 16. Pub/Sub (Publish-Subscribe)

### What
A broadcast messaging pattern where message senders (publishers) do not direct messages to specific receivers, but categorize them into named channels or topics. Multiple subscribers receive a copy of every message published to the topic they subscribe to (fan-out pattern).

### Why
- Provides 1-to-many communication without publishers knowing who the subscribers are or how many exist.
- Allows independent development and deployment of downstream consumers; new listeners can be added without altering publisher code.

### Where We Use Them
- Apache Kafka topics, AWS SNS, Google Cloud Pub/Sub, Redis Pub/Sub.
- Real-time notifications, audit log ingestion, updating cache layers, broadcasting market price ticks across multiple services.

---

## 17. Event-Driven Architecture (EDA)

### What
A software architecture model where system behavior and data flow are governed by the production, detection, and consumption of state-change occurrences ("events"). Services react to events asynchronously rather than invoking synchronous request-response chains.

### Why
- Eliminates tight temporal and architectural coupling between microservices.
- High scalability: services process domain events at their own pace without blocking upstream components.
- Enables rich event streaming, replayability, and state reconstruction.

### Where We Use Them
- E-commerce order lifecycles (e.g., `OrderPlaced` event consumed independently by Inventory, Billing, Shipping, and Fraud Detection services).
- Technologies: Apache Kafka, AWS EventBridge, Debezium (Change Data Capture - CDC).

---

## 18. Distributed Transactions

### What
A transaction that involves reads, updates, or commits across multiple autonomous network nodes, partitions, or independent database stores, requiring coordinated ACID compliance across all participants.

### Why
- In microservices or sharded databases, a single business action (e.g., bank transfer between accounts) often spans multiple physical databases.
- Ensures atomic consistency: either all database updates succeed, or all changes roll back to prevent half-completed states.

### Where We Use Them
- **Two-Phase Commit (2PC)**: Traditional protocol using a coordinator with Prepare and Commit phases (XA transactions in databases).
- **Consensus-backed Transactions**: Google Spanner (Paxos + 2PC), CockroachDB (Raft).
- Note: 2PC is synchronous and blocking; modern microservices favor the Saga Pattern for high-throughput resilience.

---

## 19. Saga Pattern

### What
A sequence of local transactions coordinated across multiple microservices to manage long-running distributed business transactions. Each service executes its local transaction and publishes an event; if any step fails, the saga triggers a series of **compensating transactions** that rollback earlier changes in reverse order.

### Why
- Avoids the blocking, high-latency locks and single-point-of-failure issues of Two-Phase Commit (2PC) in distributed microservices.
- Maintains eventual consistency across autonomous data stores while preserving service boundaries.

### Where We Use Them
- **Choreography-based Saga**: Each service listens to events and publishes next-step events (used for simpler 2–4 step workflows).
- **Orchestration-based Saga**: A centralized orchestrator (e.g., Temporal, AWS Step Functions, Camunda) commands each participant service when to execute and coordinates compensation upon failure.
- Travel booking (Flight -> Hotel -> Rental Car reservation with compensation refunds on failure).

---

## 21. Cron Jobs

### What
A time-based job scheduling utility in operating systems and distributed frameworks that runs automated shell scripts, database commands, or background tasks at fixed intervals, recurring dates, or specific calendar times.

### Why
- Automates routine maintenance, aggregation, and repetitive batch processes without human supervision.
- Frees application servers from running ad-hoc periodic threads inside user request cycles.

### Where We Use Them
- Unix `crontab`, Kubernetes `CronJob`, AWS EventBridge Scheduler, Celery Beat.
- Daily database backups, generating nightly analytics reports, sweeping expired session tokens, monthly subscription billing generation.

---

## 22. WebSockets

### What
A standardized communication protocol (RFC 6455) providing a persistent, full-duplex, bidirectional communication channel over a single long-lived TCP connection, initiated via an HTTP handshake (`Upgrade: websocket`).

### Why
- HTTP request/response overhead (headers, handshake latency) is too costly for high-frequency real-time updates.
- Enables the server to push data to the client instantly without waiting for a client request, achieving sub-10ms delivery.

### Where We Use Them
- Collaborative workspaces (Figma cursor tracking, Google Docs editing).
- Live chat applications (Discord, Slack, WhatsApp Web).
- Financial trading terminals (real-time order book and stock tickers), live multiplayer browser gaming.

---

## 23. Long Polling

### What
A client-server communication technique where the client sends an HTTP request to the server, and instead of immediately responding with empty data, the server holds the connection open until new data is available or a timeout occurs. Once data is returned, the client immediately initiates a new request.

### Why
- Bridges the gap for real-time updates over standard HTTP infrastructure where WebSockets may be blocked by corporate firewalls, strict proxies, or legacy clients.
- Drastically reduces wasted network roundtrips compared to traditional rapid polling (polling every 1 second).

### Where We Use Them
- Chat widgets on restricted networks, notification bells, AWS SQS long polling (`WaitTimeSeconds = 20`), fallback transports in Socket.IO.

---

## 24. Server-Sent Events (SSE)

### What
A lightweight web standard (part of HTML5) that allows a web server to push continuous, unidirectional streams of text data (formatted as `text/event-stream`) to client browsers over a persistent HTTP/1.1 or HTTP/2 connection.

### Why
- Simpler than WebSockets: uses standard HTTP without custom binary framing or protocol upgrades.
- Built-in reconnection, event IDs, and message replay capabilities natively supported by browser `EventSource` APIs.
- Ideal when data only flows from server to client (unidirectional).

### Where We Use Them
- Streaming responses from Large Language Models (ChatGPT, Claude, Gemini API completion streams).
- Real-time sports scoreboards, stock ticker feeds, social media activity tickers, build progress logs in CI/CD platforms.

---

## 101. Webhooks

### What
A user-defined HTTP callback mechanism ("reverse API") where a source server programmatically delivers an event payload via an HTTP `POST` request to a target subscriber URL the moment a specific event occurs, rather than requiring the consumer to continuously poll for updates.

### Why
- Eliminates wasteful and expensive HTTP polling: subscribers receive events in real time without repeatedly querying API endpoints.
- Drastically saves network bandwidth and CPU cycles for both provider and consumer systems.
- Asynchronous and decoupled: provider queues the delivery and consumer processes it in background workers.

### Where We Use Them
- Payment state notifications (Stripe `charge.succeeded`, PayPal order notifications).
- Git repository events (GitHub push, pull request triggers in CI/CD).
- Messaging and telephony callbacks (Twilio incoming SMS/call webhooks).
- Best practices: Always verify webhook signatures (HMAC SHA-256) and return an immediate HTTP 200 before executing background processing.
