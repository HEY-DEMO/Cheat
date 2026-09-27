# 🛡️ SkillSpector

> **Security scanner for AI agent skills.** Detect vulnerabilities, malicious patterns, and security risks before installing agent skills into coding environments like Claude Code, Codex CLI, Gemini CLI, and OpenCode.

[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://www.apache.org/licenses/LICENSE-2.0)
[![GitHub Stars](https://img.shields.io/github/stars/nvidia/skillspector?style=social)](https://github.com/nvidia/skillspector)
[![Upstream Repository](https://img.shields.io/badge/upstream-nvidia%2Fskillspector-76b900.svg)](https://github.com/nvidia/skillspector)

---

## 🚀 Overview

AI agent skills execute with implicit trust and broad filesystem or tool execution privileges. In empirical security research across 31,000+ skills:
- **26.1%** of skills contain latent security vulnerabilities
- **5.2%** demonstrate likely malicious intent (exfiltration, prompt injection, privilege escalation)

**SkillSpector** answers the critical question: *"Is this skill safe to install?"*

It is maintained by NVIDIA and serves as the core scanning engine of the [NVIDIA Verified Skills pipeline](https://docs.nvidia.com/skills/), which scans, evaluates, and cryptographically signs skills before publication to the NVIDIA skills catalog.

---

## ⚡ Key Features

- **Multi-Format Ingestion**: Scans Git repositories, raw URLs, `.zip` archives, local directories, or standalone `SKILL.md` / markdown instructions.
- **71 Vulnerability Patterns across 17 Categories**:
  - Prompt injection & jailbreak vectors
  - Data exfiltration & covert egress channels
  - Privilege escalation & environment manipulation
  - Supply-chain dependency risks
  - Excessive agency & unauthorized sub-task spawning
  - Output handling & unsanitized markdown / code rendering
  - System prompt / configuration leakage
  - Agent memory & context poisoning
  - Tool misuse & parameter hijacking
  - Anti-refusal & ethical guardrail bypass
  - Dangerous AST patterns & shell injection
  - Taint tracking from user inputs to sinks
  - YARA signatures for known malicious malware/scripts
  - MCP least privilege violations & tool poisoning
- **Hybrid Analysis Architecture**:
  1. *Static Analysis*: Lightning-fast AST parsing, regex signatures, and taint analysis.
  2. *Semantic LLM Analysis*: Deep contextual reasoning using OpenAI, Anthropic, AWS Bedrock, Azure OpenAI, NVIDIA build, or local Ollama models.
- **Live CVE Lookup**: Integrates directly with [OSV.dev](https://osv.dev) for real-time CVE checking with offline fallbacks.
- **Baseline / False-Positive Suppression**: Capture acceptable findings into `.skillspector-baseline.yaml` so CI/CD gates only break on *new* regressions.
- **MCP Server Mode**: Run as an MCP tool (`scan_skill`) to enable coding agents to self-police and gate skill installations in real time.

---

## 📦 Installation & Setup

### Option 1: Fast Install via uv (Recommended)

```bash
# Production CLI
uv tool install git+https://github.com/NVIDIA/skillspector.git

# With MCP server support
uv tool install 'skillspector[mcp] @ git+https://github.com/NVIDIA/skillspector.git'
```

### Option 2: Clone & Build from Source

```bash
git clone https://github.com/NVIDIA/skillspector.git
cd skillspector

uv venv .venv && source .venv/bin/activate
make install
```

### Option 3: Docker (Zero Local Python Dependencies)

```bash
# Build the container
docker build -t skillspector .

# Mount and scan a local skill directory (static analysis)
docker run --rm -v "$PWD:/scan" skillspector scan ./my-skill/ --no-llm
```

---

## 🛠️ Usage & Commands

### Basic Scanning

```bash
# Scan a local skill directory
skillspector scan ./my-skill/

# Scan a single SKILL.md definition
skillspector scan ./SKILL.md

# Scan a remote Git repository directly
skillspector scan https://github.com/user/agent-skill

# Scan an archive file
skillspector scan ./my-skill.zip
```

### Output Formats

```bash
# Terminal output with formatted tables (default)
skillspector scan ./my-skill/

# JSON output for automated CI pipelines
skillspector scan ./my-skill/ --format json --output report.json

# Markdown output for documentation & PR comments
skillspector scan ./my-skill/ --format markdown --output report.md

# SARIF output for GitHub Code Scanning / IDE diagnostics
skillspector scan ./my-skill/ --format sarif --output report.sarif
```

### LLM Semantic Analysis Configuration

SkillSpector supports multiple inference backends via environment variables:

```bash
# 1. Anthropic Claude
export SKILLSPECTOR_PROVIDER=anthropic
export ANTHROPIC_API_KEY=sk-ant-...
skillspector scan ./my-skill/

# 2. OpenAI
export SKILLSPECTOR_PROVIDER=openai
export OPENAI_API_KEY=sk-...
skillspector scan ./my-skill/

# 3. Local Ollama (No API Key Required)
export SKILLSPECTOR_PROVIDER=ollama
export SKILLSPECTOR_MODEL=llama3.1:8b
skillspector scan ./my-skill/

# 4. Skip LLM analysis (pure static scanning)
skillspector scan ./my-skill/ --no-llm
```

### False-Positive Baselines

```bash
# Create baseline of existing accepted findings
skillspector baseline ./my-skill/ -o .skillspector-baseline.yaml

# Scan against baseline — only newly introduced issues trigger warnings
skillspector scan ./my-skill/ --baseline .skillspector-baseline.yaml
```

### Running as an MCP Server

Integrate SkillSpector into Claude Code, Cursor, or Gemini CLI as an automated guardrail:

```bash
# Local stdio transport
skillspector mcp

# Streamable HTTP/SSE transport
skillspector mcp --transport http --host 127.0.0.1 --port 8000
```

Exposed MCP Tool:
- `scan_skill(target, use_llm=true, output_format="json")`: Evaluates the target and returns `risk_score` (0–100), `severity`, `safe_to_install` boolean, and actionable findings.

---

## 🔗 Official Links

- **GitHub Repository**: [nvidia/skillspector](https://github.com/nvidia/skillspector)
- **NVIDIA Verified Skills**: [docs.nvidia.com/skills](https://docs.nvidia.com/skills/)
- **Upstream Catalog**: [NVIDIA Skills Catalog](https://github.com/NVIDIA/skills)
