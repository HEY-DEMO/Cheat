# Concurrency & Compute

> **Domain**: Concurrency Control, Synchronization, Memory Management, Serverless Execution  
> **Index Numbers**: 36, 37, 38, 39, 40, 41, 42, 43, 89, 90

---

## 36. Optimistic Locking

### What
A concurrency control strategy that assumes conflicting updates rarely happen. Records are read without locking. When updating, the application checks whether another transaction modified the row in the meantime by comparing a `version` number or `updated_at` timestamp in the `UPDATE` statement (e.g., `WHERE id = 1 AND version = 5`). If the version changed, the transaction aborts and retries.

### Why
- Avoids expensive database read locks, maximizing read throughput and concurrency in high-volume systems.
- Prevents the **lost update problem** in multi-user environments without holding open database locks.

### Where We Use Them
- E-commerce cart updates, web form submissions, document editing with low write contention.
- Supported natively by ORMs (Hibernate `@Version`, JPA, TypeORM).

---

## 37. Pessimistic Locking

### What
A concurrency control strategy that assumes conflicting writes will happen frequently. The database explicitly acquires an exclusive row-level or table-level lock on the target record the moment it is read (e.g., `SELECT ... FOR UPDATE`), blocking any other transaction from reading with lock or modifying the record until the holding transaction commits or rolls back.

### Why
- Guarantees strict data integrity when write contention is high, preventing race conditions before they can occur.
- Eliminates the need for application-side retry loops.

### Where We Use Them
- Financial balance deductions (e.g., bank withdrawals, ATM debit transactions).
- Flash sales and ticketing platforms (booking the last remaining concert ticket or airline seat).

---

## 38. Distributed Locks

### What
A synchronization mechanism that ensures mutually exclusive execution of a critical code section across multiple independent application processes or separate physical servers across a network.

### Why
- In-memory language locks (`synchronized`, `threading.Lock`, `sync.Mutex`) only work within a single process or single JVM.
- In distributed microservices, multiple servers running background schedulers or order processors need to guarantee that only one node processes a given task at any moment.

### Where We Use Them
- Preventing duplicate batch payouts, single-runner cron executions across Kubernetes pods.
- Technologies: **Redis Redlock** algorithm, **Apache ZooKeeper** ephemeral sequential znodes, **etcd** lease-backed locks, AWS DynamoDB conditional writes.

---

## 39. Race Conditions

### What
A software flaw where the final outcome of a system or the state of shared data depends on the unpredictable order or timing of concurrent execution threads, asynchronous processes, or network events.

### Why
- Causes unpredictable, hard-to-reproduce data corruption, negative account balances, duplicate resource allocations, and critical security vulnerabilities.
- Uncovered primarily under heavy concurrent production traffic rather than single-threaded unit tests.

### Where We Use Them
- **Check-Then-Act Flaw**: Checking if an inventory item has quantity > 0 before deducting it; two concurrent requests both see quantity = 1 and both deduct, leaving quantity = -1.
- Mitigated via: Mutexes, atomic database operations (`UPDATE inventory SET count = count - 1 WHERE id = 1 AND count > 0`), database locks, or distributed locks.

---

## 40. Deadlocks

### What
A permanent stall condition where two or more concurrent processes or transactions are unable to proceed because each holds a lock on a resource that the other process requires, forming a circular wait dependency.

### Why
- Freezes application worker threads, holds database locks indefinitely, and exhausts connection pools, eventually bringing down service availability.

### Where We Use Them
- **Detection & Resolution**: Modern RDBMS (PostgreSQL, MySQL InnoDB) continuously run deadlock detection cycles, automatically killing and rolling back the younger transaction (`Deadlock found when trying to get lock; try restarting transaction`).
- **Prevention**: Enforce global lock ordering (always acquire locks on resources in strictly ascending alphabetical or numerical order across all transactions), keep transactions short, and use explicit statement timeouts.

---

## 41. Memory Leaks

### What
A condition where an application continuously allocates memory from the heap for objects, buffers, or connections but fails to release or deallocate them when they are no longer needed, causing system memory consumption to grow unbounded over time.

### Why
- Progressively degrades system performance due to severe Garbage Collection pressure and CPU thrashing.
- Inevitably results in an **Out-Of-Memory (OOM)** crash or Kubernetes OOMKilled pod eviction.

### Where We Use Them
- Common causes: Forgotten event listeners in frontends, unclosed database/file streams, growing static collections/caches without eviction policies, circular references in unmanaged runtimes.
- Debugged via: Heap dump analyzers (Eclipse Memory Analyzer MAT, Chrome DevTools memory profiler, Go `pprof`, Valgrind).

---

## 42. Garbage Collection (GC)

### What
An automatic memory management subsystem embedded in runtime environments (Java JVM, Go, Node.js V8, Python, .NET CLR) that tracks object references on the heap, detects memory that is no longer reachable by the application, and reclaims that memory for future allocations.

### Why
- Protects developers from manual memory management bugs (dangling pointers, double frees, manual buffer overflows).
- Requires careful tuning to minimize **Stop-The-World (STW)** pauses that spike application p99 latency.

### Where We Use Them
- Generational GC algorithms (JVM ZGC, Shenandoah, G1GC for low-latency systems; Go non-generational concurrent tri-color mark-sweep collector).
- High-throughput low-latency microservices, gaming servers, real-time trading engines.

---

## 43. Thread Safety

### What
A property of code (functions, objects, data structures) that guarantees correct execution and preserves shared data invariants when accessed concurrently by multiple execution threads without additional synchronization by the caller.

### Why
- Multi-threaded runtimes share the same process memory space.
- Non-thread-safe modifications of shared memory produce memory corruption, dirty reads, and segmentation faults.

### Where We Use Them
- Using immutable data structures (read-only objects).
- Synchronization primitives: Mutexes, Read-Write Locks (`RWMutex`), Semaphore, Atomic primitives (`AtomicInteger`, Compare-And-Swap - CAS).
- Thread-safe collections: Java `ConcurrentHashMap`, Go `sync.Map`.

---

## 89. Cold Starts

### What
The initialization latency delay experienced by a serverless function (AWS Lambda, Google Cloud Functions, Azure Functions) or container when handling an incoming request that requires spinning up a new container instance, pulling runtime layers, initializing the language runtime (JVM/Node/Python), and executing global setup code.

### Why
- Can add hundreds of milliseconds to several seconds of unexpected latency to end-user API requests.
- Directly impairs p99 latency SLAs on low-traffic endpoints or during sudden auto-scaling events.

### Where We Use Them
- Addressed using: AWS Lambda Provisioned Concurrency, choosing lightweight runtimes (Go, Rust, Node.js over heavy Spring Boot JVM), optimizing imports, connection pooling persistence outside function handler bodies.

---

## 90. Serverless Limits

### What
The architectural and operational constraints imposed by serverless cloud platforms on function execution, including maximum execution duration (e.g., AWS Lambda 15-minute timeout), payload size (e.g., 6MB synchronous request limit), ephemeral disk space (`/tmp`), and concurrency quotas per account.

### Why
- Serverless architecture is optimized for stateless, short-lived, event-driven compute; attempting to run long-running batch jobs or massive streaming transfers directly violates these design boundaries.
- Exceeding quotas triggers HTTP 429 throttling errors.

### Where We Use Them
- Designing serverless pipelines: Handing off long jobs to AWS Step Functions or AWS ECS Fargate containers; using pre-signed S3 URLs for large file uploads rather than passing payloads through API Gateway and Lambda.
