# SQL Optimization

> **Category**: `databases` · **Last Updated**: `2026-09-21` · **Difficulty**: `Intermediate`

---

## TL;DR

Slow queries are usually caused by missing indexes, SELECT *, or N+1 patterns. Use EXPLAIN, index strategically, and fetch only what you need.

---

## 🔑 Quick Wins

| Problem                   | Fix                                             |
|---------------------------|--------------------------------------------------|
| Full table scans          | Add indexes on WHERE/JOIN columns                |
| `SELECT *`                | Select only needed columns                       |
| N+1 queries               | Use JOINs or batch fetching                      |
| Missing EXPLAIN analysis  | Run `EXPLAIN ANALYZE` before optimizing          |
| No connection pooling     | Use PgBouncer, HikariCP, etc.                    |

---

*← Back to [Databases](./README.md) · [Root Index](../README.md)*

