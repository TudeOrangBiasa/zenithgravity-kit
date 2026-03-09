# Framework Agnostic Extension Guide

This native kit is designed to be **100% framework agnostic** out of the box. The core skills (`behavioral-modes`, `orchestrator`, `quality-assurance`, `ux-humanist-designer`, `system-architect`, `database-architect`, `api-architect`, `sec-ops`, `devops-architect`) apply equally well whether you are coding in Python, Go, PHP, or JavaScript.

## The "Installable Skills" Concept

When you drop this `.agent` folder into a new project, you can "install" specific skills that teach the AI exactly how to write code for your specific stack.

### How to Install a Project-Specific Skill

1. Identify the main framework of your project (e.g., Next.js).
2. Create a new folder: `.agent/skills/nextjs-expert/`.
3. Create `SKILL.md` inside it. In this file, you put hard rules about how to write Next.js _according to your preferences_.

### Example: Installing a `nextjs-expert` Skill

```yaml
---
name: nextjs-expert
description: Use when writing or modifying Next.js code, React components, or API routes.
---
# Next.js Expert Guidelines
- **Always use App Router**, never Pages Router.
- **Server Components by Default**: Only add `"use client"` when state or effects are strictly needed.
- **Data Fetching**: Use native fetch API instead of `axios`.
```

### Example: Installing a `laravel-patterns` Skill

```yaml
---
name: laravel-patterns
description: Use when writing PHP, Laravel controllers, models, or Eloquent queries.
---
# Laravel Patterns
- **Fat Models, Skinny Controllers**: Push business logic constraints to the model or dedicated service classes.
- **Validation**: Always use Form Requests instead of inline validation in controllers.
- **CLI-First**: Never create migrations manually, always use `artisan make:migration`.
```

## Why This Architecture Wins

- **Token Efficient**: Projects that don't use Laravel don't load Laravel instructions. Projects that don't use React don't load React instructions.
- **Pluggable**: You can copy-paste specific `installable skills` from project A to project B depending on the tech stack.
- **Stable Base**: The core of the AI (how it thinks, plans, and verifies) remains perfectly consistent across all languages.
