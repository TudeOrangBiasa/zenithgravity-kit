---
name: quality-assurance
description: Use to run targeted checks, analyze test results, and define verification strategies before claiming completion.
metadata:
  version: 1.2.0
  priority: medium
---

# QUALITY ASSURANCE

## RULES
- **Adversarial Review**: Attack your own solution; find edge cases.
- **Small First**: Unit/Type checks before full E2E.
- **Evidence-First**: Output exact commands + results.
- **Regressions**: Check dependencies in `CODEBASE.md`.

## RTK ENFORCEMENT
- Run all checks with `rtk` prefix for token-efficient output: `rtk vitest run`, `rtk playwright test`, `rtk tsc`.
- Use `python3 .agent/scripts/verify_changes.py` as the Antigravity gate before claiming completion.

## DONT
- Assume UI correctness without structural/visual proof.
- Claim "Complete" without terminal evidence showing passing checks.
