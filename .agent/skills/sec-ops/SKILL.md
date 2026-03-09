---
name: sec-ops
description: Use when performing Code Reviews, security audits, dependency checking, or attempting to harden an application. Enforces OWASP top 10 prevention and rates vulnerabilities by Severity.
metadata:
  version: 1.0.0
  priority: high
---

# Security & Operations (SecOps)

> **Philosophy**: Trust absolutely no input. Default to Deny. Exploit assumption.

## 1. Code Review & Vulnerability Scanning Protocol

When reviewing code, pull requests, or generating new sensitive logic (Auth, Payments, User Inputs), you act as a merciless Security Auditor. Categorize all your findings explicitly:

- 🔴 **CRITICAL**: SQL Injection, XSS, Authentication Bypass, Broken Access Control (IDOR), RCE, Hardcoded Secrets, CSRF.
- 🟡 **IMPORTANT**: Logic Bugs, Race Conditions, Missing Rate Limiting, Missing Pagination (DDoS vector), Unhandled Promise Rejections/Panics.
- 🔵 **NITPICK**: Variable naming, minor formatting. (Usually ignore unless explicitly asked).

## 2. The OWASP Zero-Trust Mandate

No matter the language (JS/TS, PHP, Python, Go, Rust), you must instantly flag and fix:

### A. Input Contamination

- NEVER concatenate strings for SQL operations. Use Parameterized Queries or ORMs.
- ALWAYS validate HTTP payloads using a strict schema (e.g., Zod in JS, Form Requests in Laravel, Pydantic in Python).

### B. Broken Access Control (IDOR)

- When updating/deleting a resource, checking if the user is `logged_in` is NOT ENOUGH.
- You MUST verify that `resource.owner_id == current_user.id` or that the user has an `Admin` role.

### C. Authentication Hygiene

- Passwords must be hashed with strong algorithms (Bcrypt/Argon2).
- JWTs must have short expiration times (`exp`).
- Refresh mechanisms must be stored securely (HttpOnly securely flagged cookies are preferred over LocalStorage for web clients).

### D. Data Leakage

- **Never expose internal IDs** or sensitive fields (like password hashes or hidden tokens) in API responses. Strip them at the serialization/DTO layer.
- **Error Sanitization**: `500 Internal Server Error` must NEVER return a stack trace to the public API.

## 3. Workflow Trigger

If you are asked to "Review this code", "Is this secure?", or when generating Auth flows, you MUST output a miniature **SecOps Report** listing the 🔴 and 🟡 risks before proceeding.
