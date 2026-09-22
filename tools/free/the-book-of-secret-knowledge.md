# The Book of Secret Knowledge

> **Category**: `tools/free` · **Last Updated**: `2026-09-21` · **Difficulty**: `Intermediate`

---

## TL;DR

*The Book of Secret Knowledge* is an open-source handbook and reference collection (175k+ stars) curating the most powerful CLI tools, network diagnostics, security audit utilities, container managers, and battle-tested shell one-liners for DevOps engineers, sysadmins, and security researchers.

---

## 📋 Overview

- **What**: An organized encyclopedia of high-utility command-line tools, network analyzers, security scanners, and shell one-liners maintained by [trimstray](https://github.com/trimstray).
- **Why**: Modern infrastructure requires jumping across networking, system diagnostics, container orchestration, and security hardening. Finding the most modern, optimized CLI tool or exact one-liner saves hours of troubleshooting.
- **When**: Incident response, server configuration, network debugging, security auditing, container profiling, and terminal optimization.

---

## 🔑 Modern CLI Tool Upgrades

Replace legacy Unix utilities with modern, high-speed, and human-friendly alternatives:

| Legacy Tool | Modern Alternative | Key Advantage | Command / Package |
|---|---|---|---|
| `cat` | **bat** | Syntax highlighting, Git gutter diffs, paging | `bat filename.js` |
| `ls` | **eza** (formerly exa) | Tree view, git status, file icons, human dates | `eza -la --git` |
| `find` | **fd** | 5-10x faster, regex by default, ignores `.gitignore` | `fd "\.ts$"` |
| `grep` | **ripgrep (`rg`)** | Blazing fast, honors `.gitignore`, unicode support | `rg "pattern" src/` |
| `top` | **btop / htop** | Visual CPU/memory graphs, disk I/O, process killing | `btop` |
| `du` | **ncdu / dust** | Interactive terminal disk usage explorer | `ncdu /var/log` |
| `curl` | **HTTPie / curlie** | Colorized JSON formatting, intuitive flags | `http GET api.com/users` |
| `ping` / `traceroute` | **mtr** | Real-time interactive ping + traceroute combined | `mtr 1.1.1.1` |
| `docker ps` | **lazydocker / ctop** | Terminal UI for container logs, metrics, and exec | `lazydocker` |
| `kubectl` | **k9s** | Full-screen interactive terminal Kubernetes dashboard | `k9s` |

---

## 🌐 Network & Security Diagnostics

### 1. Port & Network Scanning
- **`nmap`**: Comprehensive network discovery, service fingerprinting, and vulnerability scanning.
  ```bash
  # Scan top 1000 ports, service versions, and OS detection
  nmap -sV -sC -O target.com
  ```
- **`masscan`**: The fastest Internet port scanner; asynchronously scans entire subnets in seconds.
  ```bash
  masscan -p80,443 192.168.1.0/24 --rate=10000
  ```
- **`socat`**: Multipurpose relay for bidirectional byte streams (TCP, UDP, SSL, UNIX sockets).

### 2. Packet Analysis & Sniffing
- **`tcpdump`**: Command-line packet analyzer.
  ```bash
  # Capture HTTPS traffic on eth0 with ASCII/hex output
  tcpdump -nnSX -i eth0 port 443
  ```
- **`termshark`**: Terminal user interface for `tshark` (Wireshark inside your SSH terminal).
- **`ngrep`**: Regex pattern matching directly applied to network packets.
  ```bash
  ngrep -q -W byline "GET|POST" port 80
  ```

### 3. DNS Reconnaissance
- **`subfinder` / `amass`**: Fast subdomain enumeration combining DNS brute-forcing and OSINT scraping.
- **`dnstwist`**: Detects domain spoofing, typo-squatting, and phishing variations.

---

## 🐳 Containers & Kubernetes Power Tools

| Tool | Purpose | Typical Command |
|---|---|---|
| **`lazydocker`** | Visual TUI for Docker containers, images, volumes, and live logs. | `lazydocker` |
| **`ctop`** | Top-like real-time metric viewer for multiple containers. | `ctop` |
| **`k9s`** | Terminal-based UI to interact, tail logs, and exec into Kubernetes clusters. | `k9s` |
| **`dive`** | Inspects Docker image layers and identifies wasted space. | `dive myimage:latest` |
| **`trivy`** | Vulnerability scanner for container images, file systems, and Git repos. | `trivy image myimage:latest` |

---

## ⚡ Battle-Tested Shell One-Liners

### 1. Check SSL Certificate Expiry
Inspect SSL certificate validity directly from your terminal without opening a browser:

```bash
echo | openssl s_client -servername example.com -connect example.com:443 2>/dev/null | openssl x509 -noout -dates
```

### 2. Check Listening Ports and Owning Processes
Identify what service is occupying a port:

```bash
# macOS and Linux (ss / lsof)
ss -tulpn | grep :8080
# Or using lsof:
lsof -i :8080
```

### 3. Top 10 Memory-Consuming Processes
Find rogue memory consumers instantly:

```bash
ps aux --sort=-%mem | awk 'NR<=10{print $1, $2, $4"%", $11}'
```

### 4. Visual HTTP Request Timing with `httpstat`
Benchmark DNS lookup, TCP handshake, TLS negotiation, and TTFB:

```bash
curl -s -w '\nLookup time:\t%{time_namelookup}\nConnect time:\t%{time_connect}\nTLS handshake:\t%{time_appconnect}\nPre-transfer:\t%{time_pretransfer}\nStart transfer:\t%{time_starttransfer}\nTotal time:\t%{time_total}\n' -o /dev/null https://example.com
```

### 5. Find Files Larger than 100MB
Locate large files eating up disk space:

```bash
find / -type f -size +100M -exec ls -lh {} + 2>/dev/null | awk '{print $5, $9}'
```

### 6. Zero-Dependency HTTP File Server
Serve current directory over HTTP immediately:

```bash
python3 -m http.server 8000
```

---

## ⚠️ Anti-Patterns & Common Traps

| Trap | Risk | Recommended Best Practice |
|---|---|---|
| **Running `masscan` carelessly** | Flooding networks with high SYN rates triggers IDS alerts and ISP disconnects. | Set conservative `--rate` limits and scan only authorized subnets. |
| **Hardcoding cleartext secrets in bash history** | `HISTFILE` retains sensitive tokens, API keys, and passwords. | Prepend sensitive commands with a space (` HISTCONTROL=ignorespace`) or use env files. |
| **Ignoring `.gitignore` in large searches** | Legacy `grep -r` wastes minutes crawling `node_modules` or `.git`. | Default to `ripgrep` (`rg`) or `fd` which respect ignore rules out-of-the-box. |
| **Unrestricted `tcpdump` captures** | Generating multi-gigabyte PCAP files fills root partitions rapidly. | Always constrain capture limits using `-c <count>` and specific port filters. |

---

## 🔗 Related Resources

- **Full Upstream Handbook**: [github_repos/the-book-of-secret-knowledge.md](../../github_repos/developer-tools/the-book-of-secret-knowledge.md)
- **GitHub Repository**: [trimstray/the-book-of-secret-knowledge](https://github.com/trimstray/the-book-of-secret-knowledge)
- **Related Guides**: [DevOps Docker Guide](../../devops/docker.md) · [OWASP Top 10](../../security/owasp-top-10.md)

---

*← Back to [Free Tools](./README.md) · [Root Index](../../README.md)*
