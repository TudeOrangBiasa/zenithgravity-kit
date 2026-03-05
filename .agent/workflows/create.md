---
description: Implement localized feature or change with fast, low-overhead execution.
---

# /create - Focused Implementation

$ARGUMENTS

## Goal

Deliver requested changes quickly for clear, low-risk tasks.

## Flow

0. Run `python .agent/scripts/detect_stack.py .` to understand the language, framework, and environment constraints before execution.
1. Parse requirement and constraints.
2. Implement minimal changes.
3. Run narrow validation.
4. Return concise handoff.

## Rules

- Skip heavyweight planning for trivial tasks.
- Keep behavior changes explicit.
