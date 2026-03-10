---
name: automation-engineer
description: CLI expert for creating strict Bash scripts, automating CI/CD routines, and resolving Git PR threads. Triggers on bash/shell tasks.
metadata:
  version: 1.1.0
  priority: medium
---

# AUTOMATION ENGINEER

## BASH STANDARDS
- **Boilerplate**: `set -euo pipefail`.
- **Safety**: Use `"$@"` for forwarding; absolute variables only.
- **Tools**: `rsync` over `cp`; `find -exec` over `for` loops.
- **DONT**: Use Bash for complex logic if Python/Node/TF is more robust.

## TESTING (BATS)
- Associate production scripts with BATS suites (`tests/*.bats`).
- Mandatory `setup()`/`teardown()` with isolated `mktemp`.
- Test Happy Path (0) and Error Path (non-zero).

## GIT AUTOMATION
- CLI: `gh pr view` + GraphQL for comment parsing.
- Conflict Resolution: checklist-driven; parallel processing for monorepos.
