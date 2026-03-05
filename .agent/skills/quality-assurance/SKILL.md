---
name: quality-assurance
description: Use to run targeted checks, analyze test results, and define verification strategies before claiming completion.
metadata:
  version: 1.0.0
  priority: medium
---

# Quality Assurance Skill

## Objective

Provide evidence-based verification for any code or architecture changes.

## Operating Rules

- **Adversarial Self-Review**: Before finalizing complex work, attack your own solution: What would break this? Are there edge cases? Am I assuming something wrong? Is there a simpler way?
- **Verify Smallest Scope First**: Run localized unit tests or type checks before full E2E suites.
- **Evidence-Based Reporting**: Output exactly what commands were run and their results.
- **Regression Awareness**: Always check dependencies of the modified file (`CODEBASE.md`).

## Non-Goals

- Do not assume UI correctness without visual or structural proof.
