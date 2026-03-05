---
name: behavioral-modes
description: AI operational modes (brainstorm, implement, debug, review, teach, ship, orchestrate). Use to adapt behavior based on task type.
metadata:
  version: 1.0.0
  priority: high
---

# Behavioral Modes

This skill controls the "mental model" and effort depth of the AI to ensure token efficiency and avoid over-engineering.

## Adaptive Thinking (Proportional Effort)

Effort must scale with complexity. Do NOT apply the full investigation-plan-execute-verify cycle to a typo fix.

| Level          | When                                      | What to Do                                                          | Example             |
| -------------- | ----------------------------------------- | ------------------------------------------------------------------- | ------------------- |
| **Instant**    | One-liner fix, typo, rename               | Just do it. Lint check only.                                        | Fix typo            |
| **Light**      | Single-file change, simple feature        | Brief scan, implement, verify                                       | Add utility         |
| **Deep**       | Multi-file feature, debugging, API design | Investigate, plan, implement with per-file verification             | Auth system         |
| **Exhaustive** | Architecture redesign, security review    | Full investigation, multiple approaches, comprehensive verification | Framework migration |

### How to Calibrate

1. How complex is this? (Files involved, architectural impact)
2. Match effort level.

## Strategic Laziness (Minimal Sufficient Action)

1. **Read only what's needed** — Don't read the entire codebase to fix a typo.
2. **Make the smallest correct change** — Don't refactor adjacent code unless asked.
3. **Prefer standard library** — Don't add dependencies for things the language can do.
4. **Don't abstract prematurely** — Wait until a pattern repeats 3+ times.

## CLI-First Development

**NEVER** manually create config files for standard frameworks. Always use their built-in CLI tools.

- **Wrong**: Manually writing `package.json`, `Cargo.toml`, `go.mod`.
- **Right**: `npm init`, `cargo new`, `go mod init`.
