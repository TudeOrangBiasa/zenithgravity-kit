---
name: behavioral-modes
description: AI operational modes (brainstorm, implement, debug, review, teach, ship, orchestrate). Use to adapt behavior based on task type.
metadata:
  version: 1.3.0
  priority: high
---

# BEHAVIORAL MODES

## EFFORT CALIBRATION

Map the user's request to the right effort level FIRST:

| Mode | Trigger | Effort Level |
|---|---|---|
| **brainstorm** | Ambiguous/exploratory requests | Light |
| **implement** | Single clear feature | Light → Deep |
| **debug** | Bug or error report | Light → Deep |
| **review** | Code/plan review request | Light |
| **teach** | Explanation request | Instant → Light |
| **ship** | Production deployment | Deep → Exhaustive |
| **orchestrate** | Multi-file/multi-step task | Deep → Exhaustive |

## EFFORT LEVELS
- **Instant (Typo/Rename)**: Direct fix + Lint.
- **Light (Small feature)**: Scan -> Implement -> Verify.
- **Deep (Multi-file/API)**: Investigate -> Plan -> Per-file implementation/verification.
- **Exhaustive (Architecture)**: Multi-approach investigation -> Full plan -> Comprehensive verification.

## STRATEGIC HYGIENE
- **Lazy Read**: Only read what's necessary (no full codebase reads for local fixes).
- **Minimal Mutation**: No unrelated refactors.
- **Standard Lib**: Prefer native logic over new dependencies.
- **Late Abstraction**: Wait for 3+ repetitions.
- **CLI First**: Use `npm init`, `cargo new`, `go mod init` (no manual config writing).

## ANTIGRAVITY CONSTRAINTS
- All CLI commands must use `rtk` prefix (`rtk lint`, `rtk git status`, `rtk vitest run`).
- NEVER provide partial code snippets — every code block must be production-ready.
- ARTIFACT-FIRST: Generate Implementation Plan before writing any code on Deep/Exhaustive modes.
