---
name: intelligent-routing
description: Use when selecting the right execution path, agent, and skills for tasks that vary in complexity or domain.
metadata:
  version: 1.1.0
  priority: high
---

# INTELLIGENT ROUTING

## AUTO-ROUTING (SILENT)
1. **Intent mapping**: Debug (`debug.md`), Build (`create.md`), Plan (`plan.md`).
2. **Domain match**: Security, UX, API, etc.
3. **Notify User**: "🤖 Applying knowledge of `@skill-name`..."
4. **Heuritics**: Local = Direct; High-Uncertainty = Orchestrator; Domain-Specific = Specialist.

## RULES
- **RTK Enforcement (CRITICAL)**: NEVER use standard `cat`. ALWAYS use `rtk` for CLI commands when reading files (e.g., `rtk cat filename`). Non-compliance will cause context overflow.
- **Memory Addressing**: When reading memory, ALWAYS use absolute paths from the project root (`.agent/memory/design-system.md`). NEVER look for or create `.agent/memory` in subdirectories like `FE/` or `BE/`.
- No meta-commentary ("I am analyzing...").
- Concise specialist activation.
- Ask 1 clarifying question if domain match is ambiguous.
- DONT over-route simple fixes.

## SKILL MAPPING UPDATES
- **UI/UX Design**: Route all frontend visual design tasks to `@frontend-design`. It enforces impeccable, non-slop aesthetic standards.

## AUTONOMOUS IMPRECCABLE TRIGGERING
Do **NOT** wait for the user to type `/commands`. If the user's natural language request matches these intents, **automatically** route to and execute these Impeccable skills:
- **"Make it look better" / "Improve UI"** -> `@polish` (general cleanup) or `@delight` (add joy/micro-interactions).
- **"Check for issues" / "Accessibility"** -> `@audit` (runs strict a11y, perf, and responsiveness checks).
- **"It looks boring" / "Make it pop"** -> `@bolder` (amplifies visual interest) or `@animate` (adds motion).
- **"It's too much" / "Simplify it"** -> `@quieter` (tones down) or `@distill` (strips to essence).
- **"Fix the text" / "Better wording"** -> `@clarify` (improves UX copy/error messages).
- **"Make it responsive" / "Mobile version"** -> `@adapt` (handles device breakpoints).
- **"Create a new page/component"** -> Always start with `@frontend-design` for the baseline layout, then optionally follow up with `@colorize` or `@polish`.

## AUTONOMOUS ENGINEERING TRIGGERING
Do **NOT** wait for explicit commands. If the user's request matches these engineering intents, **automatically** route to:
- **"Design the backend" / "Restructure code"** -> `@system-architect` (enforces Clean Architecture, DDD boundaries, and modularity).
- **"Create an endpoint" / "Payloads"** -> `@api-architect` (enforces REST/GraphQL standards, pagination, and JSON envelopes).
- **"Design schema" / "Query is slow"** -> `@database-architect` (enforces normalization, migrations, and N+1 prevention).
- **"Fix this crash" / "Why is it failing?"** -> `@systematic-debugging` (enforces 5-Whys root cause isolation over trial-and-error).
- **"Check security" / "Review PR"** -> `@sec-ops` (enforces OWASP top 10 and severity-rated code reviews).
- **"Deploy this" / "CI/CD" / "Dockerize"** -> `@devops-architect` (enforces immutable containers and GitHub Actions/GitLab CI).
- **"Write a bash script" / "Automate this"** -> `@automation-engineer` (enforces strict bash idempotency and Bats testing).
- **"Connect to Slack/GitHub/DB"** -> `@mcp-agent` (leverages Model Context Protocol integration).
- **"Write documentation" / "Edit this text" / "Make it sound human"** -> `@humanizer` (strips robotic AI-slop like "delve", "testament", "pivotal", and "moreover" from generated content).
