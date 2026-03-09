# Design System Memory (State Anchor)

> **Purpose:** Single source of truth for UI generation. AI agents MUST read this file before designing components.

## Framework Context & Literacy
- **Detected UI Stack**: Vanilla / Undetermined
> **Constraint**: No local UI components detected (`@/components/ui/`).

## Design & Aesthetic Constraints (ux-humanist-designer)
- **Base Spacing Unit**: `8px` grid (`p-2`, `m-4`, etc.). All padding/margins must be multiples of 8.
- **Base Border Radius**: `md` (approx `6px`) for cards and buttons.
- **Elevation Strategy**: Subtle Layering (Borders + Background shifts). **NO HEAVY DROP SHADOWS**.
- **Mathematical Patterns**: Enforce Golden Ratio proportions and Modular Typographic Scales.
- **Anti-Slop Ban**: NEVER use generic purple/indigo gradients or Inter/Arial fonts.