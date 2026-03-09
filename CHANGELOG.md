# Changelog

All notable changes to the **Zenithgravity-kit** project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.4] - 2026-03-09

### Added

- **UX Humanist Designer Skill**: Introduced `.agent/skills/ux-humanist-designer/SKILL.md` as the primary, token-efficient UI/UX reasoning engine.
- **Embedded Aesthetics**: Migrated UI kits and palette matrices directly into the single layout payload.
- **Database Architect Skill**: Added `.agent/skills/database-architect/SKILL.md` to enforce normalization, index strategies, and N+1 query prevention.
- **API Architect Skill**: Added `.agent/skills/api-architect/SKILL.md` to standardize REST patterns, JSON envelopes, and versioning.
- **SecOps Skill**: Added `.agent/skills/sec-ops/SKILL.md` to introduce strict code review protocols and vulnerability scanning (OWASP) with critical/important severity ratings.
- **DevOps Architect Skill**: Added `.agent/skills/devops-architect/SKILL.md` to enforce Container Immutability, CI/CD pipelines, and Observability patterns.
- **System Architect Skill**: Added `.agent/skills/system-architect/SKILL.md` to enforce structural boundaries like Clean Architecture, DDD, Modular Monoliths, and Atomic Design on backend and full-stack generations.
- **Systematic Debugging Skill**: Added `.agent/skills/systematic-debugging/SKILL.md` to enforce root-cause isolation (The "5 Whys") and eliminate AI trial-and-error guessing.
- **Automation Engineer Skill**: Added `.agent/skills/automation-engineer/SKILL.md` to enforce strict Bash idempotency, `Bats` testing, and Git parallel PR resolution operations.
- **RTK Protocol**: Added rule to `.agent/rules/GEMINI.md` to enforce prepending `rtk` (Rust Token Killer) to high-output CLI scans (ls, cat, grep, pytest) to compress context window consumption by 60-90%.
- **Architecture Memory Sync**: Upgraded `.agent/scripts/sync_memory.py` to recursively detect project topology up to depth 3, detect Testing & QA frameworks, map CI/CD footprint, and output a new `.agent/memory/system-architecture.md` anchor.

### Changed

- **Stack Detection Expansion**: `detect_stack.py` and `sync_memory.py` now specifically route the AI to use `system-architect` when backend frameworks or multiple architecture layers are found. This includes deep detection for Node (AdonisJS, Nuxt, Astro), PHP (Laravel, Symfony via composer), and Python (Django, FastAPI via requirements).
- **UI Stack Synchronization**: Updated `.agent/memory/design-system.md` interaction protocols. The agent is now forced to retrieve baseline UI Kit constraints from memory before determining aesthetic layouts.
- **Project Documentation Update**: Replaced all references of `frontend-design` with `ux-humanist-designer` across `README.md`, `INSTALLABLE_SKILLS_GUIDE.md`, and `ARCHITECTURE.md`.

### Removed

- **Old Frontend Skill**: Deprecated and deleted `.agent/skills/frontend-design/` as its capabilities have been superseded by the `ux-humanist-designer` skill.
- **Temporary Skills**: Deleted the `temp/` directory completely after successfully reviewing, evaluating, and extracting core cognitive patterns from `ui-ux-pro-max`, `frontend-ui-ux`, and `ux-researcher-designer`.

### Fixed

- **README Documentation**: Corrected the `npx` command to use the full package name (`npx zenithgravity-kit init`) to avoid 404 errors during initialization.

## [1.0.3] - 2026-03-05

### Added

- **Extension Documentation**: Completely updated `docs/EXTENDING.md`, `.agent/KNOWLEDGE.md`, `.agent/ARCHITECTURE.md`, and `CODEBASE.md` to document the entire `.agent/` directory structure, explicitly clarifying the distinction between `agents/` and `skills/`, and introducing the `memory/` directory as a custom feature folder for state anchors.
- **`readme` command**: Added a new command to the CLI (`zenithgravity readme`) to easily display the project's documentation in the terminal.
- **Global Installation Support**: Updated `README.md` with explicit instructions for global installation and direct CLI usage.

### Fixed

- **CLI Syntax Error**: Corrected a regression in `bin/cli.js` where the `printHelp` function declaration was accidentally removed.

## [1.0.1] - 2026-03-05

### Fixed

- **CLI Package Structure**: Moved `cli.js` to `bin/cli.js` and updated `package.json` (`main` and `bin` fields) to resolve NPM publish errors regarding invalid bin scripts.
- **NPM Publishing**: Cleaned up package references. Removed the `src/` directory which was redundant.

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
