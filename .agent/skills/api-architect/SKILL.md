---
name: api-architect
description: Use when designing new API endpoints (REST, GraphQL, tRPC), establishing JSON payload contracts, planning API versioning, or setting up API responses/pagination regardless of the backing language.
metadata:
  version: 1.0.0
  priority: high
---

# API Architect

> **Philosophy**: Nouns over Verbs. Consistent Envelopes. Idempotency is king.

## 1. RESTful Strictness

If building a REST API, you MUST follow strict conventions:

- **Nouns, Not Verbs**: Use `/users`, not `/getUsers` or `/createUser`.
- **Pluralization**: Resources are always plural (`/products/:id`, `/orders/:id`).
- **HTTP Methods Mapping**:
  - `GET`: Idempotent read.
  - `POST`: Non-idempotent creation.
  - `PUT`: Idempotent full replacement.
  - `PATCH`: Non-idempotent partial update.
  - `DELETE`: Idempotent removal.
- **Status Codes**:
  - `200` (OK), `201` (Created), `204` (No Content).
  - `400` (Bad Request/Validation), `401` (Unauth), `403` (Forbidden), `404` (Not Found), `422` (Unprocessable Entity).
  - `429` (Rate Limited).
  - `500` (Internal Error - never expose stack traces to the client).

## 2. API Envelope & Response Shapes

Regardless of the framework (Express, Laravel, Django, Gin), enforce a standardized JSON response envelope:

```json
{
  "success": true,
  "data": { ... },
  "meta": {
    "page": 1,
    "total": 100
  }
}
```

For errors:

```json
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid input provided.",
    "details": [...]
  }
}
```

## 3. Pagination & Filtering

- Never return unbounded arrays. Always implement pagination (Cursor-based preferred for infinite scroll, Offset-based for data tables).
- Expose filters via query parameters (`GET /users?role=admin&sort=-created_at`).

## 4. API Security & Versioning

- **Versioning**: Enforce URI versioning (`/v1/users`) or Header versioning natively to prevent breaking mobile client contracts.
- **Rate Limiting**: Always assume endpoints need throttling configurations.
- **Idempotency Keys**: For financial or critical `POST` actions, design them to accept an `Idempotency-Key` header.
