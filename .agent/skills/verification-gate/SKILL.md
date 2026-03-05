---
name: verification-gate
description: Use for enforcing evidence-based completion through targeted checks, regression awareness, and concise reporting.
metadata:
	version: 1.0.0
	priority: high
---

# Verification Gate Skill

## Objective
Ensure implementation claims are backed by concrete checks.

## Verification Strategy
1. Run the narrowest relevant check first.
2. Expand to broader checks only if needed.
3. Separate related failures from unrelated pre-existing issues.

## Report Format
- Checks executed
- Outcome summary
- Remaining risks or unverified areas

## Non-Goals
- Do not fix unrelated failing tests unless requested.
