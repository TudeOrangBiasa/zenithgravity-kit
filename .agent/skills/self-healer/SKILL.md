---
name: self-healer
description: Use when a terminal command fails with a non-zero exit code, throws a CLI error, crashes during build/test/deploy, or produces an unrecoverable traceback. Automatically retries before escalating to the user. Trigger on phrases like "command failed", "exit code 1", "error running", or any shell error output.
metadata:
  version: 1.1.0
  priority: high
---

# SELF-HEALER (Antigravity Harness)

## Goal
Prevent laziness by autonomously debugging failing terminal commands without immediately asking the user for help.

## Instructions
1. If a terminal command fails (exit code != 0), do NOT immediately `notify_user`.
2. Automatically analyze the traceback and error message.
3. Search for a fix using codebase search tools or knowledge items.
4. Apply the correction and re-run using `rtk` prefix (e.g., `rtk vitest run`, `rtk next build`).
5. **Iteration Limit**: Maximum 3 autonomous retry iterations. Only escalate to user after 3 distinct failed attempts.

## RTK ENFORCEMENT
- Always re-run failing commands with `rtk` prefix to get filtered, token-efficient output.
- Use `rtk err <cmd>` to isolate errors-only from verbose tooling output.
