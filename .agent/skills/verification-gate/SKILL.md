---
name: verification-gate
description: Use for enforcing evidence-based completion through targeted checks, regression awareness, and concise reporting.
metadata:
  version: 1.3.0
  priority: high
---

# VERIFICATION GATE

## ORDERED CHECK SEQUENCE
Run checks in this order — stop and fix failures before proceeding to the next level:

1. **Type Check**: `rtk tsc` (TypeScript) or equivalent static analysis.
2. **Lint**: `rtk lint` — no ESLint/Biome violations allowed.
3. **Unit Tests**: `rtk vitest run` or `rtk cargo test` — failures = blocker.
4. **E2E/Integration**: `rtk playwright test` — only if scope touches user flows.
5. **Sandbox Gate**: `python3 .agent/scripts/sandbox_verify.py` — full structural check.
6. **Antigravity Gate**: `python3 .agent/scripts/verify_changes.py` — final sign-off.

## ANTIGRAVITY GATE
- Task is only "Complete" if ALL applicable levels above pass.
- Isolate new failures from pre-existing issues before reporting.

## REPORT FORMAT
```
## Verification Results
- TypeCheck: PASS / FAIL
- Lint: PASS / FAIL
- Unit Tests: PASS (N) / FAIL (N errors)
- E2E: PASS / SKIP / FAIL
- Residual Risks: <any unverified areas>
```

## DONT
- Fix unrelated tests unless requested.
- Claim success without terminal evidence.
