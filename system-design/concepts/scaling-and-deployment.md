# Scaling & Deployment Strategies

> **Domain**: Infrastructure Scaling, Container Orchestration, Deployment Workflows, High Availability  
> **Index Numbers**: 6, 7, 8, 45, 46, 47, 51, 52, 53, 54, 55, 56, 57, 83, 86, 88, 103, 104, 105, 106, 107, 108

---

## 6. CI/CD (Continuous Integration & Continuous Delivery/Deployment)

### What
A set of automated practices and pipelines that automatically compile, test, validate, package, and deploy software changes into staging and production environments upon code commits to a version control repository.

### Why
- Eliminates manual, error-prone release checklists and long deployment freezes.
- Delivers bug fixes and new features to customers rapidly with high test coverage and automated safety gates.

### Where We Use Them
- Tools: GitHub Actions, GitLab CI/CD, Jenkins, ArgoCD, CircleCI.
- Automated linting, unit testing, integration testing, container image building, vulnerability scanning, and GitOps deployments.

---

## 7. Docker

### What
An open-source containerization platform that packages an application along with all of its runtime dependencies, libraries, configuration files, and system binaries into a portable, lightweight, standalone executable unit called a container image.

### Why
- Solves the classic "it works on my machine" problem by guaranteeing identical execution environments across local developer laptops, testing environments, and production cloud servers.
- Much lighter and faster than traditional Virtual Machines (VMs) because containers share the host OS kernel instead of virtualizing an entire guest OS.

### Where We Use Them
- Packaging microservices, running local development dependencies (Redis, PostgreSQL, LocalStack) via `docker-compose.yml`, building standardized images for Kubernetes.

---

## 8. Kubernetes (K8s)

### What
An open-source container orchestration platform designed to automate the deployment, scaling, networking, self-healing, and lifecycle management of containerized applications across a cluster of physical or virtual worker nodes.

### Why
- Managing hundreds of standalone Docker containers manually across dozens of machines is impossible.
- Provides native service discovery, load balancing, automated rollouts/rollbacks, storage orchestration, and declarative infrastructure management.

### Where We Use Them
- Cloud-managed Kubernetes: AWS EKS, Google GKE, Azure AKS.
- Orchestrating multi-tier microservices, distributed databases, machine learning inference workloads.

---

## 45. Autoscaling

### What
A dynamic cloud infrastructure feature that automatically adjusts the quantity of compute instances (EC2 VMs, Kubernetes pods, serverless workers) up or down in real-time based on live demand and utilization metrics (CPU usage, memory pressure, request counts, queue backlog).

### Why
- Prevents service outages and high latency during sudden traffic spikes.
- Drastically saves operational costs by scaling down unused compute capacity during quiet off-peak hours (nights and weekends).

### Where We Use Them
- Kubernetes Horizontal Pod Autoscaler (HPA) and Vertical Pod Autoscaler (VPA).
- AWS EC2 Auto Scaling Groups (ASG) based on CloudWatch alarms.
- KEDA (Kubernetes Event-driven Autoscaling) scaling pods based on Kafka topic consumer lag.

---

## 46. Horizontal Scaling (Scaling Out)

### What
The practice of expanding system capacity by adding more discrete machines, nodes, or container instances to the overall pool of compute resources, distributing traffic across them via a load balancer.

### Why
- Unlocks theoretically limitless scalability, far beyond the maximum hardware capacity of any single physical server.
- Eliminates single points of failure (high availability); if one node fails, the rest continue serving traffic.

### Where We Use Them
- Stateless web and API servers, microservices clusters, sharded database nodes (Cassandra, MongoDB, DynamoDB).

---

## 47. Vertical Scaling (Scaling Up)

### What
The practice of increasing system capacity by upgrading the physical or virtual hardware resources of an existing single machine (adding more CPU cores, increasing RAM, attaching faster NVMe SSD storage, or upgrading network bandwidth).

### Why
- Simple to implement: requires zero architectural changes, code rewrites, or complex distributed data partitioning logic.
- Maintains single-node ACID transaction semantics without distributed consensus overhead.

