---
name: database-architect
description: Use when designing database schemas, creating migrations, choosing indexing strategies, analyzing query performance (N+1), or determining relational vs NoSQL boundaries regardless of the ORM (Prisma, Eloquent, GORM) being used.
metadata:
  version: 1.1.0
  priority: high
---

# DATABASE ARCHITECT

## SCHEMA RULES
- **3NF Default**: Denormalize only if bottleneck is proven.
- **Data Types**: No lazy JSON/JSONB for relational data.
- **IDs**: UUIDv4/ULID for public; Auto-increment for internal.
- **Audit**: `created_at`, `updated_at`, `deleted_at` (soft deletes).

## INDEXING
- **Mandatory**: Every foreign key must be indexed.
- **Lookups**: `WHERE`, `JOIN`, `ORDER BY` columns.
- **Composite**:selective-first ordering for multi-column filters.

## OPTIMIZATION
- **Zero N+1**: Explicit Eager Loading (`include`, `with`, `Preload`).
- **Selectivity**: No `SELECT *`; fetch required fields only.
- **Transactions**: Atomic multi-table mutations.

## WORKFLOW
1. Context Check (`system-architecture.md`) -> 2. Safe Migration generation -> 3. Declare indexing logic.
