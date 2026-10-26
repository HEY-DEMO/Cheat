# Resiliency & Fault Tolerance

> **Domain**: System Reliability, Transient Failure Handling, Self-Healing Systems  
> **Index Numbers**: 9, 10, 11, 12, 13, 14, 20, 44, 85, 87, 95, 96

---

## 9. Service Discovery

### What
Service Discovery is an automated mechanism through which microservices and infrastructure components register their network locations (IP address, port, health status) in a centralized registry and locate other services dynamically at runtime without hardcoded hostnames or IPs.

### Why
- In modern cloud/container environments (Kubernetes, AWS ECS), instances constantly spin up, scale down, crash, or move to different physical hosts.
- Hardcoded endpoints or static DNS records lead to stale routing, manual configuration errors, and slow propagation during changes.
- Automatically handles health tracking and drops unhealthy instances from rotation.

### Where We Use Them
- **Client-Side Discovery**: Microservices query HashiCorp Consul, Netflix Eureka, or Apache Zookeeper directly before dispatching requests.
- **Server-Side Discovery**: AWS ALB / Envoy Proxy / Kubernetes CoreDNS where clients make requests to a virtual service name (`http://payment-service.prod.svc.cluster.local`) and the platform discovers and routes to live pods.

---

## 10. Circuit Breakers

### What
A design pattern that monitors remote calls and stops calls from proceeding when a downstream dependency is failing or timing out. Like an electrical circuit breaker, it transitions between three states:
- **Closed**: Requests pass through normally while monitoring error rates.
- **Open**: When failure thresholds (e.g., 50% errors in 10s) are breached, requests fail fast immediately without hitting downstream systems.
- **Half-Open**: After a cooldown period, allows a trial batch of requests to pass through to verify if the dependency has recovered.

### Why
- Prevents **cascading failures** across a distributed system when one downstream dependency stalls or crashes.
- Conserves caller resources (threads, sockets, memory) by failing fast rather than hanging on connection timeouts.
- Gives the struggling downstream service room and time to recover.

### Where We Use Them
- High-volume RPC/HTTP boundaries in microservices using Resilience4j, Polly (.NET), Envoy Proxy, Istio, or Netflix Hystrix.
- Payment gateway wrappers (e.g., failing fast to fallback payment processors when Stripe or PayPal is degraded).

---

## 11. Timeouts

### What
A timeout is an explicit upper bound on the maximum duration a client or server is willing to wait for an operation (network connection, socket read, query execution, or thread lock acquisition) before abandoning the operation and releasing resources.

### Why
- Network failures, server freezes, or packet drops often leave connections open indefinitely without returning an error.
- Without timeouts, incoming worker threads block waiting for responses, quickly exhausting thread pools and causing total system freeze.
- Bounds latency and enforces strict SLA budgets.

### Where We Use Them
- HTTP/gRPC client configurations (e.g., connect timeout = 500ms, read timeout = 2s).
- Database query timeouts (`statement_timeout = 5000ms` in PostgreSQL) preventing unindexed queries from hanging database locks.
- Cache lookups (Redis command timeout = 100ms) to ensure cache misses fail quickly and fall back to databases.

---

## 12. Retries

### What
A fault-handling strategy where a client or intermediate service automatically re-executes a failed operation when encountering a transient failure (network glitch, brief packet drop, rate limit, or service restart).

### Why
- Networks and distributed systems are fundamentally unreliable; a large percentage of failures are temporary (transient) and succeed on immediate or near-immediate retry.
- Enhances end-user availability and reliability without human intervention.

### Where We Use Them
- Idempotent API calls (HTTP `GET`, `PUT`, `DELETE`).
- Outbound third-party API clients, cloud SDK operations (S3 uploads, DynamoDB reads).
- Event consumers pulling messages from message brokers.
- *Caution*: Retries must only be used with idempotent operations or safe network failures (e.g., connection reset before request transmission) to avoid duplicate charges or duplicate rows.

---

## 13. Exponential Backoff

### What
An algorithm that progressively doubles the wait interval between consecutive retry attempts (e.g., 100ms, 200ms, 400ms, 800ms) and introduces randomized jitter to desynchronize retry spikes.

### Why
- Immediate or constant-interval retries create the **thundering herd problem**, where thousands of failing clients hammer an already recovering service simultaneously, crashing it again.
- Jitter (`random_between(0, backoff)`) disperses retry bursts evenly across time, giving services a smooth recovery runway.

### Where We Use Them
- Cloud SDKs (AWS SDK, Google Cloud SDK) when encountering HTTP 429 (Too Many Requests) or 503 (Service Unavailable).
- Distributed background workers pulling and reprocessing failed tasks.
- Database connection reconnection logic after unexpected cluster failover.

---

## 14. Idempotency

### What
A property of an operation whereby performing it multiple times with the exact same inputs produces the identical state outcome as performing it once, returning the original result without side effects.

### Why
- In distributed systems with network drops and retries, a client may send a request, the server executes it, but the network drops the acknowledgement response.
- If the client retries, a non-idempotent operation will execute twice (e.g., charging a credit card twice or creating duplicate orders).
- Guarantees safety under network partitions and retry loops.

