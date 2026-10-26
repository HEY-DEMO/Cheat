# System Design Concepts (1–111 Master Catalog)

A structured, categorized reference guide covering the **111 fundamental backend and system design concepts** essential for building reliable, scalable, and high-performance distributed systems.

Each concept is broken down into:
- **What**: Core definition, underlying mechanics, and architectural purpose.
- **Why**: The engineering problem it solves, tradeoffs, and key benefits.
- **Where we use them**: Concrete industry use cases, cloud services, and production tools.

---

## Domain Categorization

The 111 concepts are grouped into 9 cohesive architectural domain modules:

| Domain Module | File | Covered Concepts | Concept Count |
|:---|:---|:---|:---:|
| **1. Traffic & Routing** | [traffic-and-routing.md](traffic-and-routing.md) | 1–5, 48–50, 102 | 9 |
| **2. Scaling & Deployment** | [scaling-and-deployment.md](scaling-and-deployment.md) | 6–8, 45–47, 51–57, 83, 86, 88, 103–108 | 22 |
| **3. Resiliency & Fault Tolerance** | [resiliency-and-fault-tolerance.md](resiliency-and-fault-tolerance.md) | 9–14, 20, 44, 85, 87, 95, 96 | 12 |
| **4. Asynchronous & Real-Time** | [asynchronous-and-realtime.md](asynchronous-and-realtime.md) | 15–19, 21–24, 101 | 10 |
| **5. Database & Storage** | [database-and-storage.md](database-and-storage.md) | 25–35, 81–82, 84 | 14 |
| **6. Concurrency & Compute** | [concurrency-and-compute.md](concurrency-and-compute.md) | 36–43, 89–90 | 10 |
| **7. Observability & SRE** | [observability-and-sre.md](observability-and-sre.md) | 58–66, 91–94, 109–111 | 16 |
| **8. Security & Protection** | [security-and-protection.md](security-and-protection.md) | 67–80 | 14 |
| **9. Protocols & Networking** | [protocols-and-network.md](protocols-and-network.md) | 97–100 | 4 |

---

## 1–111 Master Concept Index

