# Zenithgravity-kit 🚀

Disciplined, domain-aware Agentic Engineering.

This kit patches standard AI execution environments (like Antigravity IDE) by injecting State Anchors, Deep Planning rules, and modular skillsets directly into your codebase.

## 🌟 Core Features

- **Full-Spectrum Auto-Routing**: Natural language intents map to specialized roles (`@system-architect`, `@database-architect`, `@devops-architect`, `@systematic-debugging`).
- **Impeccable UI Integration**: Core `frontend-design` skill with 17 actionable steering commands (`/polish`, `/audit`, `/delight`) to combat "AI UI slop".
- **Cross-Platform Verification**: Python 3 scripts ensure zero-blind execution logic and memory syncing across Linux, macOS, and Windows.
- **Context Compression**: Integrates with [RTK (Rust Token Killer)](https://github.com/rtk-ai/rtk) to shrink massive CLI outputs.

## 📚 Documentation

- [Architecture & Theory](docs/ARCHITECTURE.md)
- [Extending the Architecture](docs/EXTENDING.md)
- [Installable Skills Guide](.agent/INSTALLABLE_SKILLS_GUIDE.md)
- [Codebase Map](CODEBASE.md)

---

## ⚙️ Execution Loop (Pseudocode)

The framework uses "Behavioral Routing" to process prompts:

```text
ON USER_PROMPT:
  // 1. Intent Mapping (GEMINI.md)
  IF prompt matches "plan" OR "design":
     ACTIVATE Workflow('.agent/workflows/plan.md')
     APPLY Skill('orchestrator' -> "Deep Planning Mandate")

  // 2. State Anchoring
  IF prompt touches "Frontend" OR "UI":
     APPLY Skill('frontend-design' -> "Impeccable Constraints")
     READ Memory('.agent/memory/design-system.md')

  IF prompt touches "Backend" OR "API" OR "Database":
     APPLY Skill('system-architect' -> "Clean Architecture")
     APPLY Skill('api-architect' -> "RESTfulness")
     READ Memory('.agent/memory/system-architecture.md')

  // 3. Verification
  APPLY Skill('sec-ops' -> "OWASP Hardening")
  RUN 'scripts/verify_changes.py' -> "Zero Blind Execution"

  // 4. Execution
  GENERATE Code
```

---

## 🛠️ Installation & Extensions

### CLI Initialization

Inject this architecture into any project. It merges into an existing `.agent` directory without overwriting custom extensions.

```bash
npx zenithgravity-kit@latest init
```

### Global Installation

```bash
npm install -g zenithgravity-kit@latest
```

Once installed, use:
```bash
zenithgravity init
zenithgravity readme
```

### Extension via Smithery

Zenithgravity is compatible with the [Smithery](https://smithery.ai) ecosystem for third-party skills.

```bash
npx @smithery/cli@latest skill add davila7/humanizer --agent antigravity
```

> **⚠️ Requirements**: Zenithgravity relies on `rtk` (Rust Token Killer) for compression and `python3` for verification scripts. Ensure both are in your PATH.
