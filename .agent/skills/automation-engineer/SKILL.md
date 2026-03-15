---
name: automation-engineer
description: Use when creating Bash/shell scripts, automating CI/CD routines, writing cron jobs, resolving Git PR threads via CLI, or performing any shell-based automation task. Triggers on phrases like "write a bash script", "automate this", "shell command", "cron job", "git automation", or "CI pipeline step".
metadata:
  version: 1.2.0
  priority: medium
---

# AUTOMATION ENGINEER

## BASH STANDARDS
- **Boilerplate**: `set -euo pipefail`.
- **Safety**: Use `"$@"` for forwarding; absolute variables only.
- **Tools**: `rsync` over `cp`; `find -exec` over `for` loops.
- **DONT**: Use Bash for complex logic if Python/Node/TF is more robust.

## RTK ENFORCEMENT
- All CLI validation commands must use `rtk` prefix: `rtk git status`, `rtk gh pr view <num>`.
- Filter build/test output: `rtk lint`, `rtk vitest run`, `rtk cargo test`.

## TESTING (BATS)
- Associate production scripts with BATS suites (`tests/*.bats`).
- Mandatory `setup()`/`teardown()` with isolated `mktemp`.
- Test Happy Path (0) and Error Path (non-zero).

## GIT AUTOMATION
- CLI: `rtk gh pr view` + GraphQL for comment parsing.
- Conflict Resolution: checklist-driven; parallel processing for monorepos.
