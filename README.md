# Zenithgravity-kit 🚀

An **Agentic Architecture Framework** designed to transform idle LLMs into disciplined, domain-aware Software Engineers.

> Stop fighting AI prompt amnesia and "AI slop". This kit patches standard AI execution environments (like Antigravity IDE) by injecting State Anchors, Deep Planning rules, and modular skillsets directly into your codebase.

## 📚 Deep-Dive Documentation

- [Architecture & Theory (The "Why")](docs/ARCHITECTURE.md)
- [How to Extend the Architecture (Agents, Skills, Memory, etc.)](docs/EXTENDING.md)
- [Codebase Map & Directory Structure](CODEBASE.md)
- [Native Agent Architecture](.agent/ARCHITECTURE.md)

---

## ⚙️ How It Works (The Pseudocode Loop)

Instead of fine-tuning models, this kit uses "Behavioral Routing". When you chat with the AI, the operation acts like this:

```text
ON USER_PROMPT:
  // 1. Intent Mapping (GEMINI.md)
  IF prompt matches "plan" OR "design":
     ACTIVATE Workflow('.agent/workflows/plan.md')
     APPLY Skill('orchestrator' -> "Deep Planning Mandate")
     FORBID "lazy bullet points"

  // 2. State Anchoring & Architecture Detection
  IF prompt touches "Frontend" OR "UI":
     APPLY Skill('ux-humanist-designer' -> "Mathematical Constraints & Anti-Slop")
     READ Memory('.agent/memory/design-system.md')

  IF prompt touches "Backend" OR "API" OR "Database":
     APPLY Skill('system-architect' -> "Clean Architecture / DDD")
     APPLY Skill('api-architect' -> "RESTfulness & Idempotency")
     APPLY Skill('database-architect' -> "Normalization & No N+1")
     READ Memory('.agent/memory/system-architecture.md')

  // 3. Security & Ops Check
  APPLY Skill('sec-ops' -> "Zero Trust & OWASP Hardening")
  APPLY Skill('devops-architect' -> "CI/CD & Immutable Containers")

  // 4. Execution
  GENERATE Code
```

This guarantees that **every single output** is rigorously aligned with your exact project dependencies and architectural standards.

---

## 🛠️ Installation & CLI

### Option A: Direct Usage (No Install)

> **⚠️ Required Dependency**: Zenithgravity 1.0.4+ relies on [`rtk` (Rust Token Killer)](https://github.com/rtk-ai/rtk) to perform Context Compression. Please install it first (`brew install rtk` or `cargo install --git https://github.com/rtk-ai/rtk`) before attempting agentic loops.

You can inject this architecture into any new or existing project with a single command:

```bash
npx zenithgravity-kit init
```

### Option B: Global Installation

For a faster experience, install the kit globally:

```bash
npm install -g zenithgravity-kit
```

Once installed, you can use the commands directly:

```bash
zenithgravity init
zenithgravity readme
```
