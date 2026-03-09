# System Architecture Memory (State Anchor)

> **Purpose:** Defines the structural boundaries of the repository. AI MUST strictly respect these boundaries when generating logic or files.

## Topological Context
- **Detected Architecture Patterns**: Standard/Flat (No explicit macro-architecture found).

## Architectural Constraints (`system-architect`)
- **Modularity Over Monoliths**: If Feature-Sliced or Modular patterns are detected, keep code cohesive to its domain.
- **Separation of Concerns**: Controllers MUST NOT have business logic. Extract to Use Cases / Services.
- **Atomic Strictness**: If Atomic Design is detected on UI, Atoms cannot contain or import Molecules/Organisms.

## Signature Paths
*(Add critical system paths here, e.g., 'API Routes are in apps/api/src/routes')*
- TBD
