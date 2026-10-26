> 🔗 **GitHub Repository**: [vxcontrol/pentagi](https://github.com/vxcontrol/pentagi)

---

# 🕵️ PentAGI

> **Autonomous multi-agent system for penetration testing and offensive security assessments.** PentAGI coordinates specialized AI agents (Recon, Developer, Executor) inside isolated Docker sandboxes to autonomously perform end-to-end security workflows from reconnaissance to structured vulnerability reporting.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Go Version](https://img.shields.io/badge/backend-Go%201.22+-00ADD8.svg?logo=go)](https://golang.org)
[![React Version](https://img.shields.io/badge/frontend-React%2018%20%2F%20TS-61DAFB.svg?logo=react)](https://react.dev)
[![Docker](https://img.shields.io/badge/sandbox-Docker%20Compose-2496ED.svg?logo=docker)](https://www.docker.com)
[![GitHub Stars](https://img.shields.io/github/stars/vxcontrol/pentagi?style=social)](https://github.com/vxcontrol/pentagi)
[![Upstream Repository](https://img.shields.io/badge/upstream-vxcontrol%2Fpentagi-blueviolet.svg)](https://github.com/vxcontrol/pentagi)

---

## 🚀 Overview

Traditional penetration testing requires manual execution of disparate CLI tools, manual chaining of exploits, and tedious note-taking. PentAGI modernizes this process by providing a **self-hosted, fully autonomous offensive security engine** powered by a team of collaborative AI agent specialists.

Unlike brittle single-prompt scripts, PentAGI operates through a hierarchical execution flow:
1. **Flow**: Receives high-level user security goals and scopes.
2. **Task**: Breaks engagement goals down into tactical milestones (e.g., DNS enumeration, service probing, web fuzzing).
3. **Subtask & Action**: Executes individual terminal commands safely inside isolated containerized environments, continuously ingesting outputs into a vector-backed memory system.

---

## ⚡ Key Architecture & Agents

```
                           ┌───────────────────────────┐
                           │      User / Web UI        │
                           │   (React + GraphQL Sub)   │
                           └─────────────┬─────────────┘
                                         │
                                         ▼
                           ┌───────────────────────────┐
                           │   Orchestrator Backend    │
                           │       (Go Engine)         │
                           └──────┬─────────────┬──────┘
                                  │             │
                ┌─────────────────┴─┐         ┌─┴────────────────┐
                │ Long-Term Memory  │         │ Observability    │
                │ PostgreSQL+Vector │         │ Langfuse/Metrics │
                └───────────────────┘         └──────────────────┘
                                  │
         ┌────────────────────────┼────────────────────────┐
         ▼                        ▼                        ▼
┌──────────────────┐    ┌──────────────────┐    ┌──────────────────┐
│ Researcher Agent │    │ Developer Agent  │    │  Executor Agent  │
│ Recon, OSINT,    │    │ Exploit Planning,│    │ Terminal Driving,│
│ CVE Matching     │    │ Script Crafting  │    │ Tool Execution   │
└────────┬─────────┘    └────────┬─────────┘    └────────┬─────────┘
         │                       │                       │
         └───────────────────────┼───────────────────────┘
                                 ▼
                ┌─────────────────────────────────┐
                │   Isolated Docker Sandbox Host  │
                │ Nmap · Metasploit · Sqlmap · etc│
                └─────────────────────────────────┘
```

### Specialized Agent Team

| Agent Role | Primary Focus | Capabilities & Tooling |
|---|---|---|
| **🎯 Orchestrator Agent** | Task planning & coordination | Deconstructs user objectives, maintains engagement state, schedules tasks, and balances token budget across models. |
| **🔍 Researcher Agent** | Reconnaissance & OSINT | Port scanning, DNS brute forcing, subdomain discovery, web crawling, CVE database querying, and target fingerprinting. |
| **💻 Developer Agent** | Strategy & payload authoring | Analyzes raw scan outputs, formulates multi-stage attack vectors, writes/adapts custom exploit scripts, and crafts validation tests. |
| **⚡ Executor Agent** | Sandboxed tool execution | Interacts directly with the isolated Docker container terminal, runs security utilities, handles timeouts, and parses stdout/stderr into structured signals. |

---

## 🛡️ Core Features

- **Strict Sandbox Isolation**: All terminal operations and network scans execute within self-contained Docker containers, protecting the host system and preventing unintended collateral damage.
- **20+ Built-in Security Tools**: Preloaded with essential assessment tools including `nmap`, `sqlmap`, `metasploit-framework`, `nikto`, `gobuster`, `ffuf`, `hydra`, `wpscan`, and `curlc/whois/dig`.
- **Vector-Backed Long-Term Memory**: Powered by PostgreSQL with `pgvector` to persist discovered assets, open ports, discovered credentials, and past successes across sessions.
- **Provider-Agnostic LLM Routing**: Seamlessly routes tasks between 10+ LLM backends (OpenAI, Anthropic Claude, DeepSeek, Google Gemini, Ollama, Groq, OpenRouter, and AWS Bedrock).
- **Real-Time Web Console**: Rich web interface displaying live terminal streaming, graphical asset topology maps, task progress trees, and downloadable PDF/Markdown assessment reports.
- **Human-in-the-Loop Mode**: Configurable confirmation gates allow security engineers to review and approve sensitive actions before execution.

---

## 📦 Installation & Setup

PentAGI is packaged for simple, reliable deployment using Docker Compose.

### Prerequisites

- [Docker Engine](https://docs.docker.com/engine/install/) (v24.0+)
- [Docker Compose](https://docs.docker.com/compose/) (v2.20+)
- LLM API key (OpenAI, Anthropic Claude, or local Ollama instance)

### 1. Clone & Prepare Directory

```bash
git clone https://github.com/vxcontrol/pentagi.git
cd pentagi

# Copy environment configuration template
cp .env.example .env
```

### 2. Configure Environment Variables

Edit `.env` to supply your LLM provider credentials and instance settings:

```ini
# Core Configuration
PORT=8443
APP_ENV=production
ADMIN_EMAIL=admin@pentagi.com
ADMIN_PASSWORD=change_this_secure_password

# Database Configuration
POSTGRES_DB=pentagi
POSTGRES_USER=pentagi
POSTGRES_PASSWORD=secure_postgres_secret
POSTGRES_HOST=postgres
POSTGRES_PORT=5432

# LLM Providers (Configure at least one)
OPENAI_API_KEY=sk-proj-...
ANTHROPIC_API_KEY=sk-ant-...
DEEPSEEK_API_KEY=sk-...

# Search & OSINT APIs (Optional but recommended)
TAVILY_API_KEY=tvly-...
SHODAN_API_KEY=...
```

### 3. Launch Services

```bash
# Pull images and start the complete stack in detached mode
docker compose up -d

# Verify all containers are healthy
docker compose ps
```

### 4. Access Web Console

Open your browser and navigate to:
```text
https://localhost:8443
```

- **Default Username**: `admin@pentagi.com`
- **Default Password**: Defined in your `.env` (defaults to `admin` if unchanged)

---

## 🛠️ Usage Workflows

### 1. Scope Definition & Target Onboarding

From the PentAGI Web Console:
1. Click **New Assessment**.
2. Specify the target domain or IP range (e.g., `testphp.vulnweb.com`).
3. Set operational constraints:
   - **Mode**: Reconnaissance Only | Vulnerability Assessment | Full Penetration Test.
   - **Execution Tier**: Fully Autonomous | Approval Required for Active Exploits.
   - **Rate Limits**: Max concurrent requests and scan speeds.

### 2. Example Natural Language Objectives

You can direct PentAGI using high-level objectives:

```text
"Perform an external attack-surface mapping on target staging.example.com.
Identify all exposed web services, detect outdated CMS versions, and test
for OWASP Top 10 injection vulnerabilities without altering database state."
```

```text
"Enumerate open ports on 192.168.10.0/24. Find unauthenticated API endpoints
and verify if any service is susceptible to known RCE vulnerabilities."
```

### 3. Monitoring & Live Interaction

- **Live Flow Graph**: Visualize the active hierarchy of Goals → Tasks → Subtasks.
- **Terminal Mirror**: Watch the Executor agent invoke tools like `nmap` and `ffuf` inside the sandbox with live colorized stdout/stderr streams.
- **Findings Drawer**: Review discovered assets, service versions, CVE matches, and CVSS scores in real time.

---

## ⚙️ Configuration Reference

| Environment Variable | Description | Default |
|---|---|---|
| `PORT` | HTTPS port for the web dashboard and GraphQL API | `8443` |
| `DEFAULT_LLM_PROVIDER` | Default engine (`openai`, `anthropic`, `ollama`) | `anthropic` |
| `DEFAULT_MODEL` | Default model identifier | `claude-3-5-sonnet-latest` |
| `SANDBOX_TIMEOUT_MINUTES` | Maximum run duration for a single subtask tool execution | `15` |
| `MAX_PARALLEL_TASKS` | Max concurrent agent tasks executed simultaneously | `4` |
| `LANGFUSE_PUBLIC_KEY` | Public key for optional Langfuse LLM observability | `""` |
| `LANGFUSE_SECRET_KEY` | Secret key for optional Langfuse LLM observability | `""` |

---

## 🔗 Official Links

- **GitHub Repository**: [vxcontrol/pentagi](https://github.com/vxcontrol/pentagi)
- **Documentation & Guides**: [pentagi.com](https://pentagi.com)
- **Organization**: [VXControl](https://github.com/vxcontrol)
