# Extending Zenithgravity-kit

`zenithgravity-kit` ships with a set of battle-tested rules (`clean-code`, `frontend-design`, `orchestrator`). To tailor the AI to your specific backend (e.g., Spring Boot, Go DDD), internal company APIs, or custom workflows, you can extend the `.agent/` directory.

## 1. Modular Capabilities (`.agent/skills/`)

Skills represent specific knowledge domains, formatting rules, or behavioral adjustments. The IDE dynamically discovers skills by recursively scanning the `.agent/skills/` directory for files named `SKILL.md`.

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

**Note:** Skills can also be used as "LLM Roleplay" personas (e.g., a "socratic-tutor" skill that forces the AI to never give direct answers but ask guiding questions instead).

## 2. Execution Coordinators & Personas (`.agent/agents/`)

While `skills/` contain the "how-to", `agents/` define "who" is performing the work and their overarching mission. Agents combine multiple skills and determine which tools the AI is allowed to use.

Use this folder to create advanced orchestrators or specialized operators (e.g., `security-auditor.md`, `database-architect.md`).

1. Create a markdown file like `.agent/agents/database-architect.md`
2. Add YAML frontmatter defining the available `tools` and required `skills`:

```yaml
---
name: database-architect
description: Use for designing schemas, migrating databases, and evaluating DB performance.
model: inherit
tools: Read, Grep, Bash, Edit, Write
skills: model-consistency, clean-code, systematic-debugging
---
# Database Architect
## Mission
Ensure schema designs are normalized, performant, and safe.
```

## 3. Global Routing & Governance (`.agent/rules/`)

The `rules/` directory contains always-on governance, primarily `GEMINI.md`. All extensions to core routing logic should go here.

To map new natural language intents to workflows or skills, modify `.agent/rules/GEMINI.md`:

```markdown
## 3) Routing Policy

- "audit security", "find vulnerabilities" -> execute .agent/workflows/security-scan.md
```

## 4. State Anchors & Context Injection (`.agent/memory/`)

The `memory/` directory stores persistent context that the AI should consult before making decisions. It acts as an anchor against "AI drifting" over long conversations.

To use memory:

1. Create a context file, e.g., `.agent/memory/api-endpoints.md`.
2. Reference this memory file from your `skills/` or `agents/` instructions. For example: "You MUST read `.agent/memory/api-endpoints.md` before writing data fetching logic."

## 5. Custom Workflows (`.agent/workflows/`)

Workflows are step-by-step sequential recipes triggered by a slash command or mapped intent.

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

## 6. Automation Helpers (`.agent/scripts/`)

Place programmable utilities (Python, Node.js, Bash scripts) here. These scripts are typically invoked by workflows or agents to gather localized context, verify states, or automate terminal tasks (e.g., `scripts/detect_stack.py` to identify frameworks).
