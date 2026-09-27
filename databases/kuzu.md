# 🦎 Kùzu Graph Database

> **Category**: databases · **Last Updated**: 2026-09-23 · **Difficulty**: Intermediate

---

## TL;DR

Kùzu is an ultra-fast, open-source, embedded in-process property graph database (the "DuckDB for graph data"). Built in C++, it supports openCypher queries, vectorized execution, columnar storage, and seamless integration with Python, Rust, Node.js, and PyTorch Geometric.

---

## 📋 Overview

- **What**: An in-process, serverless property graph database management system designed for fast analytical queries over graph-structured data.
- **Why**: Traditional client-server graph databases (e.g., Neo4j) introduce network latency, heavy memory footprints, and server setup overhead. Kùzu runs directly inside your application process with zero-copy data transfer.
- **When**: Building AI Agent knowledge graphs (RAG), code intelligence graphs, fraud detection networks, recommendation systems, or embedding graph analytics in Python/Rust applications.

---

## 🔑 Key Concepts

| Concept | Description |
|---|---|
| **Property Graph Model** | Data is modeled as nodes (entities) and relationships/edges (connections), both holding key-value properties. |
| **openCypher Support** | Standard graph query language using declarative patterns like MATCH (a)-[r]->(b) WHERE ... RETURN .... |
| **In-Process Architecture** | Runs inside your application memory space without a separate daemon server process. |
| **Vectorized Execution Engine** | Employs columnar storage and SIMD-friendly vector operations for high-throughput analytical workloads. |
| **Parquet / Arrow Interop** | Ingests CSV, Parquet, and Pandas/Polars DataFrames directly via zero-copy arrow integration. |
| **Recursive Path Queries** | Efficient variable-length path traversal queries (e.g., shortest paths, multi-hop reachability). |

---

## 📐 Syntax / Visual Diagram

`mermaid
graph LR
    subgraph Kùzu Embedded Engine
        A[Node Table: User] -- ":FOLLOWS" --> B[Node Table: User]
        A -- ":WRITES" --> C[Node Table: Post]
        B -- ":LIKES" --> C
    end
    D[Python / PyArrow / Rust] <-->|Zero-Copy / In-Memory| Kùzu Embedded Engine
    E[Parquet / CSV Data] -->|COPY FROM| Kùzu Embedded Engine
`

---

## 💻 Code Examples

### Basic Usage (Python)

`python
import kuzu

# 1. Initialize embedded database and connection
db = kuzu.Database("./kuzu_db")
conn = kuzu.Connection(db)

# 2. Define Node and Relationship Schemas
conn.execute("CREATE NODE TABLE Person(name STRING, age INT64, PRIMARY KEY (name))")
conn.execute("CREATE REL TABLE KNOWS(FROM Person TO Person, since INT64)")

# 3. Insert Data via Cypher
conn.execute("CREATE (:Person {name: 'Alice', age: 30})")
conn.execute("CREATE (:Person {name: 'Bob', age: 32})")
conn.execute("""
    MATCH (a:Person {name: 'Alice'}), (b:Person {name: 'Bob'})
    CREATE (a)-[:KNOWS {since: 2021}]->(b)
""")

# 4. Query Graph
response = conn.execute("""
    MATCH (a:Person)-[r:KNOWS]->(b:Person)
    RETURN a.name AS source, r.since AS since, b.name AS target
""")

while response.has_next():
    print(response.get_next())
`

### Advanced Querying & Interoperability

`python
import kuzu
import pandas as pd

db = kuzu.Database("./kuzu_analytics")
conn = kuzu.Connection(db)

# Ingest directly from Pandas DataFrame / Parquet
df_users = pd.DataFrame({
    "userId": ["U1", "U2", "U3"],
    "score": [98.5, 87.0, 94.2]
})

conn.execute("CREATE NODE TABLE User(userId STRING, score DOUBLE, PRIMARY KEY (userId))")
conn.execute("COPY User FROM df_users")

# Multi-hop Path Traversal Query
query = """
    MATCH (u1:User {userId: 'U1'})-[:FRIEND_OF*1..3]->(u2:User)
    WHERE u2.score > 90.0
    RETURN u2.userId, u2.score
"""
results = conn.execute(query).get_as_df()
print(results)
`

---

## ⚠️ Anti-Patterns

| ❌ Anti-Pattern | ✅ Better Approach |
|---|---|
| Single CREATE statements for bulk data loading | Use COPY FROM with CSV or Parquet files for 100x faster ingestion. |
| Running separate Neo4j container for embedded Python apps | Use embedded Kùzu to eliminate network IPC overhead and infrastructure ops. |
| Omitting Primary Key on Node Tables | Define explicit primary keys (PRIMARY KEY (id)) for quick node lookups and unique constraint enforcement. |
| Over-fetching large subgraphs into application memory | Filter paths early using Cypher WHERE clauses and project only required attributes. |

---

## 🌍 Real-World Use Case

**Scenario**: Building a Retrieval-Augmented Generation (RAG) Knowledge Graph for an AI Coding Agent.

**Problem**: Traditional vector databases miss relational structure (e.g., module imports, function calls, class inheritance), leading to incomplete context for complex code reasoning tasks.

**Solution**: Store code AST and import dependencies in a local Kùzu graph database embedded directly inside the AI agent process.

**Result**: Sub-millisecond graph traversals combined with vector search allow the agent to fetch relevant function definitions and their call graphs with zero network latency.

---

## 🔗 Related Topics

- [SQL Optimization](sql-optimization.md) — Query tuning and database performance strategies.
- [Codebase Memory MCP](../github_repos/ai-agents-skills/codebase-memory-mcp.md) — Persistent memory graphs for AI agents.

---

## 📚 References

- [Official Kùzu Documentation](https://kuzudb.github.io/docs/)
- [Kùzu GitHub Repository](https://github.com/kuzudb/kuzu)

---

*← Back to [Databases](./README.md) · [Root Index](../README.md)*
