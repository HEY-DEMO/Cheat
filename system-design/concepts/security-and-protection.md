# Security & Protection

> **Domain**: Application Security, Cryptography, Access Governance, Threat Mitigation  
> **Index Numbers**: 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80

---

## 67. Secrets Management

### What
A centralized, secure system and operational practice for storing, accessing, distributing, auditing, and rotating sensitive application credentials (API tokens, database passwords, encryption keys, private SSH keys, TLS certificates) without hardcoding them in source code or plain environment files.

### Why
- Prevents credential leaks in git repositories, container images, build logs, and environment variables.
- Enables automated credential rotation without requiring application restarts or code deployments.

### Where We Use Them
- HashiCorp Vault, AWS Secrets Manager, GCP Secret Manager, Azure Key Vault, Doppler.
- Injecting short-lived, dynamic credentials directly into Kubernetes pods at runtime.

---

## 68. IAM (Identity and Access Management)

### What
A security framework and control plane of policies and technologies that ensures the right individuals and autonomous compute entities (services, pods, VMs) have the appropriate, verified access to technology resources based on Role-Based Access Control (RBAC) or Attribute-Based Access Control (ABAC).

### Why
- Enforces the **Principle of Least Privilege (PoLP)**: granting only the minimum permissions required to perform an authorized task.
- Prevents lateral movement across infrastructure if a single service is compromised.

### Where We Use Them
- Cloud provider IAM (AWS IAM roles, GCP IAM policies), Okta, Keycloak, Auth0.
- Kubernetes RBAC (`Roles`, `ClusterRoles`, `RoleBindings`, `ServiceAccounts`).

---

## 69. OAuth (Open Authorization)

### What
An open standard authorization protocol (OAuth 2.0 / 2.1) that allows third-party applications to obtain limited access to an HTTP service on behalf of a resource owner without exposing the user's password or credentials, using scoped access tokens.

### Why
- Users never share their primary credentials with third-party software.
- Allows granular access scoping (e.g., read-only access to user email without granting access to drive files) and instantaneous token revocation.

### Where We Use Them
- "Sign in with Google / GitHub / Apple" login flows.
- Public developer APIs (GitHub API, Slack API, Spotify API access tokens).

---

## 70. JWT Rotation (JSON Web Token Rotation)

### What
A security design pattern for stateless token-based authentication where clients are issued short-lived Access Tokens (e.g., expiring in 15 minutes) alongside long-lived, one-time-use Refresh Tokens stored securely. When the access token expires, the client exchanges the refresh token for a brand new access token and a brand new refresh token, invalidating the old one.

### Why
- Mitigates the risk of token theft: an intercepted access token expires quickly.
- Detects token replay attacks: if a stolen refresh token is used after already being rotated, the auth server detects the reuse anomaly, revokes the entire token family, and forces re-authentication.

### Where We Use Them
- Single Page Applications (SPAs), mobile apps, stateless microservices architectures.

---

## 71. TLS (Transport Layer Security)

### What
A cryptographic protocol operating above the transport layer (TCP) that provides end-to-end data encryption, server authentication (via X.509 digital certificates), and data integrity checking across computer networks (the underlying security protocol of HTTPS).

### Why
- Protects network communication against **Man-in-the-Middle (MitM)** attacks, packet sniffing, and payload tampering by untrusted intermediate network nodes.

### Where We Use Them
- HTTPS web browsing (TLS 1.2 and modern TLS 1.3).
- **Mutual TLS (mTLS)**: Enforcing bidirectional identity authentication between microservices inside service meshes (Istio, Linkerd).

---

## 72. Encryption at Rest

### What
The cryptographic protection of data stored persistently on physical disks, database tables, block storage volumes, object stores, and backup tapes, ensuring data cannot be read if the physical media is stolen or improperly accessed.

### Why
- Protects sensitive data against physical disk theft, unauthorized filesystem access, and snapshot leaks.
- Mandatory for regulatory compliance (PCI-DSS, HIPAA, GDPR, SOC2).

### Where We Use Them
- AWS KMS / AES-256 encrypted Amazon S3 buckets, AWS EBS volume encryption.
- Database Transparent Data Encryption (TDE) in PostgreSQL, MySQL, and Microsoft SQL Server.

---

## 73. Encryption in Transit

### What
The cryptographic encryption of data while it is traveling over a network between clients and servers, or internally between backend microservices, ensuring payloads remain confidential and tamper-proof while in flight.

### Why
- Prevents eavesdropping, packet interception, and session hijacking over public Wi-Fi, public internet backbones, and shared cloud VPCs.

### Where We Use Them
- TLS/HTTPS connections, IPsec VPN tunnels, SSH connections, internal service mesh mTLS.

---

## 74. WAF (Web Application Firewall)

### What
A specialized application-layer (Layer 7) security filter deployed in front of web applications that monitors, filters, and blocks malicious HTTP/HTTPS traffic matching known attack signatures and behavioral patterns.

