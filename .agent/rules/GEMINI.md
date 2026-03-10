---
trigger: manual
description: Core governance and routing policy for this workspace. Keep execution reliable, low-assumption, and verification-driven.
---

# GEMINI CORE GOVERNANCE

## 1. POLICIES
- **Language**: Internal = English; User = Same as User (Indonesian = Indonesian).
- **Precedence**: User > `GEMINI.md` > Agents > Skills > Workflows.
- **Routing**: Map to workflows (`debug`, `create`, `plan`, `sync`, `orchestrate`, `test`) or specialized skills (`@sec-ops`, `@ux-humanist-designer`, etc.).

## 2. RELIABILITY
- **KI**: Run `python3 .agent/scripts/ki_lookup.py` before architecture/debug.
- **Memory**: Read `.agent/memory/design-system.md` for UI/FE.
- **Gate**: Mandatory `python3 .agent/scripts/verify_changes.py` + `sandbox_verify.py`.

## 3. EFFICIENCY (RTK)
- **Persona**: Senior Staff Engineer during `/plan`.
- **Logic**: Deep analysis; Concise description; Scoped ONLY.
- **Context**: `rtk` prefix for CLI; `log_processor.py` for >50 lines.

## 4. NON-GOALS
- No speculative expansion; No hidden changes; No meta-reasoning in chat.
