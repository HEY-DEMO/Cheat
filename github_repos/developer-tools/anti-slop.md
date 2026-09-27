> 🔗 **GitHub Repository**: [dmmulroy/anti-slop](https://github.com/dmmulroy/anti-slop)

---

# 🧹 anti-slop

> **Opinionated Oxlint rules against low-evidence TypeScript and JavaScript patterns.** Designed to be vendored directly into codebases to eliminate artificial types, unnecessary spreads, fragile runtime assertions, and redundant iterations.

[![skills.sh](https://skills.sh/b/dmmulroy/anti-slop)](https://skills.sh/dmmulroy/anti-slop)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/dmmulroy/anti-slop?style=social)](https://github.com/dmmulroy/anti-slop)
[![Upstream Repository](https://img.shields.io/badge/upstream-dmmulroy%2Fanti--slop-crimson.svg)](https://github.com/dmmulroy/anti-slop)

---

## 🚀 Overview

**anti-slop** is a high-signal linting plugin built for [Oxlint](https://oxc.rs) that catches and eliminates low-quality patterns commonly introduced by developers and AI code generators. Rather than serving as an immutable npm dependency, anti-slop is designed to be **vendored** directly into your repository where teams can audit, customize, and evolve the rules to match their specific architecture.

It includes an automated agent skill that vendors the plugin, resolves Oxlint dependencies, registers the plugin into `oxlint.config.ts`, and enables baseline rules with three-way merge update support.

---

## ⚡ Core Rules Reference

### Generic Quality & Type Discipline Rules

| Rule | Description & Rationale |
|---|---|
| `no-array-filter-map` | Rejects adjacent eager `.filter().map()` loops in favor of single-pass reducers, `flatMap`, or lazy iterator pipelines. |
| `no-reduce-accumulator-copy` | Rejects copying accumulators inside reducers (`{ ...acc, [key]: val }`), eliminating O(n²) memory allocations. |
| `no-chained-type-assertions` | Rejects nested `as` and angle-bracket assertions (`x as unknown as T`) that fabricate fake compiler evidence. |
| `no-conditional-empty-object-spread` | Forbids `{ ...(condition ? { a: 1 } : {}) }` patterns where omission is mistakenly conflated with undefined values. |
| `no-known-value-widening` | Rejects expressions flowing into overly broad targets (`unknown`, `object`, open records) when tighter types are available. |
| `no-module-mocking` | Rejects runtime module mocks (`vi.mock`, `jest.mock`) in favor of clear dependency injection and explicit seams. |
| `no-object-parameters` | Rejects bare `object` or generic record types on function inputs that obscure actual parameter requirements. |
| `no-reflect-apply` / `no-reflect-get` | Enforces standard direct function calls and property access rather than untyped reflection. |
| `no-runtime-typeof` | Requires explicit boundary parsers / schema validators instead of fragile ad-hoc `typeof` checks. |
| `require-safety-comment-for-type-assertion` | Mandates explanatory comments when type assertions are truly unavoidable. |

### Optional Effect Rules

For projects leveraging the [Effect-TS](https://effect.website) ecosystem, an optional rule group is included:
- `no-manual-effect-error-tag`
- `no-manual-tag-comparison`
- `prefer-effect-match`
- `no-service-constructor-imports`

---

## 📦 Installation & Setup

### Option 1: Automatic Vendoring via Agent Skill

```bash
# Add the installer skill to your agent
npx skills add dmmulroy/anti-slop --skill install-anti-slop
```

Then ask your AI coding assistant:
> *"Install and configure anti-slop in this repository."*

The skill copies the plugin into `tools/oxlint/anti-slop/`, resolves compatible `@oxlint/plugins`, wires `oxlint.config.ts`, and verifies your configuration.

### Option 2: Manual Local Installation

1. Copy the `src/` directory from the upstream repository into `tools/oxlint/anti-slop/`.
2. Install the matching plugin package:
   ```bash
   npm install -D @oxlint/plugins
   ```
3. Register the plugin in `oxlint.config.ts`:

```typescript
import { defineConfig } from "oxlint";

export default defineConfig({
  ignorePatterns: [
    ".agents/**",
    ".claude/**",
    ".cursor/**",
    "tools/oxlint/anti-slop/**"
  ],
  jsPlugins: [
    { name: "anti-slop", specifier: "./tools/oxlint/anti-slop/index.ts" }
  ],
  rules: {
    "oxc/no-accumulating-spread": "error",
    "anti-slop/no-array-filter-map": "error",
    "anti-slop/no-reduce-accumulator-copy": "error",
    "anti-slop/no-chained-type-assertions": "error",
    "anti-slop/no-conditional-empty-object-spread": "error",
    "anti-slop/no-known-value-widening": "error",
    "anti-slop/no-module-mocking": "error",
    "anti-slop/no-object-parameters": "error",
    "anti-slop/no-reflect-apply": "error",
    "anti-slop/no-reflect-get": "error",
    "anti-slop/no-runtime-typeof": "error",
    "anti-slop/require-readable-spacing": "error",
    "anti-slop/require-safety-comment-for-type-assertion": "error"
  }
});
```

---

## 🛠️ Updating Vendored Rules

When upstream introduces new rules or bugfixes, run:

```text
"Update anti-slop while preserving our local modifications."
```

The installer performs a three-way merge, keeping project-specific rule adjustments intact while importing upstream improvements.

---

## 🔗 Official Links

- **GitHub Repository**: [dmmulroy/anti-slop](https://github.com/dmmulroy/anti-slop)
- **Skills Directory Listing**: [skills.sh/dmmulroy/anti-slop](https://skills.sh/dmmulroy/anti-slop)
