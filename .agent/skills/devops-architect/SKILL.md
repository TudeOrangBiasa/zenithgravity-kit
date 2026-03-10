---
name: devops-architect
description: Use when designing CI/CD pipelines (GitHub Actions, GitLab CI), writing Infrastructure as Code (Terraform, Docker, K8s), configuring Observability, or troubleshooting deployment failures and production incidents.
metadata:
  version: 1.1.0
  priority: high
---

# DEVOPS ARCHITECT

## CONTAINERS
- **Immutability**: Build-time installs only (no runtime code pulling).
- **Security**: Alpine/Distroless; Non-root process only.
- **Multi-Stage**: Separate build env from production runtime.
- **Availability**: Readiness/Liveness probes; Rolling/Blue-Green deployments.

## CI/CD
- **Stages**: Lint -> Test -> Build -> Security Scan -> Deploy.
- **Secrets**: Native secrets managers only (GitHub/AWS/Vault), no hardcodes.
- **Gates**: Fail deploy on tool failure (`test` or `sec-ops`).

## OBSERVABILITY
- **Logic**: Logs (ELK/Loki) -> Metrics (Prometheus) -> Traces (OTel).
- **Rollbacks**: Idempotent reversion via container tag or TF state.

## WORKFLOW
1. Environment Check (`system-architecture.md`) -> 2. YAML/HCL Output -> 3. Incident Report (Symptom/Hypothesis/Resolution) if debugging.
