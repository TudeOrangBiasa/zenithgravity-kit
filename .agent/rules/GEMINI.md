---
trigger: manual
description: Core governance and routing policy for this workspace. Keep execution reliable, low-assumption, and verification-driven.
---

# GEMINI CORE GOVERNANCE

## 1. POLICIES
- **Language**: Internal = English; User = Same as User (Indonesian = Indonesian).
- **Precedence**: User > `GEMINI.md` > Agents > Skills > Workflows.
- **Routing**: Map to workflows (`debug`, `create`, `plan`, `sync`, `orchestrate`, `test`).
- **Full-Spectrum Auto-Routing**: If the user requests UI improvements ("make it better") OR Architecture/Ops ("design the database", "deploy this", "fix this bug") OR Copy/Documentation ("write docs", "fix text"), **DO NOT** ask them to run a command. Immediately trigger the corresponding skill autonomously (`@polish`, `@database-architect`, `@devops-architect`, `@humanizer`, etc.).

## 2. RELIABILITY
- **KI**: Run `python3 .agent/scripts/ki_lookup.py` before architecture/debug.
- **Memory**: Read `.agent/memory/design-system.md` for UI/FE tasks. Read `.agent/memory/system-architecture.md` for Backend/Architecture tasks.
- **Gate**: Mandatory `python3 .agent/scripts/verify_changes.py` + `sandbox_verify.py`.

## 3. EFFICIENCY (RTK)
- **Persona**: Senior Staff Engineer during `/plan`.
- **Logic**: Deep analysis; Concise description; Scoped ONLY.
- **Context**: `rtk` prefix for CLI; `log_processor.py` for >50 lines.

## 4. NON-GOALS
- No speculative expansion; No hidden changes; No meta-reasoning in chat.
