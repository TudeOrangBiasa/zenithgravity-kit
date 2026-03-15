---
name: brainstorming
description: Socratic questioning protocol and user communication mandates. Use this skill when requirements are ambiguous or missing to prevent guessing.
metadata:
  version: 2.2.0
  priority: high
---

# BRAINSTORMING (Socratic Gate)

## MANDATORY RULES
- **Suppress Instincts**: DONT build incomplete requests (e.g., "make a dashboard").
- **Ask 1-3 Questions** (calibrated to ambiguity level):
  - **Simple/local tasks**: Ask 1 focused question only.
  - **Feature/component tasks**: Ask 2 questions — Purpose + Scope.
  - **Architecture/multi-system tasks**: Ask all 3 — Purpose + Users + Scope.
  - Default 3: **Purpose** (business problem/goal), **Users** (target demographic), **Scope** (technical constraints/APIs).
- **Wait**: No design/implementation until user responds.

## ERROR HYGIENE
- Max 2 random fix attempts for CLI failures.
- Present error concisely -> Offer trade-offs -> Let user choose path.
- *Rule*: Produce data, not assumptions.

## ANTIGRAVITY ALIGNMENT
- Directly enforces `GEMINI.md` **ARTIFACT-FIRST** constraint.
- After user responds, generate Implementation Plan artifact before writing any code.
- Route to `@clarify-first` if a single targeted question would unblock progress faster.
