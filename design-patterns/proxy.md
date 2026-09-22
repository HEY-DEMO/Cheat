# Proxy Pattern

> **Category**: `design-patterns / structural` · **Last Updated**: `2026-09-21` · **Difficulty**: `Intermediate`

---

## TL;DR

The Proxy pattern provides a **surrogate or placeholder** for another object to **control access** to it. The proxy has the same interface as the real object, so the client can't tell the difference.

---

## 📋 Overview

- **What**: A structural pattern that provides a substitute object that controls access to the original object, allowing you to perform something before or after the request reaches the original.
- **Why**: Adds a level of indirection for lazy loading, access control, logging, caching, or remote access.
- **When**: When you need lazy initialization (virtual proxy), access control (protection proxy), logging (logging proxy), or caching (caching proxy).

---

## 🔑 Key Concepts

| Proxy Type         | Description                                                   |
|--------------------|---------------------------------------------------------------|
| Virtual Proxy      | Delays expensive object creation until actually needed         |
| Protection Proxy   | Controls access based on permissions/roles                     |
| Remote Proxy       | Represents an object in a different address space (RPC/API)   |
| Logging Proxy      | Records all operations for debugging/auditing                  |
| Caching Proxy      | Caches results of expensive operations                         |

---

## 💻 Code Examples

### Python — Virtual Proxy (Lazy Loading)

```python
from abc import ABC, abstractmethod

class Image(ABC):
    @abstractmethod
    def display(self) -> None: ...

class RealImage(Image):
    def __init__(self, filename: str):
        self.filename = filename
        self._load_from_disk()  # Expensive operation
    
    def _load_from_disk(self):
        print(f"⏳ Loading {self.filename} from disk...")
    
    def display(self):
        print(f"🖼️ Displaying {self.filename}")

class ProxyImage(Image):
    def __init__(self, filename: str):
        self.filename = filename
        self._real_image = None  # Deferred creation
    
    def display(self):
        if self._real_image is None:
            self._real_image = RealImage(self.filename)
        self._real_image.display()

# Usage
gallery = [ProxyImage(f"photo_{i}.jpg") for i in range(100)]
# No images loaded yet! Only loaded when displayed:
gallery[0].display()   # ⏳ Loading... 🖼️ Displaying
gallery[0].display()   # 🖼️ Displaying (cached, no reload)
```

---

## 🌍 Real-World Use Cases

| Use Case                     | Description                                                     |
|------------------------------|-----------------------------------------------------------------|
| **Lazy-loaded Images**       | Web pages load image placeholders; real images load on scroll    |
| **ORM Lazy Relations**       | SQLAlchemy/Hibernate load related objects only when accessed     |
| **API Rate Limiting**        | Proxy counts and throttles calls to a downstream service        |
| **Access Control**           | Check user permissions before allowing resource access           |
| **Caching Proxies**          | CDN caches responses; serves cached copy if available           |

---

## 🔗 Related Topics

- [Decorator](decorator.md) — Similar structure but different intent (adds vs. controls)
- [Adapter](adapter.md) — Changes interface; Proxy keeps the same interface
- [Facade](facade.md) — Simplifies a subsystem; Proxy wraps one object
- [Flyweight](flyweight.md) — Shares objects; Proxy manages access to them

---

## 📚 References

- [GeeksforGeeks — Proxy Design Pattern](https://www.geeksforgeeks.org/proxy-design-pattern/)
- [Refactoring Guru — Proxy](https://refactoring.guru/design-patterns/proxy)

---

*← Back to [Design Patterns](./README.md) · [Root Index](../README.md)*
