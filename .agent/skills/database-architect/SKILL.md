---
name: database-architect
description: Use when designing database schemas, creating migrations, choosing indexing strategies, analyzing query performance (N+1), or determining relational vs NoSQL boundaries regardless of the ORM (Prisma, Eloquent, GORM) being used.
metadata:
  version: 1.0.0
  priority: high
---

# Database Architect

> **Philosophy**: Optimize for read/write ratios. Never skip indexing. Eliminate N+1 queries. Stay framework-agnostic.

## 1. Schema Design Core Principles

When asked to design or modify a database schema, you must enforce the following rules:

- **Normalization by Default**: Start with 3NF (Third Normal Form). Denormalize ONLY if there is a mathematically proven performance bottleneck.
- **Data Types Matter**: Do not use `JSON`/`JSONB` columns as a lazy alternative to proper relational modeling. Use UUIDv4 or ULID for public-facing primary keys (prevent ID guessing), and consider auto-incrementing Integers for internal-only clustering/performance.
- **Audit Trails**: Heavily trackable entities should always have `created_at`, `updated_at`, and potentially `deleted_at` (for Soft Deletes).

## 2. Indexing Strategy

Before submitting any schema, you must define the indexes:

- **Foreign Keys**: Every foreign key MUST have an index.
- **Lookups**: Columns used in `WHERE`, `JOIN`, or `ORDER BY` clauses heavily must be indexed.
- **Composite Indexes**: Use composite indexes for queries filtering by multiple columns simultaneously (e.g., `user_id` + `status`). Order the composite index by the most selective column first.

## 3. Query Optimization & ORM Usage

Regardless of whether the project uses **Prisma (Node)**, **Laravel Eloquent (PHP)**, **GORM (Go)**, or **SQLAlchemy (Python)**:

- **Zero Tolerance for N+1**: Always eagerly load relationships using the framework's native fetching methods (e.g., `include` in Prisma, `with()` in Eloquent, `Preload()` in GORM).
- **Selectivity**: Never use `SELECT *` implicitly. Explicitly select only the fields required for the payload.
- **Transactions**: Any operation modifying more than one table simultaneously MUST be wrapped in a Database Transaction.

## 4. Execution Protocol

When executing a database modification task:

1. Identify the targeted ecosystem from `.agent/memory/system-architecture.md`.
2. Generate the safe migration file or schema syntax specific to that ORM.
3. Explicitly state the indexing logic applied in your response.
