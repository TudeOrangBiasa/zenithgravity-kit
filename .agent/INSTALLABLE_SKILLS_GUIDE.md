# Framework Agnostic Extension Guide

This native kit is framework agnostic. The core skills (`behavioral-modes`, `orchestrator`, `quality-assurance`, `system-architect`, `database-architect`, `api-architect`, `sec-ops`, `devops-architect`, `systematic-debugging`, `automation-engineer`, `clarify-first`, `logic-critic`, `self-healer`, `intellegent-routing`, `verification-gate`, `brainstroming`) apply to Python, Go, PHP, or JavaScript.

## The "Installable Skills" Concept

When you drop this `.agent` folder into a new project, you can "install" specific skills that teach the AI exactly how to write code for your specific stack.

### How to Install a Project-Specific Skill (Manual)

1. Identify the main framework of your project (e.g., Next.js).
2. Create a folder: `.agent/skills/nextjs-expert/`.
3. Create `SKILL.md` inside it. Add hard rules about how to write Next.js according to your preferences.

### How to Install a Skill via Smithery (Automated)

Install remote community skills directly into this architecture using the [Smithery CLI](https://smithery.ai). The `.agent` directory follows standard Agentic formats, ensuring seamless installations.

**Example: Installing the `humanizer` skill by @blader:**

```bash
npx @smithery/cli@latest skill add davila7/humanizer --agent antigravity
```

*This command automatically downloads and mounts the `humanizer` skill into your `.agent/skills/` directory.*

### Example: Custom `nextjs-expert` Skill

```yaml
---
name: nextjs-expert
description: Use when writing or modifying Next.js code, React components, or API routes.
---
# NEXTJS EXPERT
- **Structure**: Mandatory App Router (`app/`).
- **Components**: Server components by default; `"use client"` only for state/effects.
- **Data**: Native `fetch` only (No Axios).
```

### Example: Installing a `laravel-patterns` Skill

```yaml
---
name: laravel-patterns
description: Use when writing PHP, Laravel controllers, models, or Eloquent queries.
---
# LARAVEL PATTERNS
- **Logic**: Fat Models / Skinny Controllers.
- **Validation**: Strict Form Requests.
- **CLI**: Mandatory `artisan` for migrations.
```

## Why This Architecture Wins

- **Token Efficient**: Projects that don't use Laravel don't load Laravel instructions. Projects that don't use React don't load React instructions.
- **Pluggable**: You can copy-paste specific `installable skills` from project A to project B depending on the tech stack.
- **Stable Base**: The core of the AI (how it thinks, plans, and verifies) remains perfectly consistent across all languages.
