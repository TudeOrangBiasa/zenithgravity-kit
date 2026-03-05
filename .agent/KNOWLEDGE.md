# Project Knowledge

This file contains project-specific logic, architectural decisions, and business rules that do not fit into the standard repository structure but are essential for the AI to understand.

## Known Constraints

- Keep token usage minimal. Rely on short, punchy rules rather than verbose descriptions.

## Architectural Decisions (ADR)

- **ADR 001: Progressive Skill Loading**: Instead of loading all agent instructions at once, we use a modular folder structure in `.agent/skills/`. The AI reads the index, then reads specific `SKILL.md` files on demand. This saves context tokens.
- **ADR 002: English-only Internal Docs**: `.agent` contents must be fully English to maximize token density, as tokenizers handle English more efficiently than Indonesian.
- **ADR 003: Auto-Discovery Environment**: Instead of guessing the tech stack or execution environment (Native vs Docker/DDEV), `workflows` must execute `detect_stack.py` first to inject context dynamically.
- **ADR 004: Natural Language Auto-Routing**: To enhance user experience, explicit slash commands (e.g., `/create`) are replaced with Intent Mapping inside `GEMINI.md` and `intelligent-routing`, allowing casual human language to trigger strict workflows behind the scenes.
- **ADR 005: Terminal Interaction Protocol**: To address the LLM's "Blind Execution Flaw" (assuming a command worked without checking), the `model-consistency` skill enforces mandatory verification of STDOUT/STDERR and the use of non-interactive flags (e.g., `-y`).

_(Add more project-specific knowledge here as the project evolves)_
