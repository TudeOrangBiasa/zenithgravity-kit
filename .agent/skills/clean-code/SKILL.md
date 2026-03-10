---
name: clean-code
description: Pragmatic coding standards - concise, direct, no over-engineering, no unnecessary comments.
metadata:
  version: 2.1.0
  priority: high
---

# CLEAN CODE

## CORE RULES
- **Working Code > Essay**: Implement/Fix first; avoid long pre-execution essays.
- **SRP & Flat**: Max 2 levels nesting; Guard Clauses over nested if-else.
- **Self-Documenting**: Intent-revealing names (`hasPermission`) over logic comments.
- **YAGNI**: No over-engineering or premature abstraction.

## ECOSYSTEM CHECK (`CODEBASE.md`)
- Check imports/dependents before change.
- Update all affected files in SAME task boundary.

## COMPLETION GATE
- [ ] Match user request 100%?
- [ ] Zero lint/type errors?
- [ ] Verified/Tested results?