### Where We Use Them
- **Idempotency Keys**: Clients send unique UUIDs in headers (`Idempotency-Key: 7f3b...`) saved in a fast store (Redis) with request status and response payload.
- Database operations using UPSERT (`INSERT ... ON CONFLICT DO UPDATE`) or atomic conditional writes.
- Payment APIs (Stripe, Adyen, PayPal).

---

## 20. Dead Letter Queues (DLQ)

### What
A designated secondary queue or storage buffer where a message broker automatically routes messages that cannot be processed successfully after reaching the maximum retry threshold or failing validation (poison pills).

### Why
- Prevents **poison pill** messages (malformed JSON, corrupted data, unhandled null pointers) from endlessly blocking the primary processing queue.
- Isolates failed messages for post-mortem debugging, inspection, alerting, and manual replay once the root cause is resolved.

### Where We Use Them
- Asynchronous messaging architectures using AWS SQS DLQ, RabbitMQ DLX (Dead Letter Exchange), Apache Kafka error topics, or GCP Pub/Sub.
- Order processing, billing pipelines, webhook ingestion systems.

---

## 44. Backpressure

### What
A flow-control mechanism where a downstream consumer signals an upstream producer to slow down or pause message/data emission when incoming volume exceeds the consumer's processing capacity or memory limits.

### Why
- When producers outpace consumers, intermediate buffers fill up, leading to out-of-memory (OOM) crashes, high garbage collection pauses, and dropped packets.
- Stabilizes systems under sudden load spikes by converting unbounded buffering into controlled flow moderation.

### Where We Use Them
- Reactive stream processing libraries (RxJava, Project Reactor, Akka Streams).
- TCP window scaling (TCP flow control receiver window).
- Node.js streams (`stream.write()` returning `false` until `'drain'` event fires).
- Kafka consumers adjusting partition fetch sizes and poll intervals.

---

## 85. Failover

### What
An automated or manual operational procedure that switches production workload from a failing primary hardware node, database instance, service, or datacenter to a redundant standby instance without data loss or prolonged interruption.

### Why
- Hardware failures, power outages, and software crashes are inevitable in large-scale deployments.
- High Availability (HA) architectures require recovery times measured in seconds (low RTO - Recovery Time Objective) rather than hours of manual restoration.

### Where We Use Them
- Relational database primary-replica failover (e.g., AWS RDS Multi-AZ promotion, PostgreSQL Patroni with etcd).
- DNS failover (Cloudflare, AWS Route 53 Health Checks re-routing DNS A-records from primary to secondary datacenter).
- Reverse proxy load balancers detecting dead backend instances and redirecting active traffic.

---

## 87. Chaos Engineering

### What
The discipline of experimenting on a distributed software system in production or staging by intentionally injecting real-world infrastructure failures (killing instances, injecting latency, dropping packets, terminating database primaries) to build confidence in the system's resilience.

### Why
- Complex distributed interactions cannot be fully validated through unit or integration tests alone.
- Uncovers hidden bugs, missing timeouts, misconfigured circuit breakers, and cascading failures before they trigger catastrophic outages in live customer traffic.

### Where We Use Them
- Netflix Chaos Monkey, Chaos Kong (simulating entire AWS AZ outages).
- Chaos Mesh, LitmusChaos in Kubernetes clusters to inject network packet loss and pod kills.
- Gremlin for scheduled, controlled enterprise resilience game days.

---

## 95. Network Partitions

### What
A communication breakdown in a distributed network where one group of servers or nodes can no longer communicate with another group due to router failures, cable severance, firewall misconfigurations, or cloud VPC outages, splitting the cluster into disconnected components (split-brain).

### Why
- Networks are asynchronous and fallible; according to the CAP theorem, distributed databases and consensus algorithms must be explicitly engineered to handle partitions gracefully.
- Prevents **split-brain** scenarios where two isolated clusters simultaneously believe they are the authoritative leader and accept conflicting writes.

### Where We Use Them
- Consensus protocols (Raft, Paxos, ZAB in ZooKeeper) requiring a strict quorum (majority: `N/2 + 1`) to commit changes or elect leaders.
- Distributed database failover safeguards (e.g., CockroachDB, TiDB, Cassandra partition discovery).

---

## 96. Clock Skew

### What
The divergence in current time between internal hardware clocks (oscillators) across different physical machines in a distributed network, caused by temperature fluctuations, hardware drift, and network latency in NTP (Network Time Protocol) synchronization.

### Why
- Distributed systems cannot rely on wall-clock time (`System.currentTimeMillis()`) to determine the chronological ordering of distributed events.
- Relying on wall clocks leads to data corruption, silent write overwrites (Last-Write-Wins), and broken transaction isolation.

### Where We Use Them
- **Logical Clocks**: Lamport Timestamps and Vector Clocks to establish causal ordering without physical time.
- **Hybrid Logical Clocks (HLC)**: Combining physical and logical time in distributed databases like CockroachDB and MongoDB.
- **Google Spanner TrueTime API**: Hardware atomic clocks and GPS receivers providing bounded time uncertainty `[now - ε, now + ε]` to guarantee global external consistency.
