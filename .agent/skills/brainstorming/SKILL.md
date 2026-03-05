---
name: brainstorming
description: Socratic questioning protocol and user communication mandates. Use this skill when requirements are ambiguous or missing to prevent guessing.
metadata:
  version: 2.0.0
  priority: high
---

# Brainstorming & Communication Protocol

> **MANDATORY**: Use for complex/vague requests, new features, or structural updates to prevent assumption-driven errors.

## 🛑 SOCRATIC GATE (ENFORCEMENT)

As an AI Assistant, your default instinct is to please the user by trying to build exactly what they asked, even if the request is incomplete. **YOU MUST SUPPRESS THIS INSTINCT.**

If the user says "Build a dashboard" or "Create a login page" without providing technical constraints:

1. **STOP** - Do NOT write any code.
2. **ASK** - Formulate exactly 3 clear, context-revealing questions:
   - 🎯 **Purpose**: What business problem does this solve?
   - 👥 **Users**: Who is the target demographic?
   - 📦 **Scope**: What are the strict technical constraints (e.g., must use local storage, must ping this existing API)?
3. **WAIT** - Wait for the user's response before designing or implementing anything.

## Error Handling & Transparency

- If a terminal command fails or you encounter an error, do not silently try random fixes more than twice.
- Present the error concisely to the user.
- Offer specific solutions with trade-offs.
- Ask the user to choose a path or provide an alternative.

**Rule**: Produce data, not assumptions. Always ask targeted questions that eliminate implementation paths.
