# Native .agent Architecture

## Purpose

A low-effort, high-reliability native kit for Antigravity IDE with stable routing and reduced model drift.

## Structure

- `rules/` -> always-on governance (`GEMINI.md` only)
- `agents/` -> execution coordinators for simple vs complex task modes
- `skills/` -> modular capabilities. Divided conceptually into:
  - **Core Skills**: Framework-agnostic (e.g., `orchestrator`, `ux-humanist-designer`, `system-architect`, `database-architect`, `api-architect`, `sec-ops`, `devops-architect`). These ship with the base kit.
  - **Installable Skills**: Framework/stack-specific (e.g., `laravel-expert`, `react-patterns`). Added per-project.
- `memory/` -> custom state anchors (persistent context injection)
- `workflows/` -> deterministic step-by-step operational recipes
- `scripts/` -> optional automation helpers

## Load Strategy

1. `rules/GEMINI.md` (Core governance & Intent Mapping)
2. Agent selection (`orchestrator` / `project-planner`)
3. Skill activation by semantic relevance, Intent Mapping, or `@skill-name`
4. Workflow execution (Auto-triggered by conversational intent without slash commands)

## Built-In Capabilities

- **Auto-Discovery**: `scripts/detect_stack.py` runs before planning/creation to identify Native vs Docker/DDEV environments.
- **Auto-Routing**: Natural language requests map directly to `workflows/` via `.agent/skills/intelligent-routing/`.
- **Terminal Interaction Protocol**: Enforced zero blind-execution rules (always verify output, use `-y` flags).

## Complexity Gate

- Trivial/local task: direct `/create`
- Multi-file or ambiguous task: `/plan` -> `/orchestrate`
- Defect task: `/debug`
- Validation handoff: `/test`

## Language Contract

- Internal docs in `.agent/**`: English only
- User interaction: follow user language

## Design Constraints

- Keep always-on text compact.
- Prefer progressive disclosure via skills.
- Prioritize verifiable outcomes over speculative reasoning.

## Extension Patterns

### Detailed Guide

For a comprehensive guide on extending agents, rules, memory, scripts, skills, and workflows, please refer to the dedicated documentation at `docs/EXTENDING.md`.

### Adding a New Skill

1. Create a new folder: `.agent/skills/<skill-name>/`
2. Create `.agent/skills/<skill-name>/SKILL.md` using the minimum template.
3. Define the `description` carefully, as this is how the AI auto-discovers the skill.

### Adding a New Agent

1. Create `.agent/agents/<agent-name>.md`.
2. Define the `tools` and `skills` the agent needs in the YAML frontmatter.
3. Register the new agent in `.agent/rules/GEMINI.md` for proper routing.
