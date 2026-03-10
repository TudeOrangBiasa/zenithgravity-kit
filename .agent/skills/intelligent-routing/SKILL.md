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
- No meta-commentary ("I am analyzing...").
- Concise specialist activation.
- Ask 1 clarifying question if domain match is ambiguous.
- DONT over-route simple fixes.
