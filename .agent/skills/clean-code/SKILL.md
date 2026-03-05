---
name: clean-code
description: Pragmatic coding standards - concise, direct, no over-engineering, no unnecessary comments.
metadata:
  version: 2.0.0
  priority: high
---

# Clean Code - Pragmatic AI Coding Standards

> **CRITICAL SKILL** - Be **concise, direct, and solution-focused**. Stop writing tutorials in your code comments.

## Core Rules

1. **Working Code > Explanations**: If the user asks for a feature or reports a bug, just write/fix the code. Do not write a long essay explaining what you are going to do before doing it.
2. **SRP & Flat Structure**: Functions must do one thing. Avoid deep nesting (max 2 levels). Use Guard Clauses (Early Returns) instead of nested if-else.
3. **No Redundant Comments**: Do not write comments explaining obvious logic. Let variables and function names reveal intent (e.g., `hasPermission` instead of `userStatusCheck`). If a comment is needed to explain what a variable is, rename the variable.
4. **YAGNI (You Aren't Gonna Need It)**: Do not over-engineer. Do not build abstract factory patterns for 2 objects. Keep it brutally simple.

## Before Editing ANY File (THINK FIRST!)

Before changing a file, pause and verify its ecosystem (`CODEBASE.md`):

- What imports this file? (They might break)
- What does this file import? (Interface changes)
- What tests cover this? (Tests might fail)

**Rule:** Always update dependent files within the SAME task boundary. Never leave broken imports.

## Completion Gate

Before proclaiming a task as "done", verify:

- [ ] Did I do _exactly_ what the user asked?
- [ ] Are there zero lint/type errors?
- [ ] Have I tested/verified the change successfully?
