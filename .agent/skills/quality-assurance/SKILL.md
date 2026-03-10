---
name: quality-assurance
description: Use to run targeted checks, analyze test results, and define verification strategies before claiming completion.
metadata:
  version: 1.1.0
  priority: medium
---

# QUALITY ASSURANCE

## RULES
- **Adversarial Review**: Attack your own solution; find edge cases.
- **Small First**: Unit/Type checks before full E2E.
- **Evidence-First**: Output exact commands + results.
- **Regressions**: Check dependencies in `CODEBASE.md`.

## DONT
- Assume UI correctness without structural/visual proof.
