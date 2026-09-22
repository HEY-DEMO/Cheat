# Flyweight Pattern

> **Category**: `design-patterns / structural` · **Last Updated**: `2026-09-21` · **Difficulty**: `Advanced`

---

## TL;DR

The Flyweight pattern **reduces memory usage** by sharing as much data as possible among similar objects. It separates intrinsic (shared) state from extrinsic (unique) state.

---

## 📋 Overview

- **What**: A structural pattern that lets you fit more objects into available RAM by sharing common parts of state between multiple objects.
- **Why**: When an application creates millions of similar objects, each consuming memory — Flyweight shares the common data.
- **When**: Large numbers of similar objects, games (particles, tiles), text editors (character formatting), caching systems.

---

## 🔑 Key Concepts

| Concept          | Description                                                      |
|------------------|------------------------------------------------------------------|
| Intrinsic State  | Shared data that is constant across objects (stored in flyweight)|
| Extrinsic State  | Unique data that varies per context (passed by client)           |
| Flyweight Factory| Creates and manages flyweight objects, returning cached instances|

---

## 💻 Code Examples

### Python — Game Particle System

```python
class TreeType:
    """Flyweight — shared intrinsic state"""
    def __init__(self, name: str, color: str, texture: str):
        self.name = name
        self.color = color
        self.texture = texture  # Large texture data
    
    def draw(self, x: int, y: int):
        print(f"  Drawing {self.name} ({self.color}) at ({x}, {y})")

class TreeFactory:
    """Flyweight Factory — caches and reuses TreeType objects"""
    _cache: dict[str, TreeType] = {}
    
    @classmethod
    def get_tree_type(cls, name: str, color: str, texture: str) -> TreeType:
        key = f"{name}_{color}"
        if key not in cls._cache:
            cls._cache[key] = TreeType(name, color, texture)
            print(f"  [NEW] Created TreeType: {key}")
        return cls._cache[key]

class Tree:
    """Context — holds extrinsic state (position)"""
    def __init__(self, x: int, y: int, tree_type: TreeType):
        self.x = x
        self.y = y
        self.type = tree_type
    
    def draw(self):
        self.type.draw(self.x, self.y)

# Usage — 1 million trees, only a handful of TreeType objects
forest = []
for i in range(1000):
    tt = TreeFactory.get_tree_type("Oak", "green", "<huge_texture_data>")
    forest.append(Tree(i * 10, i * 5, tt))

print(f"Trees planted: {len(forest)}")
print(f"TreeType objects: {len(TreeFactory._cache)}")  # Just 1!
```

---

## 🌍 Real-World Use Cases

| Use Case                     | Description                                                     |
|------------------------------|-----------------------------------------------------------------|
| **Text Editors**             | Character glyphs share font/style; only position varies         |
| **Game Engines**             | Particle systems, tiles, bullets share sprites                   |
| **String Interning**         | Python/Java intern strings — same content → same object          |
| **Browser DOM**              | CSS classes shared across elements; position/content varies      |
| **GIS/Map Applications**     | Map icons shared; coordinates are extrinsic                      |

---

## 🔗 Related Topics

- [Singleton](singleton.md) — Flyweight Factory can be a Singleton
- [Facade](facade.md) — Can use Flyweight internally
- [Proxy](proxy.md) — Proxy manages access; Flyweight manages memory

---

## 📚 References

- [GeeksforGeeks — Flyweight Design Pattern](https://www.geeksforgeeks.org/flyweight-design-pattern/)
- [Refactoring Guru — Flyweight](https://refactoring.guru/design-patterns/flyweight)

---

*← Back to [Design Patterns](./README.md) · [Root Index](../README.md)*
