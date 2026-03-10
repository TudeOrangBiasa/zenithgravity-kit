---
name: systematic-debugging
description: A 4-phase structured debugging methodology focusing on root cause analysis over trial and error. Use whenever the user reports a bug, crash, or an unexpected error message.
metadata:
  version: 1.1.0
  priority: critical
---

# SYSTEMATIC DEBUGGING (4-Phase)

1. **CLASSIFY**: Never guess. Identify category (Syntax, Type, Network, DB, etc.). Extract context (Path, Line, Payload).
2. **REPRODUCE**: Isolate via test/CLI. Use high verbosity (`-v`) or `stderr`. Binary search if vague.
3. **ANALYZE (5 Whys)**: Fix root cause, not symptom. Trace from error back to source logic.
4. **RESOLVE**: Provide Immediate Fix + Architectural Fix + Verification Plan (Test).

## DIAGNOSIS FORMAT
- **Classification**: [Type/Scope]
- **Location**: `file:line`
- **Root Cause**: 1-2 sentence tech explanation.
- **Proposed Fix**: Exact code change.
