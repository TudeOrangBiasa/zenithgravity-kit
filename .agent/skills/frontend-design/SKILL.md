---
name: frontend-design
description: Design thinking and decision-making for web UI. Use when designing components, layouts, color schemes, typography, or creating aesthetic interfaces.
metadata:
  version: 1.1.0
  priority: high
---

# Frontend Design System

> **Philosophy:** Every pixel has purpose. Restraint is luxury. User psychology drives decisions.
> **Warning**: Never default to a generic "AI Slop" style.

## 1. Intent First & Constraint Analysis

Before coding UI, you must state (in 2-3 lines) your design intent:

1. **Who is the Audience & Emotion?** (e.g., Trust = Blues, Luxury = Deep hues).
2. **Color World & Signature**: What specific colors and unique structural element define this product's domain?
3. **Typography & Feel**: What fonts and spacing fit the intent?
   _If the user didn't specify these, ask before assuming._

## 2. Design Memory & Component Literacy (MANDATORY)

- **Consult State Anchor**: You **MUST** read `.agent/memory/design-system.md` before starting any design work to ensure consistency across sessions.
- **Component Literacy**: Use the UI kit components declared in the memory file (e.g., built-in Shadcn `<Button>`, Radix `<Popover>`) before inventing raw custom components from scratch.
- **Update Memory**: If you create a new reusable pattern or establish a new variable, update the `design-system.md` file after confirming with the user.

## 3. Anti-AI Slop (MANDATORY BANS)

AI tends to default to safe, boring, or cliché designs. **AVOID THESE AT ALL COSTS:**

- **Bento Grids**: Do not use bento grids unless the content _needs_ a grid.
- **Mesh/Aurora Gradients**: Use solid, high-contrast flat colors instead.
- **Generic Drab Colors**: No standard bootstrap blue/green/red. **Purple/Violet is banned**. Use curated, harmonious palettes (DSL tailored, sleek dark modes).
- **Rounded Everything**: Stop making everything perfectly rounded. Think where sharp, brutalist edges can be used.
- **Emoji as UI**: **NEVER** use emojis for UI icons. Use SVG icons (e.g., Lucide) or real imagery.

## 4. Token Architecture & Subtle Layering

- **Primitives over Hex**: Do not hardcode hex values in UI components. Use CSS variables or framework configuration tokens (e.g., `--surface-primary`, `bg-background`).
- **Subtle Layering**: **BAN heavy drop shadows**. Create elevation using subtle background opacity shifts (e.g., one step lighter in dark mode) and extremely faint borders.
- **Whisper Borders**: If borders are the first thing you see, they are too strong. Use low opacity borders to separate surfaces.

## 5. Layout Precision & Motion

- **8-Point Grid Concept**: All spacing/sizing in multiples of 8px (4, 8, 16, 24, 32, 48, 64).
- **Hero Sections**: Must be truly centered (`height: 100svh`), not biased by asymmetric padding. Consistency in max-width containers.
- **Motion First**: Animate only `transform` and `opacity` for performance. Easing: `ease-out` for entering, `ease-in` for leaving.
