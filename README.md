# Zenithgravity-kit 🚀

An **Agentic Architecture Framework** designed to transform idle LLMs into disciplined, domain-aware Software Engineers.

> Stop fighting AI prompt amnesia, "AI UI slop", and robotic writing. This kit patches standard AI execution environments (like Antigravity IDE) by injecting State Anchors, Full-Spectrum Auto-Routing, and modular skillsets directly into your codebase.

## 🌟 Core Features

- **Full-Spectrum Auto-Routing**: Say goodbye to manual slash commands. Natural language intents are automatically mapped to specialized roles (`@system-architect`, `@database-architect`, `@devops-architect`, `@systematic-debugging`).
- **Impeccable UI Integration**: Deep integration with [Impeccable](https://impeccable.style/) by Paul Bakaus. The `frontend-design` core skill plus 17 actionable steering commands (`/polish`, `/delight`, `/bolder`) prevents generic "AI UI slop".
- **Cross-Platform Verification**: Robust Python 3 scripts ensure zero-blind execution logic and memory syncing across Linux, macOS, and Windows.
- **Context Compression**: Integrates with [Rust Token Killer (`rtk`)](https://github.com/rtk-ai/rtk) to shrink massive CLI outputs and prevent context window exhaustion.

## 📚 Deep-Dive Documentation

- [Architecture & Theory (The "Why")](docs/ARCHITECTURE.md)
- [How to Extend with Smithery & Custom Skills](.agent/INSTALLABLE_SKILLS_GUIDE.md)
- [Codebase Map & Directory Structure](CODEBASE.md)
- [Native Agent Architecture](.agent/ARCHITECTURE.md)

---

## ⚙️ How It Works (The Pseudocode Loop)

Instead of fine-tuning models, this kit uses "Behavioral Routing". When you chat with the AI, the operation acts like this:

```text
ON USER_PROMPT:
  // 1. Intent Mapping (GEMINI.md)
  IF prompt touches "Frontend" OR "UI":
     APPLY Skill('frontend-design' -> "Impeccable Architectural Constraints")
     READ Memory('.agent/memory/design-system.md')

  IF prompt touches "Backend" OR "API" OR "Database":
     APPLY Skill('system-architect' -> "Clean Architecture / DDD")
     APPLY Skill('database-architect' -> "Normalization & No N+1")
     READ Memory('.agent/memory/system-architecture.md')
     
  // 2. Security & Verification
  APPLY Skill('sec-ops' -> "Zero Trust & OWASP Hardening")
  RUN 'scripts/verify_changes.py' -> "Zero Blind Execution"

  // 3. Execution
  GENERATE Code
```

This guarantees that **every single output** is rigorously aligned with your exact project dependencies and architectural standards.

---

## 🛠️ Installation & Extensions

### 1. Initialize the Kit

You can inject this architecture into any new or existing project with a single command. It will safely merge into an existing `.agent` directory without overwriting your custom extensions.

```bash
npx zenithgravity-kit@latest init
```

*Or install globally for faster access:*
```

Once installed, use the commands directly:
```bash
zenithgravity init
zenithgravity readme
```

### 2. Extend with Smithery CLI

This framework is 100% compatible with the [Smithery](https://smithery.ai) ecosystem for third-party skills. You can install capabilities like the `humanizer` directly:

```bash
npx @smithery/cli@latest skill add davila7/humanizer --agent antigravity
```

> **⚠️ Required Dependencies**: Zenithgravity relies on `rtk` (Rust Token Killer) for compression, and `python3` for cross-platform scripts. Ensure both are available in your PATH.
