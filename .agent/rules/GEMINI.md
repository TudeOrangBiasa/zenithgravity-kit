---
trigger: manual
description: Core governance and routing policy for this workspace. Keep execution reliable, low-assumption, and verification-driven.
---

# GEMINI Core Governance

## 1) Language Policy

- Internal artifacts in `.agent/**` MUST be written in English.
- User-facing conversation should follow the user language.
- If the user speaks Indonesian, answer in Indonesian.

## 2) Instruction Precedence

1. User explicit request
2. This file (`rules/GEMINI.md`)
3. Agent files (`agents/*.md`)
4. Skill files (`skills/**/SKILL.md`)
5. Workflow files (`workflows/*.md`)

If instructions conflict, resolve by precedence and state assumptions briefly.

## 3) Routing Policy

- **Intent Mapping (Auto-Workflow)**: Map natural language to workflows.
  - "fix this", "why error" -> execute `.agent/workflows/debug.md`
  - "build feature X", "create" -> execute `.agent/workflows/create.md`
  - "design architecture", "plan" -> execute `.agent/workflows/plan.md`
  - "sync memory", "update ui kit tracking" -> execute `.agent/workflows/sync.md`
- Use direct execution for simple, localized tasks.
- Trigger specialized skills by semantic match on `description`.
- Allow manual skill/workflow override via `@skill-name` or `/workflow`.

## 4) Reliability Policy (Anti-Hallucination)

- Do not invent files, APIs, outputs, or test results.
- Read relevant files before editing them.
- If context is uncertain, ask 1-3 precise questions or present assumptions explicitly.
- Prefer grounded claims tied to observable workspace state.
- **Design Memory**: For anything UI/Frontend related, you MUST read `.agent/memory/design-system.md` to ensure design consistency and framework/component literacy. Do not invent raw components if the UI kit provides them.

## 5) Verification Gate

- For code changes, run the most targeted validation first.
- Report what was verified and what remains unverified.
- Never claim completion without evidence of checks when checks are available.

## 6) Scope & Efficiency

- Solve only the requested scope.
- Avoid unrelated refactors and avoid unnecessary dependencies.
- Keep always-on rules concise to reduce token overhead.

## 7) Non-Goals

- No speculative architecture expansion.
- No hidden behavior changes outside the requested task.
- No verbose meta reasoning in user-facing responses.

## 8) Token Efficiency (RTK Protocol)

- **Context Compression**: When exploring the user's codebase, ALWAYS prepend high-output CLI commands with `rtk` to save 60-90% of token consumption (e.g. use `rtk ls`, `rtk git status`, `rtk grep`, `rtk pytest`, `rtk cat`).
- If `rtk` fails or is not installed, gracefully fall back to the standard command (`ls`, `git`, `cat`, etc) without complaining to the user.
