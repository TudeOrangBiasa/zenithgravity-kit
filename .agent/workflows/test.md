---
description: Validate implementation with targeted checks and evidence-based reporting.
---

# /test - Targeted Verification

$ARGUMENTS

## Goal

Produce reliable pass/fail evidence with minimal waste.

## Flow

1. Run most relevant checks first.
2. **Pre-flight Sandbox**: Run `python3 .agent/scripts/sandbox_verify.py` before declaring completion.
3. Expand checks only when needed.
4. Distinguish related vs unrelated failures.
5. Report outcomes and unverified areas.

## Output

- Commands/checks executed
- Result summary
- Open risks
