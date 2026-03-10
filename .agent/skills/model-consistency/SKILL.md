---
name: model-consistency
description: Use to reduce assumption drift, improve factual grounding, and keep execution behavior stable across model quality variance.
metadata:
  version: 1.1.0
  priority: high
---

# MODEL CONSISTENCY

## CERTAINTY Tiers
- **Certain**: Proceed.
- **Likely**: Proceed -> Verify immediately.
- **Uncertain**: Search or Ask User first.
- *Mandate*: Be intellectually honest; "I'm not sure, let me check."

## RULES
- **Anti-Assumption**: No hidden requirement assumptions; ask if ambiguous.
- **Read-Before-Edit**: Inspect target + context files before modification.
- **Evidence-Based**: Decisions must ground in observable files/tool output.

## TERMINAL PROTOCOL
- **No Assumption**: Verify exit codes + STDOUT/STDERR.
- **Mutation Check**: Use `list_dir` to confirm `rm`, `mkdir`, `mv` effects.
- **Non-Interactive**: Use `-y`, `--force`, `--no-fund` to prevent hanging.

## COMPLETION GATE
- Need validation evidence.
- Explicitly report residual risks.
