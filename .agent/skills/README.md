# 🧠 Agent Skills Architecture

This directory holds specific instructions for different tasks. Skills are localized rules that teach the AI how to write code according to your architectural standards, design systems, or tech stack.

## 🌟 Core vs. Extension Skills

- **Core Skills**: The foundational architecture that ships natively with Zenithgravity (e.g., `system-architect`, `database-architect`, `devops-architect`, `systematic-debugging`, `sec-ops`, `frontend-design`, `humanizer`, `skill-creator`, `rtk`). These enforce general software engineering discipline.
- **Extension Skills**: Framework or project-specific skills (e.g., `nextjs-expert`, `laravel-patterns`) that you add to tailor the AI to your exact stack.

## 🔌 Installing 3rd-Party Skills via Smithery

Zenithgravity is 100% compliant with the [Smithery](https://smithery.ai) specification. Instead of manually writing skills, you can pull community-curated expertise directly into your project:

```bash
npx @smithery/cli@latest skill add [namespace]/[skill-name] --agent antigravity
```

*Example: Installing the Humanizer skill to strip AI-slop from text:*
```bash
npx @smithery/cli@latest skill add davila7/humanizer --agent antigravity
```

## 🛠️ Authoring Custom Skills (Manual)

If you need private, project-specific rules, you can create them manually:

### Folder Pattern
```text
.agent/skills/
  your-skill-name/
    SKILL.md        # Required: The core instruction payload
    scripts/        # Optional: Executable helpers (e.g. bash/python scripts)
    references/     # Optional: Markdown examples or context files
```

### Required `SKILL.md` Template (YAML Frontmatter is Mandatory)
```yaml
---
name: your-skill-name
description: Explicitly state when the AI should use this skill (e.g. "Use when writing React components"). This string is used by the Auto-Router.
version: 1.0.0
---
# YOUR SKILL RULES
- **Constraint 1**: ...
- **Constraint 2**: ...
```

## 🔀 Full-Spectrum Auto-Routing

You **do not** need to manually call skills using slash commands. 

The framework utilizes **Full-Spectrum Auto-Routing** (via Intent Mapping in `GEMINI.md` and `intelligent-routing/SKILL.md`). The AI matches your natural language intent (e.g., "design the database", "fix the deployment", "make the UI look better") to the `description` of the skill and automatically activates the corresponding constraints (`@database-architect`, `@devops-architect`, `@frontend-design`).

If you wish to force a specific skill, you can use an explicit mention: `@your-skill-name`.