### Why
- Standard network firewalls only inspect ports and IP addresses; WAFs inspect the full HTTP request payload, headers, cookies, and query parameters.
- Provides immediate "virtual patching" against zero-day vulnerabilities before engineering teams can rewrite application code.

### Where We Use Them
- AWS WAF, Cloudflare WAF, ModSecurity, Akamai.
- Blocking OWASP Top 10 exploits, SQL injection attempts, cross-site scripting strings, and bad bot scrapers.

---

## 75. DDoS Protection (Distributed Denial of Service)

### What
A suite of network infrastructure, scrubbing centers, and traffic routing defenses designed to detect, absorb, and mitigate malicious, high-volume distributed traffic floods aimed at exhausting bandwidth, network sockets, or server compute capacity.

### Why
- DDoS attacks can saturate network pipelines with hundreds of gigabits per second, causing complete global outages and massive unexpected cloud bandwidth bills.

### Where We Use Them
- Cloudflare, AWS Shield (Standard & Advanced), Akamai Prolexic.
- Defending against Layer 3/4 volumetric floods (SYN floods, UDP amplification) and Layer 7 application floods (HTTP GET/POST floods).

---

## 76. CORS (Cross-Origin Resource Sharing)

### What
A browser-enforced security mechanism based on HTTP headers that allows or restricts a web page from one origin (domain, protocol, or port) to make asynchronous `fetch` or `XMLHttpRequest` calls to an API hosted on a completely different origin.

### Why
- Enforces the browser's **Same-Origin Policy (SOP)**, preventing malicious websites from silently executing authenticated API calls against your backend using the victim's ambient browser cookies.

### Where We Use Them
- API server HTTP response headers: `Access-Control-Allow-Origin: https://app.example.com`, `Access-Control-Allow-Methods: GET, POST, OPTIONS`, `Access-Control-Allow-Headers: Authorization, Content-Type`.
- Handling HTTP `OPTIONS` preflight requests.

---

## 77. CSRF (Cross-Site Request Forgery)

### What
A web security vulnerability where an attacker tricks an authenticated user's browser into executing an unwanted, malicious action on a trusted application where the user is currently authenticated, exploiting the browser's automatic inclusion of session cookies with every request.

### Why
- Can allow attackers to silently change user emails, transfer funds, or purchase items without the user's knowledge simply by having the user visit a malicious webpage.

### Where We Use Them
- **Mitigations**:
  - `SameSite=Strict` or `SameSite=Lax` cookie attributes.
  - **Anti-CSRF Tokens**: Cryptographic, unpredictable tokens embedded in forms or custom request headers (`X-CSRF-Token`) that third-party sites cannot read or guess.

---

## 78. SQL Injection (SQLi)

### What
A code injection technique where an attacker inserts or manipulates untrusted input containing malicious SQL fragments that are concatenated directly into database queries, causing the database to execute arbitrary SQL commands.

### Why
- One of the most destructive web vulnerabilities: can lead to unauthorized data exfiltration, complete database destruction (`DROP TABLE`), and administrative account takeover.

### Where We Use Them
- **Mitigation**:
  - Never concatenate raw user input into SQL strings.
  - Use **Parameterized Queries / Prepared Statements** (`SELECT * FROM users WHERE email = ?`) where user input is treated strictly as data, never executable code.
  - Modern ORMs (Prisma, Hibernate, SQLAlchemy) parameterize queries by default.

---

## 79. XSS (Cross-Site Scripting)

### What
A security vulnerability where an application includes unvalidated or unescaped user input inside a web page returned to client browsers, allowing attackers to inject and execute malicious client-side JavaScript in the context of the victim's browser session.

### Why
- Enables attackers to steal session cookies, hijack user sessions, log keystrokes, and redirect users to phishing sites.

### Where We Use Them
- **Types**: Stored XSS (persistent in DB), Reflected XSS (immediate in URL parameter), DOM-based XSS.
- **Mitigation**: Context-aware output encoding/escaping (HTML, JS, CSS escaping), using modern reactive frontend frameworks (React, Angular, Vue automatically escape JSX/templates), enforcing strict **Content Security Policy (CSP)** headers, and storing auth tokens in `HttpOnly` cookies.

---

## 80. SSRF (Server-Side Request Forgery)

### What
A security exploit where an attacker abuses application functionality to force the backend server to make unauthorized HTTP or TCP requests to arbitrary destinations chosen by the attacker, targeting internal private network services or cloud metadata endpoints.

### Why
- The backend server has network access to internal VPC resources, internal microservices, and cloud metadata APIs (`http://169.254.169.254`) that are completely blocked from the public internet.
- Attackers use SSRF to steal cloud IAM instance credentials, inspect internal databases, and scan private networks.

### Where We Use Them
- Feature vectors: Webhook delivery URLs, image URL downloaders, PDF generation from URL.
- **Mitigations**: Strict URL allowlisting, blocking private IP ranges (RFC 1918 addresses: `10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`, `127.0.0.1`), blocking cloud metadata IP (`169.254.169.254`), and using AWS IMDSv2 (session token required).
