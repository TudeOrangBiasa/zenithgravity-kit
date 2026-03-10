---
name: behavioral-modes
description: AI operational modes (brainstorm, implement, debug, review, teach, ship, orchestrate). Use to adapt behavior based on task type.
metadata:
  version: 1.1.0
  priority: high
---

# BEHAVIORAL MODES

## ADAPTIVE EFFORT
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
