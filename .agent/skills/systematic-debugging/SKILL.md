---
name: systematic-debugging
description: A 4-phase structured debugging methodology focusing on root cause analysis over trial and error. Use whenever the user reports a bug, crash, or an unexpected error message.
metadata:
  version: 1.0.0
  priority: critical
---

# Systematic Debugging

## Objective

Eradicate "trial and error" coding. When a bug or stack trace is encountered, you must not guess the fix. You must locate the exact fault line and perform a structured root-cause analysis (The "5 Whys") before modifying any code.

## Operating Rules

### Phase 1: CLASSIFY & PARSE

When an error is reported or discovered:

1. **Never guess**: Stop and identify the error category (Syntax, Type, Network, DB, Dependency, OOM, etc).
2. **Extract Context**: Pinpoint the precise file path, line number, and error payload.

### Phase 2: REPRODUCE & ISOLATE

1. Can you reproduce it using a test or CLI command? Do so if safe.
2. If the error is obscured, isolate the environment (e.g., read the raw logs, use `-v` verbosity, or read `stderr` directly).
3. Use Binary Search if the error location is vague: comment out halves of the logic until the error disappears.

### Phase 3: ANALYZE (The 5 Whys)

Do not patch the symptom. Analyze the Root Cause.
_Symptom_: Cannot read property 'name' of undefined.
_Why 1?_: Because the `user` object is undefined.
_Why 2?_: Because the DB query returned null.
_Why 3?_: Because the `tenant_id` was missing from the query context.
_Why 4?_: Because the auth middleware dropped the tenant header.
_Root Cause_: Auth middleware fails to pass standard headers.

### Phase 4: RESOLVE & PREVENT

1. Provide the **Immediate Fix** to unblock the user.
2. Provide the **Proper Architectural Fix** (if different).
3. Generate a **Verification Plan** (How do we prove this works? Can we write a `test`?).

## Enforced Output Format

When asked to fix an error, your response MUST summarize your findings using this structure:

```markdown
## Error Diagnosis

**Classification**: [Type / Scope]
**Location**: `path/to/file.ext:LL`

## Root Cause Analysis

[1-2 sentences explaining the true underlying flaw]

## Proposed Fix

[The exact changes needed]
```
