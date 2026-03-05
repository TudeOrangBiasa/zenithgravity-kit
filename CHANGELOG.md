# Changelog

All notable changes to the **Zenithgravity-kit** project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-03-05

### Added

- **Design System Memory (`.agent/memory/design-system.md`)**: Introduced a state anchor to maintain visual consistency across sessions and explicitly list component dependencies (like Shadcn, Tailwind).
- **Auto Memory Sync (`/sync`) Workflow**: Created `.agent/workflows/sync.md` and `.agent/scripts/sync_memory.py` to automatically analyze a target project's `package.json` and sync it to the AI's internal design memory.
- **Deep Planning Mandate**: Added strict rules to `.agent/skills/orchestrator/SKILL.md` forcing the AI to consider edge-cases, data streams, and output highly detailed execution plans rather than lazy bullet points.
- **Frontend Anti-Slop Constraint**: Updated `.agent/skills/frontend-design/SKILL.md` to prevent generic "AI UI slop" by forcing the AI to consult the design memory and use signature tokens (e.g., 8px spacing, subtle layering).
- **CLI Scaffolding**: Initialized `package.json`, `bin/`, and `src/` to begin wrapping the kit into an NPM package for mass distribution (`npx zenithgravity`).
- **Deep-Dive Documentation**: Created `docs/ARCHITECTURE.md` to explain Agentic Engineering theories/flowcharts and `docs/EXTENDING.md` to guide users on installing 3rd party skills from GiHub or Smithery.

### Changed

- **Routing Policy (`GEMINI.md`)**: Re-wrote the primary routing matrix to explicitly map intents (e.g., "sync memory" -> `/sync` workflow) and enforce early consultation of `memory/design-system.md` during frontend tasks.
- **Workflow /plan**: Re-configured the `plan.md` workflow to reject superficial analysis and act as a Senior Staff Engineer.

### Removed

- Removed `.temp/` repository (Design Memory and Interface Design folders) after successfully extracting their core cognitive rules into the localized AI-kit system.