### Where We Use Them
- Monolithic applications, traditional relational databases (PostgreSQL, MySQL, Oracle) before hitting scaling limits where sharding becomes necessary.
- High-memory in-memory caches (single giant Redis instance).

---

## 51. Feature Flags (Feature Toggles)

### What
A software engineering technique that wraps new or conditional code blocks in programmatic switches (toggles) controlled dynamically by a centralized management service without deploying new code.

### Why
- **Decouples deployment from release**: Code can be continuously merged and deployed to production while remaining dark/inactive until ready.
- Enables instant kill-switches (turning off a broken feature in seconds without rolling back code) and targeted beta testing by user role or geography.

### Where We Use Them
- LaunchDarkly, Unleash, Flagsmith, AWS AppConfig.
- Beta tester programs, progressive rollouts, dark launches of new backend migration flows.

---

## 52. Blue-Green Deployment

### What
A release management strategy that utilizes two identical production environments: one active environment currently serving all live traffic ("Blue") and one idle standby environment ("Green") where the new release version is deployed and tested. Once validated, the load balancer or router switches 100% of traffic from Blue to Green instantaneously.

### Why
- Provides near-zero downtime deployments.
- Provides instantaneous, risk-free rollback: if issues emerge on Green, the router immediately points back to Blue.

### Where We Use Them
- Mission-critical banking and e-commerce APIs, Kubernetes services updating selector labels, AWS Route 53 / ALB target group flips.

---

## 53. Canary Releases

### What
A deployment technique where a new software version is released to a tiny fraction of live users or traffic (e.g., 1% to 5%) while the remaining 95% continue running the stable version. The canary is monitored for error rates and latency before gradually increasing the percentage (5% -> 25% -> 100%).

### Why
- Minimizes the "blast radius" of unforeseen bugs, memory leaks, or database performance regressions by exposing only a tiny segment of users.
- Validates real production behavior against live traffic before full commitment.

### Where We Use Them
- Argo Rollouts, Flagger, Istio service mesh, Netflix Spinnaker.
- High-scale services where automated synthetic tests cannot replicate real-world user load diversity.

---

## 54. Rolling Deployments

### What
A deployment method where instances of the old version are incrementally replaced with instances of the new version one by one or in small batches across the cluster until all instances are running the new release.

### Why
- Requires no duplicate standby hardware infrastructure (unlike Blue-Green deployments), saving cloud infrastructure costs.
- Ensures zero downtime by keeping a minimum threshold of healthy instances available at all times (`maxUnavailable` / `maxSurge` controls in Kubernetes).

### Where We Use Them
- Default deployment strategy in Kubernetes (`Deployment`), AWS ECS rolling updates, EC2 Auto Scaling rolling updates.

---

## 55. Rollbacks

### What
The immediate reversion of an application, infrastructure change, or database state to its previous known-good, stable revision following the detection of critical bugs, crashes, or degraded performance in a new release.

### Why
- The quickest path to service restoration during catastrophic production incidents (Mean Time to Recover - MTTR).
- Prevents engineers from attempting panicky "hotfixes" under extreme pressure on broken production systems.

### Where We Use Them
- Automated CI/CD rollback triggers based on Datadog/Prometheus error alerts; `kubectl rollout undo deployment/<name>`; GitOps revert commits.

---

## 56. Health Checks

### What
Periodic, automated ping or inspection probes sent by load balancers, orchestration platforms, or monitoring agents to application endpoints (e.g., `GET /healthz`) to verify if the instance is functional and capable of handling traffic.

### Why
- Enables load balancers to automatically stop routing incoming client traffic to crashed, frozen, or failing backend servers.
- Triggers automatic instance recycling or replacement before end users notice failures.

### Where We Use Them
- AWS Application Load Balancer target group health checks, NGINX upstream health checks, Consul service checks.

---

## 57. Liveness & Readiness Probes

### What
Specialized container health probes in Kubernetes:
- **Liveness Probe**: Determines if the container is still running and healthy. If it fails, Kubernetes kills the pod and restarts a fresh container.
- **Readiness Probe**: Determines if the container is ready to accept incoming traffic (e.g., after loading caches or connecting to the DB). If it fails, Kubernetes temporarily removes the pod from service load balancers without restarting it.

