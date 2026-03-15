---
name: logic-critic
description: Validates work plans before execution to prevent logic gaps, race conditions, and side effects.
metadata:
  version: 1.1.0
  priority: high
---

# LOGIC CRITIC (Antigravity Harness)

## Goal
Force multi-step architectural reasoning before writing code. You must act as an independent reviewer interrogating your own implementation plan.

## Instructions
1. Interrogate the implementation plan for:
   - Edge cases (race conditions, null pointers, infinite loops).
   - Dependency side effects (does changing X break Y?).
   - Context completeness (Confidence threshold must be >90%).
2. Use `<thought>` blocks to explicitly list out the logical vulnerabilities of the plan.
3. **MANDATORY**: REJECT any plan internally that lacks a clear "Verification Plan" or "Rollback Strategy".
4. Modify the plan or approach if vulnerabilities are found BEFORE moving to execution.

## OUTPUT FORMAT
Produce this critique block before any code is written:

```
## Logic Critique
- **Verdict**: APPROVED / REJECTED / NEEDS REVISION
- **Risks Found**:
  - [CRITICAL] <description> (if any)
  - [WARNING] <description> (if any)
- **Missing**: Verification Plan / Rollback Strategy / Edge case handling
- **Decision**: Proceed / Revise plan first
```
