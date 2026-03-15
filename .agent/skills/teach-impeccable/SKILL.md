---
name: teach-impeccable
description: One-time setup that gathers design context for your project and saves it to your AI config file. Run once to establish persistent design guidelines.
user-invokable: true
---

Gather design context for this project, then persist it for all future sessions.

## Step 1: Explore the Codebase

Before asking questions, thoroughly scan the project to discover what you can:

- **README and docs**: Project purpose, target audience, any stated goals
- **Package.json / config files**: Tech stack, dependencies, existing design libraries
- **Existing components**: Current design patterns, spacing, typography in use
- **Brand assets**: Logos, favicons, color values already defined
- **Design tokens / CSS variables**: Existing color palettes, font stacks, spacing scales
- **Any style guides or brand documentation**

Note what you've learned and what remains unclear.

## Step 2: Ask UX-Focused Questions

STOP and call the AskUserQuestionTool to clarify. Focus only on what you couldn't infer from the codebase:

### Users & Purpose
- Who uses this? What's their context when using it?
- What job are they trying to get done?
- What emotions should the interface evoke? (confidence, delight, calm, urgency, etc.)

### Brand & Personality
- How would you describe the brand personality in 3 words?
- Any reference sites or apps that capture the right feel? What specifically about them?
- What should this explicitly NOT look like? Any anti-references?

### Aesthetic Preferences
- Any strong preferences for visual direction? (minimal, bold, elegant, playful, technical, organic, etc.)
- Light mode, dark mode, or both?
- Any colors that must be used or avoided?

### Accessibility & Inclusion
- Specific accessibility requirements? (WCAG level, known user needs)
- Considerations for reduced motion, color blindness, or other accommodations?

Skip questions where the answer is already clear from the codebase exploration.

## Step 3: Write Visual Design Context

Synthesize your findings and the user's answers into a `## Design & Aesthetic Constraints` section.

**CRITICAL TYPOGRAPHY RULES**:
- **Base Size**: Force a minimum base font size of 16px (recommend 17px / 1.05x bump for dashboards/ERP to prevent eye strain).
- **Modular Scale**: Define a 5-size system (xs, sm, base, lg, xl).
- **Font Selection**: NEVER recommend generic fonts (Inter, Roboto, Arial, Open Sans). Recommend distinctive fonts (e.g., Instrument Sans, Onest, Lora) or native System Fonts (Segoe UI, -apple-system).

```markdown
### Users & Brand Personality
[Who they are, context, job to be done]
[Voice, tone, 3-word personality, emotional goals]

### Visual Identity Tokens
- **Color Palette**: [Semantic CSS variables or Hex codes: Primary, Secondary, Background, Muted, Accents]
- **Typography Scale**: [Specify Base size (e.g., 17px), Heading sizes (H1, H2, H3), and Modular Scale]
- **Typography Family**: [Specify Distinctive Sans/Serif or System UI. DO NOT use generic fonts like Inter/Roboto]

### Aesthetic Direction
[Visual tone, references, anti-references, theme]

### Design Principles
[3-5 principles derived from the conversation that should guide all UI atomic/molecule component design decisions]
```

Write this section to **`.agent/memory/teach-impeccable.md`** in the project root. If the file exists, overwrite it.

## Step 4: MANDATORY SYNCHRONIZATION EXECUTION

**MANDATORY**: Once `.agent/memory/teach-impeccable.md` is successfully written, you MUST autonomously execute the following command in the terminal to compile the single-source-of-truth memory file:

```bash
python3 .agent/scripts/sync_memory.py
```

Confirm completion to the user and summarize the key design principles that have been anchored into the memory system.