### Why
- Liveness solves deadlocks and unrecoverable hangs (restarts the process).
- Readiness prevents sending user requests to newly spun up pods that are still warming up or pods that are temporarily overloaded.

### Where We Use Them
- Configured in Kubernetes Pod specifications (`livenessProbe: httpGet ...`, `readinessProbe: httpGet ...`).

---

## 83. Disaster Recovery (DR)

### What
A comprehensive set of policies, tools, and technical procedures designed to recover and resume mission-critical technology infrastructure and operations following natural disasters, widespread cloud region outages, cyberattacks, or catastrophic human error.

### Why
- Protects organizations against catastrophic business failure and data destruction.
- Guarantees compliance with business continuity objectives:
  - **RTO (Recovery Time Objective)**: Maximum acceptable downtime duration.
  - **RPO (Recovery Point Objective)**: Maximum acceptable data loss duration.

### Where We Use Them
- DR topologies: **Backup & Restore** (high RTO/RPO), **Pilot Light** (minimal core running in backup region), **Warm Standby** (scaled-down running replica), **Multi-Site Active-Active** (zero RTO/RPO).

---

## 86. Multi-Region Deployment

### What
An architectural pattern where application services, data stores, and supporting infrastructure are deployed concurrently across multiple geographically distinct cloud regions (e.g., `us-east-1`, `eu-central-1`, `ap-southeast-1`).

### Why
- **Global Low Latency**: Serves users from the closest geographic datacenter, cutting intercontinental round-trip times.
- **High Fault Resilience**: An entire datacenter flood or AWS region-wide outage will not take down the global system.

### Where We Use Them
- Global consumer applications (Netflix, Spotify, Uber).
- Implemented with GeoDNS (Route 53 latency/geo routing), Anycast BGP, and globally replicated databases (CockroachDB, DynamoDB Global Tables, Aurora Global Database).

---

## 88. Cost Optimization

### What
The strategic continuous engineering practice of analyzing, profiling, and refining cloud infrastructure resource allocations, architecture patterns, and billing tiers to maximize performance per dollar spent (FinOps).

### Why
- Unmonitored cloud deployments suffer from runaway expenditures (idle VMs, over-provisioned databases, unattached EBS volumes, uncompressed network egress).
- Directly impacts operating margins and profitability.

### Where We Use Them
- AWS Spot Instances for non-critical batch workers, Reserved Instances / Savings Plans for baseline workloads.
- S3 Intelligent-Tiering, cleaning up unused snapshots, right-sizing Kubernetes resource requests/limits, optimizing egress routing.

---

## 103. Semantic Versioning (SemVer)

### What
A formal versioning specification and convention for software releases using a three-part numerical format: `MAJOR.MINOR.PATCH` (e.g., `2.4.1`), optionally appended with pre-release tags (`-beta.1`):
- **MAJOR**: Incremented when introducing incompatible, breaking API or behavioral changes.
- **MINOR**: Incremented when adding backwards-compatible functionality.
- **PATCH**: Incremented when making backwards-compatible bug fixes.

### Why
- Provides an explicit, machine-readable contract between software producers and consumers.
- Allows automated package managers and dependency resolvers to safely apply non-breaking patches and minor updates (`^1.2.0` or `~1.2.0`) without breaking downstream applications.

### Where We Use Them
- Package ecosystems: npm, PyPI, Go modules, Maven, NuGet, Cargo.
- Docker image tags, Helm chart versioning, GitHub release tags.

---

## 104. Infrastructure as Code (IaC)

### What
The practice of managing, provisioning, and configuring cloud infrastructure (compute, networks, databases, load balancers, IAM policies) using declarative configuration files and version-controlled code rather than manual GUI clicks or one-off CLI scripts.

### Why
- Eliminates **environment drift** (discrepancies between staging and production) and undocumented manual changes.
- Enables repeatable, automated, and auditable infrastructure provisioning directly integrated into CI/CD pipelines.
- Supports disaster recovery: an entire cloud infrastructure stack can be recreated from scratch in minutes using code.

