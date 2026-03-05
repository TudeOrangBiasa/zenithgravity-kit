---
name: intelligent-routing
description: Use when selecting the right execution path, agent, and skills for tasks that vary in complexity or domain.
metadata:
	version: 1.0.0
	priority: high
---

# Intelligent Routing Skill

## Objective

Route work to the smallest effective execution path while preserving quality. The AI acts as an intelligent Project Manager, automatically selecting the best specialist(s) without needing explicit user commands.

## Automatic Routing Protocol (ALWAYS ACTIVE)

Before responding to ANY user request, silently analyze the request:

1.  **Classify Intent (Auto-Routing)**: Map human requests to structured workflows:
    - _Intent: Debugging_ ("fix bug", "error here") ➡️ Load `.agent/workflows/debug.md`.
    - _Intent: Building_ ("create feature", "make a button") ➡️ Load `.agent/workflows/create.md`.
    - _Intent: Planning_ ("how to build", "design architecture") ➡️ Load `.agent/workflows/plan.md`.
    - _Intent: Other_ (simple QA, explanation) ➡️ Direct answer.
2.  **Detect Domains**: Identify required expertise (e.g., Security, Frontend, Mobile).
3.  **Auto-invoke**:
    - If domain-specific: Match to the appropriate skill (e.g., `security-auditor`).
    - Inform the user which workflow and skill are being applied.

## Response Format (MANDATORY)

When auto-selecting a role or skill, inform the user concisely before proceeding:

```markdown
🤖 **Applying knowledge of `@skill-name`...**

[Proceed with specialized response]
```

_(Do NOT say "I am analyzing your request". Do it silently.)_

## Routing Heuristics

- Simple/local task -> direct execution.
- Multi-file or high-uncertainty task -> `project-planner` + `orchestrator`.
- Domain-specific task -> activate matching specialist skill.

## Conflict Handling

If two domains match with similar confidence:

1. Ask one concise clarifying question, or
2. Start with the lower-risk path and declare assumptions.

## Manual Override

- Allow explicit activation with `@skill-name`.

## Non-Goals

- Do not trigger many skills by default.
- Do not over-route simple fixes.
