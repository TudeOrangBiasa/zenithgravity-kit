---
name: system-architect
description: Use when designing core architecture, structural refactoring, implementing Domain-Driven Design (DDD), Clean Architecture, or Modular Monoliths. Vital for backend logic or complex full-stack apps.
metadata:
  version: 1.1.0
  priority: high
---

# SYSTEM ARCHITECT

## CONTEXT SYNC
- Mandatory: Read `.agent/memory/system-architecture.md` before build.
- Respect topology (Modular Monolith / Feature-Sliced / Clean Architecture).

## CORE PATTERNS
- **Modular/FSD**: Group by Domain (`src/modules/billing`), not concern.
- **Clean/DDD**:
  1. Domain (Entities - No framework).
  2. Application (Use Cases/Services).
  3. Infrastructure (Repositories/APIs).
  4. Presentation (Controllers - HTTP only).
- **Atomic (FE)**: Atom -> Molecule -> Organism hierarchy.

## ANTI-SLOP
- **No Fat Controllers**: HTTP extraction/response only.
- **No ORM Leaks**: Map models to DTOs/Entities.
- **No Tight Coupling**: Use Interfaces (Ports/Adapters).
- **No God Objects**: Extract modular context boundaries.

## WORKFLOW
1. Identify Domain -> 2. Design Interfaces -> 3. Implement within boundaries.
