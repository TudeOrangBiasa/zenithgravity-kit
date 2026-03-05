---
description: Resolve defects using reproducible, root-cause-focused debugging.
---

# /debug - Systematic Debugging

$ARGUMENTS

## Goal
Fix the root cause, not symptoms.

## Flow
1. Reproduce issue consistently.
2. Isolate root cause.
3. Apply minimal safe fix.
4. Verify fix + nearby regressions.
5. Summarize cause, fix, and remaining risk.

## Rules
- No broad refactors during bug fix unless necessary.
- Do not claim fix without reproduction and re-check.
