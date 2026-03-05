---
description: Build a concise execution plan for complex, risky, or ambiguous tasks before code changes.
---

# /plan - Execution Planning

$ARGUMENTS

## Goal

Produce a highly detailed, exhaustively researched execution plan. Do not be lazy. You must act as a Senior Staff Engineer.

## Steps

0. Run `python .agent/scripts/detect_stack.py .` to understand the language, framework, and environment constraints before planning.
1. Define objective and scope boundaries.
2. List all impacted files, components, and their dependencies (sub-streams).
3. Identify at least 3 critical edge cases, nuances, or potential blockers.
4. Break implementation into granular, ordered phases. For EACH phase, you MUST list specific sub-tasks. "Bullet point" summaries without depth are strictly forbidden.
5. Define verification checks for each phase.
6. Capture key risks and rollback approach.

## Output

- Actionable, highly-detailed checklist (Minimum 3 sub-tasks per phase).
- Edge Cases Analysis (Mandatory).
- Verification strategy per phase.
