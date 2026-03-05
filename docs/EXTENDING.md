# Extending Zenithgravity-kit

Out of the box, `zenithgravity-kit` ships with a set of battle-tested rules (`clean-code`, `frontend-design`, `orchestrator`). However, to tailor the AI to your specific backend (e.g., Spring Boot, Go DDD) or internal company APIs, you should extend it.

## 1. Installing 3rd Party Skills & Agents

Antigravity IDE dynamically discovers skills by recursively scanning the `.agent/skills/` directory for files named `SKILL.md`.

To install a skill from GitHub, the Smithery API, or the community:

1. Create a new folder under `.agent/skills/`. E.g., `.agent/skills/golang-clean-architecture/`.
2. Inside that folder, create or copy the `SKILL.md` file.

**Requirements for Discovery:**
Your `SKILL.md` **MUST** include YAML frontmatter at the very top of the file:

```yaml
---
name: golang-clean-architecture
description: Use when writing Go code, designing backends, or dealing with the Domain layer.
metadata:
  version: 1.0.0
---
```

_(The IDE uses the `description` field for semantic matching. The better the description, the better the AI knows when to load your skill)._

## 2. Authoring Custom Personas & Agents

Skills don't have to just be "coding rules" (like _never use fat controllers_). They can also be entire **Personas** or **Behavioral Modes**.

For example, you can create `.agent/skills/socratic-tutor/SKILL.md`:

```yaml
---
name: socratic-tutor
description: Use when the user asks for an explanation, not code generation.
---
# The Socratic Method
When activated, you must NEVER give the user direct code answers.
Instead:
1. Ask them what they think the root cause is.
2. Provide hints.
3. Guide them to write the code themselves.
```

This demonstrates the power of **LLM Roleplay**. You are forcing the AI to switch from its generic helpful behavior into a strict teaching mode.

## 3. Creating Custom Workflows (`/command`)

Workflows are step-by-step sequences triggered by a slash command or mapped intent.

1. Create a new file in `.agent/workflows/`. E.g., `deploy.md`.
2. Write the steps clearly:

```markdown
---
description: Deploy the project to the staging server.
---

# /deploy - Staging Deployment Sequence

1. Step 1: Run `npm run test`.
2. Step 2: Run `npm run build`.
3. Step 3: Use the terminal to run `deploy.sh`.
```

3. Update `GEMINI.md` in the Routing Policy to map the intent:
   `"push to staging", "deploy" -> execute .agent/workflows/deploy.md`
