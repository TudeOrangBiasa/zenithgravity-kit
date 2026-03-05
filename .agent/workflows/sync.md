---
description: Run memory sync to detect installed UI component formats and keep AI design state updated.
---

# /sync - Synchronize AI System Memory

$ARGUMENTS

## Goal

Ensure the AI's internal design context (`.agent/memory/design-system.md`) matches the exact current state of the main `package.json` and components directory.

## Steps

0. Understand that `/sync` (or `/sync-memory`) is a maintenance command to rebuild local artifacts.
1. Execute `python .agent/scripts/sync_memory.py` via the local terminal execution tool. Wait for completion.
2. Read the newly generated `.agent/memory/design-system.md` file using `view_file` to observe what components/UI kits were detected.
3. Present a brief markdown summary table back to the user detailing the newly detected UI Kits and the count of available local UI components.

## Output

- A confirmation message that the design system memory is now up-to-date with the repository's real-world constraints.
