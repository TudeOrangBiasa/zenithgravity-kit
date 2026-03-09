---
name: system-architect
description: Use when designing core architecture, structural refactoring, implementing Domain-Driven Design (DDD), Clean Architecture, or Modular Monoliths. Vital for backend logic or complex full-stack apps.
metadata:
  version: 1.0.0
  priority: high
---

# System Architect

> **Philosophy**: Isolate the Domain. De-couple the Framework. Favor Modularity over "God Objects".

## 1. Context Synchronization (MANDATORY)

Before writing any architectural code (creating models, services, controllers, or modules), you **MUST** read `.agent/memory/system-architecture.md` to understand the project's topology.

- **Observe Detected Patterns**: If the project uses _Modular Monolith_ or _Feature-Sliced Design_, do not place new logic in global folders; keep it cohesive within the module.
- **Respect Boundaries**: If _Clean Architecture / DDD_ is detected, enforce the Dependency Rule: _Dependencies must only point inward toward the Domain._

## 2. Core Architectural Patterns

### A. Modular Monolith / Feature-Sliced Design

- Group code by **Feature/Domain**, not by technical concern (e.g., avoid a single global `controllers/` folder for 50 different domains).
- Example structure: `src/modules/billing/`, `src/modules/users/`.
- Each module should encapsulate its own Routes, Controllers, Services, and Repositories.

### B. Clean Architecture & DDD (Domain-Driven Design)

If building complex backends, strictly separate concerns into layers:

1. **Domain (Entities / Value Objects)**: Pure business rules. NO framework imports (no Express, no Prisma, no ORM decorators).
2. **Application (Use Cases / Services)**: Orchestrates domain objects.
3. **Infrastructure (Repositories / External APIs)**: Database and 3rd party specific implementation (e.g., Postgres, Redis, external gateways).
4. **Presentation (Controllers / Resolvers)**: Handles HTTP/GraphQL input/output only.

### C. Atomic Design (For Frontend Systems)

If Frontend architecture uses Atomic Design:

- **Atoms**: Basic UI elements (Buttons, Inputs).
- **Molecules**: Groups of atoms (Form Fields, Search Bars).
- **Organisms**: Complex functional UI (Headers, Sidebars).
- **Templates/Pages**: Page-level structures.
  Do not bypass the hierarchy. An Atom cannot import a Molecule.

## 3. Anti-Slop (Forbidden Backend Habits)

- **Fat Controllers**: Controllers MUST NOT contain business logic. They should extract HTTP payloads, call a Use Case/Service, and return the HTTP response.
- **ORM Leaks**: Do not return raw ORM models directly to the presentation layer if possible. Map them to DTOs or Domain Entities.
- **Tight Coupling**: Do not import infrastructure details directly into Use Cases. Rely on Interfaces (Ports and Adapters).
- **God Objects**: Stop appending methods to massive `utils.ts` or a global `app.ts`. Extract into distinct modular context boundaries.

## 4. Execution Workflow

When tasked with implementing a new feature or refactoring:

1. **Identify the Target Domain**: Which module does this belong to?
2. **Design Interfaces First**: Define the interface/port before writing the implementation.
3. **Draft the Implementation**: Keep it strictly within the architectural boundaries established in `.agent/memory/system-architecture.md`.
