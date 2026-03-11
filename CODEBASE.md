# Codebase Map

This document maps the project architecture and component relationships.

## Directory Structure

- **`/.agent/`**: Native Agentic Kit root. Contains AI governance rules, personas, workflow recipes, and skills.
  - **`rules/`**: Contains only `GEMINI.md` (Highest priority, global routing & governance).
  - **`agents/`**: Core AI personas (e.g., orchestrator, project-planner).
  - **`skills/`**: Modular capabilities loaded dynamically via YAML frontmatter in `SKILL.md` files.
  - **`memory/`**: Custom state anchors for injecting persistent context (e.g., design systems, API endpoints).
  - **`workflows/`**: Sequential recipes for specific tasks (e.g., `/create`, `/plan`). Auto-triggered via Intent Mapping.
  - **`scripts/`**: Cross-platform Python automation tools like `detect_stack.py` and `verify_changes.py`.
  - **`logs/`**: (Ignored) Temporary execution logs.

## Key Dependencies & Interactions

1.  **Rule Enforcement Flow**: `GEMINI.md` applies globally -> Intent Mapping (Auto-Routing) -> Workflow or Specialist Skill.
2.  **Token Compression Flow**: CLI explorations are intercepted by `rtk` (Rust Token Killer) to compress heavy outputs, preventing context exhaustion.
3.  **Skill Loading**: The IDE automatically discovers and loads skills by parsing the YAML frontmatter (`name`, `description`) of all `SKILL.md` files. No central index file is needed.
4.  **Task Management**: The AI maintains local task states within `.gemini/` to avoid hallucinating progress.

## Global Conventions

- All internal `.agent/` documentation must be in **English**.
- Agent communications with the user must default to the **user's language** (e.g., Indonesian).
- Verification via targeted scripts must precede any completion claim.
