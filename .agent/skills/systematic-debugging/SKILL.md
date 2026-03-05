---
name: systematic-debugging
description: A 4-phase structured debugging methodology focusing on root cause analysis over trial and error.
metadata:
  version: 2.0.0
  priority: high
---

# Systematic Debugging Protocol

> **CRITICAL**: Use this protocol to prevent random guessing when fixing bugs.

## 4-Phase Debugging Process

An AI must never apply blind "Maybe if I change this..." fixes. You must follow these 4 phases sequentially:

### Phase 1: Reproduce

Understand precisely how the bug manifests.

- Ask: Can I reproduce this consistently? Do I understand the expected behavior?

### Phase 2: Isolate

Narrow down the exact source of the failure.

- Action: Check logs, error messages, and trace back through the function calls. What is the smallest unit of code triggering this?

### Phase 3: Root Cause Analysis (Understand)

Identify the structural or logical flaw. Do not stop at the symptom.

- Use the **5 Whys**:
  - (Symptom): "The button doesn't work."
  - (Why 1): "The onClick handler throws an error."
  - (Why 2): "The user object is undefined."
  - (Why 3): "The authentication state hasn't resolved yet." -> (Root Cause).

### Phase 4: Fix & Verify

Only after the root cause is understood, implement the fix.

- Ensure the fix doesn't cause regressions.
- If necessary, run test scripts to verify.

## Anti-Patterns (BANNED BEHAVIORS)

❌ **Ignoring Evidence**: "The error says X, but I'll fix Y."
❌ **Hiding Errors**: Adding a `try-catch` block that does nothing just to suppress a warning.
❌ **Shotgun Debugging**: Changing 5 different files simultaneously hoping one combination works.
