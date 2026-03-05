# Design System Memory (State Anchor)

> **Purpose:** This file acts as the single source of truth for UI generation. AI agents MUST read this file before designing components to ensure visual consistency across sessions and prevent hallucinating generic styles.

## Framework Context & Literacy
- **Detected UI Stack**: Vanilla / Undetermined
> **Constraint**: No local UI components (`@/components/ui/`) detected. Be cautious and design clean semantic HTML or generate the components if explicitly asked.

## External Constraints & Tokens
- **Base Spacing Unit**: `8px` (`p-2`, `m-4`, etc.)
- **Base Border Radius**: `md` (approx `6px`) for cards and buttons.
- **Elevation Strategy**: Subtle Layering (Borders + Background shifts). **NO HEAVY DROP SHADOWS**.

## Signature Patterns
*(Add specific component variations here once established with the user, e.g., "All primary CTA buttons must have a subtle gradient border")*
- TBD
