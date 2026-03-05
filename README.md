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
     FORCE "Edge Case Analysis"

  // 2. State Anchoring
  IF prompt touches "Frontend" OR "UI":
     APPLY Skill('frontend-design' -> "Anti-Slop Constraints")
     READ Memory('.agent/memory/design-system.md')
     APPLY Detected_Frameworks (e.g., Shadcn, Tailwind)
     APPLY Base_Spacing (e.g., 8px)

  // 3. Execution
  GENERATE Code
```

This guarantees that **every single output** is rigorously aligned with your exact project dependencies and architectural standards.

---

## 🛠️ Installation & CLI

### Option A: Direct Usage (No Install)

You can inject this architecture into any new or existing project with a single command:

```bash
npx zenithgravity init
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