| # | Concept Name | Domain Module | Reference Link |
|:---:|:---|:---|:---|
| 1 | Rate Limiting | Traffic & Routing | [traffic-and-routing.md#1-rate-limiting](traffic-and-routing.md) |
| 2 | Caching | Traffic & Routing | [traffic-and-routing.md#2-caching](traffic-and-routing.md) |
| 3 | Load Balancing | Traffic & Routing | [traffic-and-routing.md#3-load-balancing](traffic-and-routing.md) |
| 4 | Reverse Proxies | Traffic & Routing | [traffic-and-routing.md#4-reverse-proxies](traffic-and-routing.md) |
| 5 | API Gateways | Traffic & Routing | [traffic-and-routing.md#5-api-gateways](traffic-and-routing.md) |
| 6 | CI/CD | Scaling & Deployment | [scaling-and-deployment.md#6-cicd](scaling-and-deployment.md) |
| 7 | Docker | Scaling & Deployment | [scaling-and-deployment.md#7-docker](scaling-and-deployment.md) |
| 8 | Kubernetes | Scaling & Deployment | [scaling-and-deployment.md#8-kubernetes](scaling-and-deployment.md) |
| 9 | Service Discovery | Resiliency & Fault Tolerance | [resiliency-and-fault-tolerance.md#9-service-discovery](resiliency-and-fault-tolerance.md) |
| 10 | Circuit Breakers | Resiliency & Fault Tolerance | [resiliency-and-fault-tolerance.md#10-circuit-breakers](resiliency-and-fault-tolerance.md) |
| 11 | Timeouts | Resiliency & Fault Tolerance | [resiliency-and-fault-tolerance.md#11-timeouts](resiliency-and-fault-tolerance.md) |
| 12 | Retries | Resiliency & Fault Tolerance | [resiliency-and-fault-tolerance.md#12-retries](resiliency-and-fault-tolerance.md) |
| 13 | Exponential Backoff | Resiliency & Fault Tolerance | [resiliency-and-fault-tolerance.md#13-exponential-backoff](resiliency-and-fault-tolerance.md) |
| 14 | Idempotency | Resiliency & Fault Tolerance | [resiliency-and-fault-tolerance.md#14-idempotency](resiliency-and-fault-tolerance.md) |
| 15 | Message Queues | Asynchronous & Real-Time | [asynchronous-and-realtime.md#15-message-queues](asynchronous-and-realtime.md) |
| 16 | Pub/Sub | Asynchronous & Real-Time | [asynchronous-and-realtime.md#16-pubsub](asynchronous-and-realtime.md) |
| 17 | Event-Driven Architecture | Asynchronous & Real-Time | [asynchronous-and-realtime.md#17-event-driven-architecture](asynchronous-and-realtime.md) |
| 18 | Distributed Transactions | Asynchronous & Real-Time | [asynchronous-and-realtime.md#18-distributed-transactions](asynchronous-and-realtime.md) |
| 19 | Saga Pattern | Asynchronous & Real-Time | [asynchronous-and-realtime.md#19-saga-pattern](asynchronous-and-realtime.md) |
| 20 | Dead Letter Queues | Resiliency & Fault Tolerance | [resiliency-and-fault-tolerance.md#20-dead-letter-queues](resiliency-and-fault-tolerance.md) |
| 21 | Cron Jobs | Asynchronous & Real-Time | [asynchronous-and-realtime.md#21-cron-jobs](asynchronous-and-realtime.md) |
| 22 | WebSockets | Asynchronous & Real-Time | [asynchronous-and-realtime.md#22-websockets](asynchronous-and-realtime.md) |
| 23 | Long Polling | Asynchronous & Real-Time | [asynchronous-and-realtime.md#23-long-polling](asynchronous-and-realtime.md) |
| 24 | Server-Sent Events | Asynchronous & Real-Time | [asynchronous-and-realtime.md#24-server-sent-events](asynchronous-and-realtime.md) |
| 25 | Database Indexing | Database & Storage | [database-and-storage.md#25-database-indexing](database-and-storage.md) |
| 26 | Query Optimization | Database & Storage | [database-and-storage.md#26-query-optimization](database-and-storage.md) |
| 27 | N+1 Queries | Database & Storage | [database-and-storage.md#27-n1-queries](database-and-storage.md) |
| 28 | Connection Pooling | Database & Storage | [database-and-storage.md#28-connection-pooling](database-and-storage.md) |
| 29 | Read Replicas | Database & Storage | [database-and-storage.md#29-read-replicas](database-and-storage.md) |
| 30 | Sharding | Database & Storage | [database-and-storage.md#30-sharding](database-and-storage.md) |
| 31 | Partitioning | Database & Storage | [database-and-storage.md#31-partitioning](database-and-storage.md) |
| 32 | Replication | Database & Storage | [database-and-storage.md#32-replication](database-and-storage.md) |
| 33 | Leader Election | Database & Storage | [database-and-storage.md#33-leader-election](database-and-storage.md) |
| 34 | CAP Theorem | Database & Storage | [database-and-storage.md#34-cap-theorem](database-and-storage.md) |
| 35 | Eventual Consistency | Database & Storage | [database-and-storage.md#35-eventual-consistency](database-and-storage.md) |
| 36 | Optimistic Locking | Concurrency & Compute | [concurrency-and-compute.md#36-optimistic-locking](concurrency-and-compute.md) |
| 37 | Pessimistic Locking | Concurrency & Compute | [concurrency-and-compute.md#37-pessimistic-locking](concurrency-and-compute.md) |
| 38 | Distributed Locks | Concurrency & Compute | [concurrency-and-compute.md#38-distributed-locks](concurrency-and-compute.md) |
| 39 | Race Conditions | Concurrency & Compute | [concurrency-and-compute.md#39-race-conditions](concurrency-and-compute.md) |
| 40 | Deadlocks | Concurrency & Compute | [concurrency-and-compute.md#40-deadlocks](concurrency-and-compute.md) |
| 41 | Memory Leaks | Concurrency & Compute | [concurrency-and-compute.md#41-memory-leaks](concurrency-and-compute.md) |
| 42 | Garbage Collection | Concurrency & Compute | [concurrency-and-compute.md#42-garbage-collection](concurrency-and-compute.md) |
| 43 | Thread Safety | Concurrency & Compute | [concurrency-and-compute.md#43-thread-safety](concurrency-and-compute.md) |
| 44 | Backpressure | Resiliency & Fault Tolerance | [resiliency-and-fault-tolerance.md#44-backpressure](resiliency-and-fault-tolerance.md) |
| 45 | Autoscaling | Scaling & Deployment | [scaling-and-deployment.md#45-autoscaling](scaling-and-deployment.md) |
| 46 | Horizontal Scaling | Scaling & Deployment | [scaling-and-deployment.md#46-horizontal-scaling](scaling-and-deployment.md) |
| 47 | Vertical Scaling | Scaling & Deployment | [scaling-and-deployment.md#47-vertical-scaling](scaling-and-deployment.md) |
| 48 | CDN | Traffic & Routing | [traffic-and-routing.md#48-cdn](traffic-and-routing.md) |
| 49 | Edge Caching | Traffic & Routing | [traffic-and-routing.md#49-edge-caching](traffic-and-routing.md) |
| 50 | Cache Invalidation | Traffic & Routing | [traffic-and-routing.md#50-cache-invalidation](traffic-and-routing.md) |
| 51 | Feature Flags | Scaling & Deployment | [scaling-and-deployment.md#51-feature-flags](scaling-and-deployment.md) |
| 52 | Blue-Green Deployment | Scaling & Deployment | [scaling-and-deployment.md#52-blue-green-deployment](scaling-and-deployment.md) |
| 53 | Canary Releases | Scaling & Deployment | [scaling-and-deployment.md#53-canary-releases](scaling-and-deployment.md) |
| 54 | Rolling Deployments | Scaling & Deployment | [scaling-and-deployment.md#54-rolling-deployments](scaling-and-deployment.md) |
| 55 | Rollbacks | Scaling & Deployment | [scaling-and-deployment.md#55-rollbacks](scaling-and-deployment.md) |
| 56 | Health Checks | Scaling & Deployment | [scaling-and-deployment.md#56-health-checks](scaling-and-deployment.md) |
| 57 | Liveness & Readiness Probes | Scaling & Deployment | [scaling-and-deployment.md#57-liveness-and-readiness-probes](scaling-and-deployment.md) |
| 58 | Monitoring | Observability & SRE | [observability-and-sre.md#58-monitoring](observability-and-sre.md) |
| 59 | Logging | Observability & SRE | [observability-and-sre.md#59-logging](observability-and-sre.md) |
| 60 | Distributed Tracing | Observability & SRE | [observability-and-sre.md#60-distributed-tracing](observability-and-sre.md) |
| 61 | Metrics | Observability & SRE | [observability-and-sre.md#61-metrics](observability-and-sre.md) |
| 62 | Alerts | Observability & SRE | [observability-and-sre.md#62-alerts](observability-and-sre.md) |
| 63 | SLOs | Observability & SRE | [observability-and-sre.md#63-slos](observability-and-sre.md) |
| 64 | SLIs | Observability & SRE | [observability-and-sre.md#64-slis](observability-and-sre.md) |
| 65 | Error Budgets | Observability & SRE | [observability-and-sre.md#65-error-budgets](observability-and-sre.md) |
| 66 | Observability | Observability & SRE | [observability-and-sre.md#66-observability](observability-and-sre.md) |
| 67 | Secrets Management | Security & Protection | [security-and-protection.md#67-secrets-management](security-and-protection.md) |
| 68 | IAM | Security & Protection | [security-and-protection.md#68-iam](security-and-protection.md) |
| 69 | OAuth | Security & Protection | [security-and-protection.md#69-oauth](security-and-protection.md) |
| 70 | JWT Rotation | Security & Protection | [security-and-protection.md#70-jwt-rotation](security-and-protection.md) |
| 71 | TLS | Security & Protection | [security-and-protection.md#71-tls](security-and-protection.md) |
| 72 | Encryption at Rest | Security & Protection | [security-and-protection.md#72-encryption-at-rest](security-and-protection.md) |
| 73 | Encryption in Transit | Security & Protection | [security-and-protection.md#73-encryption-in-transit](security-and-protection.md) |
| 74 | WAF | Security & Protection | [security-and-protection.md#74-waf](security-and-protection.md) |
| 75 | DDoS Protection | Security & Protection | [security-and-protection.md#75-ddos-protection](security-and-protection.md) |
| 76 | CORS | Security & Protection | [security-and-protection.md#76-cors](security-and-protection.md) |
| 77 | CSRF | Security & Protection | [security-and-protection.md#77-csrf](security-and-protection.md) |
| 78 | SQL Injection | Security & Protection | [security-and-protection.md#78-sql-injection](security-and-protection.md) |
| 79 | XSS | Security & Protection | [security-and-protection.md#79-xss](security-and-protection.md) |
| 80 | SSRF | Security & Protection | [security-and-protection.md#80-ssrf](security-and-protection.md) |
| 81 | Database Migrations | Database & Storage | [database-and-storage.md#81-database-migrations](database-and-storage.md) |
| 82 | Schema Versioning | Database & Storage | [database-and-storage.md#82-schema-versioning](database-and-storage.md) |
| 83 | Disaster Recovery | Scaling & Deployment | [scaling-and-deployment.md#83-disaster-recovery](scaling-and-deployment.md) |
| 84 | Backups | Database & Storage | [database-and-storage.md#84-backups](database-and-storage.md) |
| 85 | Failover | Resiliency & Fault Tolerance | [resiliency-and-fault-tolerance.md#85-failover](resiliency-and-fault-tolerance.md) |
| 86 | Multi-Region Deployment | Scaling & Deployment | [scaling-and-deployment.md#86-multi-region-deployment](scaling-and-deployment.md) |
| 87 | Chaos Engineering | Resiliency & Fault Tolerance | [resiliency-and-fault-tolerance.md#87-chaos-engineering](resiliency-and-fault-tolerance.md) |
| 88 | Cost Optimization | Scaling & Deployment | [scaling-and-deployment.md#88-cost-optimization](scaling-and-deployment.md) |
| 89 | Cold Starts | Concurrency & Compute | [concurrency-and-compute.md#89-cold-starts](concurrency-and-compute.md) |
| 90 | Serverless Limits | Concurrency & Compute | [concurrency-and-compute.md#90-serverless-limits](concurrency-and-compute.md) |
| 91 | Latency | Observability & SRE | [observability-and-sre.md#91-latency](observability-and-sre.md) |
| 92 | Throughput | Observability & SRE | [observability-and-sre.md#92-throughput](observability-and-sre.md) |
| 93 | p99 Latency | Observability & SRE | [observability-and-sre.md#93-p99-latency](observability-and-sre.md) |
| 94 | Tail Latency | Observability & SRE | [observability-and-sre.md#94-tail-latency](observability-and-sre.md) |
| 95 | Network Partitions | Resiliency & Fault Tolerance | [resiliency-and-fault-tolerance.md#95-network-partitions](resiliency-and-fault-tolerance.md) |
| 96 | Clock Skew | Resiliency & Fault Tolerance | [resiliency-and-fault-tolerance.md#96-clock-skew](resiliency-and-fault-tolerance.md) |
| 97 | DNS | Protocols & Networking | [protocols-and-network.md#97-dns](protocols-and-network.md) |
| 98 | TCP vs UDP | Protocols & Networking | [protocols-and-network.md#98-tcp-vs-udp](protocols-and-network.md) |
| 99 | HTTP/2 & HTTP/3 | Protocols & Networking | [protocols-and-network.md#99-http2--http3](protocols-and-network.md) |
| 100 | gRPC | Protocols & Networking | [protocols-and-network.md#100-grpc](protocols-and-network.md) |
| 101 | Webhooks | Asynchronous & Real-Time | [asynchronous-and-realtime.md#101-webhooks](asynchronous-and-realtime.md) |
| 102 | API Versioning | Traffic & Routing | [traffic-and-routing.md#102-api-versioning](traffic-and-routing.md) |
| 103 | Semantic Versioning | Scaling & Deployment | [scaling-and-deployment.md#103-semantic-versioning-semver](scaling-and-deployment.md) |
| 104 | Infrastructure as Code | Scaling & Deployment | [scaling-and-deployment.md#104-infrastructure-as-code-iac](scaling-and-deployment.md) |
| 105 | Terraform | Scaling & Deployment | [scaling-and-deployment.md#105-terraform](scaling-and-deployment.md) |
| 106 | Helm Charts | Scaling & Deployment | [scaling-and-deployment.md#106-helm-charts](scaling-and-deployment.md) |
| 107 | Build Caching | Scaling & Deployment | [scaling-and-deployment.md#107-build-caching](scaling-and-deployment.md) |
| 108 | Dependency Hell | Scaling & Deployment | [scaling-and-deployment.md#108-dependency-hell](scaling-and-deployment.md) |
| 109 | Production Incidents | Observability & SRE | [observability-and-sre.md#109-production-incidents](observability-and-sre.md) |
| 110 | On-Call | Observability & SRE | [observability-and-sre.md#110-on-call](observability-and-sre.md) |
| 111 | Postmortems | Observability & SRE | [observability-and-sre.md#111-postmortems-blameless-postmortems](observability-and-sre.md) |

