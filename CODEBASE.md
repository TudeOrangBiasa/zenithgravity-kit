# Codebase Map

This document serves as the single source of truth for the AI to navigate this project's architecture and understand component relationships.

## Directory Structure & Responsibilities

- **`/.agent/`**: Native Agentic Kit root. Contains all AI governance rules, personas, workflow recipes, and skills.
  - **`rules/`**: Strictly contains ONLY `GEMINI.md` (Highest priority, global routing & governance).
  - **`agents/`**: Core AI personas/coordinators (e.g., orchestrator, project-planner).
  - **`skills/`**: Modular capabilities loaded dynamically via YAML frontmatter in `SKILL.md` files.
  - **`memory/`**: Custom state anchors for injecting persistent context (e.g., design systems, API endpoints).
  - **`workflows/`**: Step-by-step sequential recipes for specific tasks (e.g., `/create`, `/plan`). Auto-triggered via Intent Mapping.
  - **`scripts/`**: Automation tools including `detect_stack.py` (for Environment Auto-Discovery) and `verify_agent.py`.

## Key Dependencies & Interactions

1.  **Rule Enforcement Flow**: `GEMINI.md` applies globally -> Intent Mapping (Auto-Routing) -> Workflow or Specialist Skill.
2.  **Skill Loading**: The IDE automatically discovers and loads skills by parsing the YAML frontmatter (`name`, `description`) of all `SKILL.md` files. No central index file is needed.
3.  **Task Management**: The AI maintains local task states within `.gemini/` to avoid hallucinating progress.

## Global Conventions

- All internal `.agent/` documentation must be in **English**.
- Agent communications with the user must default to the **user's language** (e.g., Indonesian).
- Verification via targeted scripts must precede any completion claim.
