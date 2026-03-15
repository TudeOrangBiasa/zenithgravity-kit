---
description: Implement localized feature or change with fast, low-overhead execution.
---

# /create - Focused Implementation

$ARGUMENTS

## Goal

Deliver requested changes quickly for clear, low-risk tasks.

## Flow

0. Run `python3 .agent/scripts/detect_stack.py .` to understand the language, framework, and environment constraints before execution.
1. Parse requirement and constraints.
2. **Logic Check**: Pass the planned changes through `@logic-critic` to detect edge cases and race conditions before execution.
3. Implement minimal changes.
4. Run narrow validation (with `@self-healer` active for terminal errors).
5. Return concise handoff.

## Rules

- Skip heavyweight planning for trivial tasks.
- Keep behavior changes explicit.
- **UI Quality Gate**: If task involves UI components, ALWAYS run `@polish` natively to refine aesthetics and `@audit` for accessibility before handoff.
- **Structured Handoff**: Even for small tasks, provide a concise summary of modified files and verification results.
