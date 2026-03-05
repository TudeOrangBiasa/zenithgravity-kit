# Skills Installation Contract (Project-Local)

This workspace uses project-local skills at `.agent/skills/<skill-name>/SKILL.md`.

## Minimum Skill Template
```yaml
---
name: my-skill
description: Use when ...
metadata:
  version: 1.0.0
  priority: medium
---
```

## Required Fields
- `name`: unique skill identifier
- `description`: actionable trigger phrase for auto-discovery

## Optional Fields
- `metadata`: structured custom data (example: version, priority)

## Folder Pattern
```
.agent/skills/
  <skill-name>/
    SKILL.md
    scripts/        # optional
    references/     # optional
    assets/         # optional
```

## Activation Rules
- Automatic: semantic match from `description`
- Manual override: `@skill-name`
- Conflict resolution: core rules -> agent -> skill -> workflow

## Authoring Guidelines
- Keep instructions specific and testable.
- Include non-goals to prevent scope drift.
- Avoid model-specific assumptions unless strictly needed.