### Where We Use Them
- Declarative tools: Terraform, OpenTofu, AWS CloudFormation, Pulumi, Kubernetes manifests.
- Managing multi-environment cloud footprints across AWS, Azure, GCP, and Cloudflare.

---

## 105. Terraform

### What
An open-source, cloud-agnostic Infrastructure as Code tool created by HashiCorp that uses HashiCorp Configuration Language (HCL) to declare cloud and on-premises resources, utilizing a persistent state file (`terraform.tfstate`) to compute and execute execution plans (`terraform plan` / `terraform apply`).

### Why
- **Cloud-Agnostic**: A unified workflow and configuration syntax to manage AWS, GCP, Azure, Kubernetes, Datadog, and hundreds of other providers through modular plugins.
- **State Management**: Accurately tracks real-world infrastructure state against declared code, detecting and correcting out-of-band drift.
- **Dependency Graph**: Automatically constructs a DAG (Directed Acyclic Graph) of resources to create or modify independent components in parallel.

### Where We Use Them
- Enterprise cloud provisioning (VPCs, subnets, EKS clusters, RDS instances, IAM roles, S3 buckets).
- Multi-cloud orchestration and GitOps infrastructure pipelines via Terraform Cloud / Spacelift / Atlantis.

---

## 106. Helm Charts

### What
The standard package manager and templating system for Kubernetes. A Helm Chart is a packaged collection of YAML templates, default configurations (`values.yaml`), and metadata used to define, version, install, and upgrade complex Kubernetes applications.

### Why
- Deploying a microservice on Kubernetes typically requires 5–10 separate YAML files (Deployment, Service, Ingress, ConfigMap, Secret, HPA, ServiceAccount).
- Helm parametrizes these manifests into reusable templates, allowing the same chart to be deployed across development, staging, and production simply by swapping environment-specific `values.yaml` files.
- Provides atomic releases, dependency management, and automated release rollbacks (`helm rollback`).

### Where We Use Them
- Deploying third-party cluster addons (Prometheus Operator, Ingress-NGINX, Cert-Manager, ArgoCD).
- Packaging internal enterprise microservices for standardized Kubernetes deployments.

---

## 107. Build Caching

### What
An optimization technique in compilers, package managers, and CI/CD pipelines that saves and reuses the intermediate artifacts, compiled binary layers, or fetched dependencies of earlier builds when their corresponding source inputs and checksums have not changed.

### Why
- Modern application builds (installing thousands of npm packages, compiling large Rust/C++/Java binaries, building multi-stage Docker images) can take 20–45 minutes per pull request.
- Build caching cuts CI/CD pipeline runtimes down from tens of minutes to seconds, accelerating developer productivity and reducing cloud runner compute costs.

### Where We Use Them
- **Docker Layer Caching**: Multi-stage Docker builds ordering cached steps (e.g., copying `package.json` and running `npm install` before copying source code).
- **CI Caching**: GitHub Actions `actions/cache`, GitLab CI cache, Turborepo, Gradle build cache, Bazel remote cache.

---

## 108. Dependency Hell

### What
An anti-pattern and software engineering state where an application cannot function or build properly due to conflicting, circular, incompatible, or excessively nested transitive dependency requirements across third-party libraries and runtime packages.

### Why
- When Library A requires Package X version 1.0, but Library B requires Package X version 2.0 with breaking changes, the runtime or package manager cannot resolve a single mutually compatible version (diamond dependency problem).
- Creates build breakages, bloated deployment artifacts, and introduces severe unpatched security vulnerabilities deep inside transitive trees.

### Where We Use Them
- **Mitigation & Resolution**:
  - Deterministic lockfiles: `package-lock.json`, `pnpm-lock.yaml`, `Cargo.lock`, `Pipfile.lock`, `go.sum`.
  - Containerization (Docker) isolating host OS dependencies.
  - Dependency isolation / shading (Maven Shade plugin, Go vendoring).
  - Automated dependency scanners (Dependabot, Renovate, Snyk).
