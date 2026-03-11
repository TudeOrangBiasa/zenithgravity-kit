---
description: Build a concise execution plan for complex, risky, or ambiguous tasks before code changes.
---

# /plan - Senior Staff Engineering Design

$ARGUMENTS

## Goal

Produce a high-standard Technical Design Document (TDD). You must act as a Senior Staff Engineer. Focus on system integrity, downstream impacts, and reliability.

## Steps

0. **Context Discovery**:
   - Run `python3 .agent/scripts/detect_stack.py .` to understand env constraints.
   - Run `python3 .agent/scripts/ki_lookup.py <topic>` to find relevant Knowledge Items. **DO NOT SKIP**.
1. **Objective & Non-Goals**: Define what is being solved and what is explicitly OUT of scope.
2. **Impact Analysis**: List impacted files and identify downstream dependencies that might break.
3. **Alternative Approaches**: Briefly describe at least one alternative way to solve this and why you chose the current path.
4. **Execution Phases**:
   - Break implementation into granular, ordered phases.
   - For EACH phase, list specific sub-tasks.
   - **Checklist Requirement**: Each plan MUST include:
     - [ ] Check dependencies & Imports
     - [ ] Update state/memory anchors
     - [ ] For UI/UX Tasks: Include `@frontend-design` layout phase and `@audit` / `@polish` quality gates
     - [ ] Run targeted validation script (`verify_changes.sh`)
5. **Rollback Strategy**: Define how to undo changes if something goes wrong.
6. **Verification Matrix**: Map each phase to a specific `rtk` or `verify_changes.sh` command.

## Output

- **Implementation Plan (TDD)**: A structured markdown document following the above sections.
- **Risk Assessment**: Identify at least 3 critical edge cases or blockers.
