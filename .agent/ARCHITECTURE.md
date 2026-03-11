# Native .agent Architecture

## Purpose
A low-effort native kit for Antigravity IDE with stable routing and reduced model drift.

## Structure
- `rules/` -> always-on governance (`GEMINI.md` only)
- `agents/` -> execution coordinators
- `skills/` -> modular capabilities
  - **Core**: Framework-agnostic (`orchestrator`, `frontend-design`, `system-architect`, `database-architect`, `api-architect`, `sec-ops`, `devops-architect`, `systematic-debugging`, `automation-engineer`, `humanizer`). Included in base kit.
  - **Extensions**: Framework-specific (`laravel-expert`, `nextjs-expert`). Installed via manual creation or [Smithery CLI](https://smithery.ai).
- `memory/` -> persistent context anchors 
- `workflows/` -> step-by-step sequential recipes
- `scripts/` -> python verification helpers

## Load Strategy
1. `rules/GEMINI.md` (Intent Mapping)
2. Agent selection (`orchestrator` / `project-planner`)
3. Skill activation (Auto-routed by intent)
4. Workflow execution

## Built-In Capabilities
- **Auto-Discovery**: `scripts/detect_stack.py` identifies environments (Native, Docker, testing frameworks) prior to planning.
- **Auto-Routing**: Natural language commands automatically map to `workflows/` via `.agent/skills/intelligent-routing/`.
- **Zero-Blind Execution**: `verify_changes.py` gates unverified commits.

## Complexity Gate
- Trivial/local task: direct `/create`
- Multi-file task: `/plan` -> `/orchestrate`
- Defect: `/debug`
- Validation: `/test`

## Language Contract
- Internal docs (`.agent/**`): English only
- User interaction: follow user language

## Design Constraints
- Prioritize high-density instructions (Rules > Prose).
- Use progressive disclosure via skills.
- Require verifiable CLI outcomes.

## Extension Patterns

Check `docs/EXTENDING.md` for a comprehensive guide on adding custom memory, scripts, and workflows.

### Adding a New Skill
1. Create `.agent/skills/<skill-name>/SKILL.md`.
2. Explicitly define trigger conditions in the `description` block for auto-routing.

### Adding a New Agent
1. Create `.agent/agents/<agent-name>.md`.
2. Register the agent in `.agent/rules/GEMINI.md` for proper routing.
