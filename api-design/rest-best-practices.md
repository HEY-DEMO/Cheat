# REST Best Practices

> **Category**: `api-design` · **Last Updated**: `2026-09-21` · **Difficulty**: `Intermediate`

---

## TL;DR

Use nouns for resources, HTTP verbs for actions, consistent error formats, pagination, and versioning from day one.

---

## 🔑 Principles

| Principle                    | Example                                     |
|------------------------------|---------------------------------------------|
| Use plural nouns             | `/users`, `/orders` (not `/getUser`)        |
| HTTP verbs = actions         | `GET /users`, `POST /users`                |
| Consistent error format      | `{ "error": { "code": 404, "message": "" } }` |
| Pagination                   | `?page=2&limit=20` or cursor-based         |
| Versioning                   | `/api/v1/users` or `Accept` header         |
| HATEOAS (optional)           | Include links to related resources          |

---

*← Back to [API Design](./README.md) · [Root Index](../README.md)*

