---
name: clarify-first
description: Use when a user request is ambiguous and different interpretations would lead to significantly different implementations, architectures, or risk levels. Trigger on: missing scope, unclear data model, undefined API contract, vague "make it better" instructions, or any request where confidence is below 80%. Do NOT trigger on obvious, low-risk, single-file tasks.
metadata:
  version: 1.2.0
  priority: medium
---

# CLARIFY FIRST

## TRIGGER CONDITIONS
- Ambiguous acceptance criteria with divergent implementation paths.
- High-risk operations (schema migration, auth change, major refactor) with unclear intent.
- Scope not defined (which module? which endpoint? which environment?).

## POLICY
- Ask 1-3 precise, numbered questions only.
- Provide a sensible default for fast confirmation (e.g., "I'll assume X unless you say otherwise").
- Skip if action is obvious/low-risk per `GEMINI.md` **Lazy Read** principle.
- **DONT** block progress with noise or over-clarify simple tasks.

## ANTIGRAVITY ALIGNMENT
- Aligns with `GEMINI.md` **ARTIFACT-FIRST** constraint — do not write code until scope is confirmed.
- After receiving answers, route to the appropriate specialist skill (`@system-architect`, `@api-architect`, etc.).
