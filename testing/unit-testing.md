<![CDATA[# Unit Testing

> **Category**: `testing` · **Last Updated**: `2026-09-21` · **Difficulty**: `Beginner`

---

## TL;DR

Unit tests verify individual functions/methods in isolation. They should be fast, deterministic, and independent. Follow the Arrange-Act-Assert pattern.

---

## 🔑 Principles

| Principle         | Details                                                 |
|-------------------|---------------------------------------------------------|
| AAA Pattern       | **Arrange** setup → **Act** execute → **Assert** verify |
| One assert/test   | Each test should verify one behavior                    |
| No side effects   | Tests should be independent and order-agnostic          |
| Mock externals    | Isolate from DB, network, file system                   |
| Fast feedback     | Unit test suite should run in seconds, not minutes      |

---

## 💻 Code Example (Python — pytest)

```python
def add(a: int, b: int) -> int:
    return a + b

def test_add_positive_numbers():
    # Arrange
    a, b = 2, 3
    # Act
    result = add(a, b)
    # Assert
    assert result == 5

def test_add_negative_numbers():
    assert add(-1, -2) == -3
```

---

*← Back to [Testing](./README.md) · [Root Index](../README.md)*
]]>
