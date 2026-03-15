---
name: api-architect
description: Use when designing new API endpoints (REST, GraphQL, tRPC), establishing JSON payload contracts, planning API versioning, or setting up API responses/pagination regardless of the backing language.
metadata:
  version: 1.2.0
  priority: high
---

# API ARCHITECT

## CONTEXT SYNC
- Mandatory: Read `.agent/memory/system-architecture.md` before designing any endpoint.
- Respect existing auth patterns, pagination conventions, and versioning strategy.

## REST CONVENTIONS
- **Nouns Only**: `/users`, not `/getUsers`.
- **Plurals**: `/products/:id`.
- **Mapping**: GET (read), POST (create), PUT (replace), PATCH (update), DELETE (remove).
- **Codes**: 200/201/204 (Success), 400/401/403/404/422/429 (Client Error), 500 (Server - No stack trace).

## DATA SHAPES
- **Envelope**: `{ success: bool, data: {}, meta: { page, total } }`.
- **Error**: `{ success: false, error: { code, message, details: [] } }`.
- **Rules**: Cursor/Offset pagination (no unbounded arrays), URL/Header Versioning, Idempotency-Keys for POST.

## SECURITY
- Throttle/Rate-Limit assumption.
- Filter exposure via query params (`?role=admin&sort=-id`).

## RTK ENFORCEMENT
- Test endpoints with `rtk curl <url>` for compact HTTP response output.
