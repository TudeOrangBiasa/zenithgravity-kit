---
name: sec-ops
description: Use when performing Code Reviews, security audits, dependency checking, or attempting to harden an application. Enforces OWASP top 10 prevention and rates vulnerabilities by Severity.
metadata:
  version: 1.1.0
  priority: high
---

# SECURITY OPS (SecOps)

## FINDING TIERS
- 🔴 **CRITICAL**: SQLi, XSS, Auth Bypass, IDOR, RCE, Secrets, CSRF.
- 🟡 **IMPORTANT**: Logic bugs, Race conditions, Rate-limiting, Missing Pagination, Unhandled Panics.
- 🔵 **NIT**: Formatting/Naming.

## ZERO-TRUST RULES
- **Input**: Parameterized queries only; strict schema validation (Zod/Pydantic).
- **Access**: Verify `resource.owner_id == current_user.id` or Admin role.
- **Auth**: Bcrypt/Argon2 hashing; short-lived JWTs; HttpOnly Secure cookies.
- **Data**: Strip sensitive fields at DTO layer; 500 errors = NO stack traces.

## WORKFLOW
1. Generate **SecOps Report** (🔴/🟡 risks).
2. **Dry-Run**: `rtk npm audit` or similar before final status.
