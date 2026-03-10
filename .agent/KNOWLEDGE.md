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
- **ADR 006: State Anchors via memory/**: The `.agent/memory/` structure is used to inject persistent context (such as design system preferences or established API contracts) explicitly before execution, preventing context loss and style drift across continuous sessions.

- **ADR 007: Cross-Platform Utility Porting**: Critical framework scripts (like `verify_changes`) must be written in Python to ensure compatibility across Linux, macOS, and Windows.
- **ADR 008: High-Density Instruction Formatting**: All agentic instructions (Skills, Rules, Profiles) must prioritize density over readability for humans to maximize context window utility for code.

_(Add more project-specific knowledge here as the project evolves)_
