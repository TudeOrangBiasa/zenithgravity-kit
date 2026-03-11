# System Architecture Memory (State Anchor)

> **Purpose:** Defines structural boundaries. AI MUST respect these when generating logic or files.

## Topological Context
- **Detected Architecture Patterns**: Standard/Flat (No explicit macro-architecture found).

## Architectural Constraints (system-architect)
- **Modularity Over Monoliths**: Keep code cohesive to its domain.
- **Separation of Concerns**: Controllers MUST NOT have business logic. Extract to Use Cases / Services.
- **Atomic Strictness**: Atoms cannot import Molecules/Organisms.

## Signature Paths
*(Update with critical system paths, e.g., 'API Routes → apps/api/src/routes')*
- TBD
