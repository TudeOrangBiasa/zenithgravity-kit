# Architectural Overview: Zenithgravity-kit

## 1. The Gap Analysis: Why this Kit Exists

Out of the box, AI IDEs (like Antigravity or Cursor) provide an execution environment: they can read files, run terminal commands, and edit code. However, the underlying Large Language Models (LLMs like Gemini 3.1 Pro or Claude 3.5 Sonnet) inherently suffer from two major flaws when left unguided:

1. **The Automation of Laziness**: LLMs prefer to summarize complex architectural changes into short 3-line bullet points rather than exhaustive technical plans.
2. **Amnesia & Generic Defaults (AI Slop)**: Every time you start a new chat, the LLM forgets your specific design tokens and relies on generic, average internet defaults (e.g., heavy drop shadows, Bootstrap blue).

**Zenithgravity-kit acts as an "Agentic Harness" that forces the LLM into a disciplined, professional-grade execution loop.** We do not fine-tune the model's weights; instead, we manipulate its behavior using a rigid directory of rules and states.

---

## 2. Core Concepts & Theory

### A. Roleplay & Behavioral Anchoring

LLMs are generalists. If you ask them to "write code", they write average code. If you ask them to "act as a Senior Staff Engineer", they activate specific parameters related to robustness and edge-cases.

- **_How Zenithgravity-kit uses this_**: When the user types `/plan`, the kit forces the AI into a "Deep Planning Mandate", strictly forbidding lazy bullet points and demanding edge-case analysis.

### B. State Anchoring (Memory)

An LLM has no memory of visual consistency between sessions.

- **_How Zenithgravity-kit uses this_**: We introduced `.agent/memory/design-system.md`. By mandating the AI to read this file before any Frontend task, the AI is "anchored" to a specific reality (e.g., Shadcn UI, 8px spacing, subtle layering).

---

## 3. The Execution Flow (How it Works)

When a user submits a prompt, the kit intercepts and routes the intent through a defined sequence:

```mermaid
graph TD
    A[User Prompt] --> B{GEMINI.md Routing Policy}

    B -->|Intent: Planning| C[.agent/workflows/plan.md]
    B -->|Intent: Bug Fix| D[.agent/workflows/debug.md]
    B -->|Intent: Update State| E[.agent/workflows/sync.md]
    B -->|Intent: UI Creation| F[Semantic Match]

    C --> G[Orchestrator Skill: Deep Planning Mandate]
    G --> Z[Execution / Output]

    F --> H[.agent/skills/frontend-design/SKILL.md]
    H --> I[Read: .agent/memory/design-system.md]
    I --> J[Apply Anti-Slop Rules & Component Literacy]
    J --> Z

    E --> K[Run: .agent/scripts/sync_memory.py]
    K --> L[Update memory file based on package.json]
```

## 4. The Anatomy of the Kit

- **`rules/GEMINI.md`**: The Constitution. It holds the highest authority, defining language policy, anti-hallucination rules, and the intent router.
- **`memory/`**: The State files. Keeps track of the project's actual dependencies so the AI doesn't hallucinate non-existent libraries.
- **`skills/`**: The Masks. Markdown files with YAML frontmatter containing specific domain expertise (e.g., `frontend-design`, `clean-code`).
- **`workflows/`**: The Pipelines. Step-by-step instructions for macro-tasks (e.g., `/create`, `/plan`).
- **`scripts/`**: The Truth Checkers. Python/JS scripts that provide factual workspace data to the AI (e.g., `detect_stack.py`, `sync_memory.py`).
