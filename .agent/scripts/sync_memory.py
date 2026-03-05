import os
import json
from pathlib import Path

def detect_ui_kit(package_json):
    """Detects UI kit definitions from package.json dependencies."""
    deps = {**package_json.get("dependencies", {}), **package_json.get("devDependencies", {})}
    
    ui_kits = []
    if "tailwindcss" in deps:
        ui_kits.append("Tailwind CSS")
    if "@radix-ui/react-dialog" in deps or "@radix-ui/react-slot" in deps:
        ui_kits.append("Radix Primitives")
    if "framer-motion" in deps:
        ui_kits.append("Framer Motion")
    if "lucide-react" in deps:
        ui_kits.append("Lucide React Icons")
    if "@chakra-ui/react" in deps:
        ui_kits.append("Chakra UI")
    if "@mui/material" in deps:
        ui_kits.append("Material UI")
        
    return ui_kits

def scan_components(base_path):
    """Scans for locally defined UI components (like shadcn components)."""
    components_dir = base_path / "components" / "ui"
    src_components_dir = base_path / "src" / "components" / "ui"
    
    target_dir = None
    if components_dir.exists():
        target_dir = components_dir
    elif src_components_dir.exists():
        target_dir = src_components_dir
        
    if not target_dir:
        return []
        
    components = []
    for file in target_dir.glob("*.tsx"):
        components.append(f"`<{file.stem}>`")
    for file in target_dir.glob("*.js"):
        components.append(f"`<{file.stem}>`")
        
    return sorted(components)

def generate_memory_file(base_path):
    pkg_path = base_path / "package.json"
    ui_kits = []
    
    if pkg_path.exists():
        with open(pkg_path, "r") as f:
            try:
                pkg_data = json.load(f)
                ui_kits = detect_ui_kit(pkg_data)
            except json.JSONDecodeError:
                pass

    local_components = scan_components(base_path)
    
    # Format the Memory State
    content = [
        "# Design System Memory (State Anchor)\n",
        "> **Purpose:** This file acts as the single source of truth for UI generation. AI agents MUST read this file before designing components to ensure visual consistency across sessions and prevent hallucinating generic styles.\n",
        "## Framework Context & Literacy",
    ]
    
    if ui_kits:
        content.append(f"- **Detected UI Stack**: {', '.join(ui_kits)}")
    else:
        content.append("- **Detected UI Stack**: Vanilla / Undetermined")
        
    if local_components:
        content.append("- **Detected Local Kits (e.g., Shadcn/Radix)**: The following components are available natively in your repo:")
        # Group into lines of 5 for readability
        for i in range(0, len(local_components), 5):
            content.append("  " + ", ".join(local_components[i:i+5]))
        content.append("> **Constraint**: You MUST use these locally available components before attempting to build custom complex elements from scratch.")
    else:
        content.append("> **Constraint**: No local UI components (`@/components/ui/`) detected. Be cautious and design clean semantic HTML or generate the components if explicitly asked.")

    # Static Generic Baselines
    content.append("\n## External Constraints & Tokens")
    content.append("- **Base Spacing Unit**: `8px` (`p-2`, `m-4`, etc.)")
    content.append("- **Base Border Radius**: `md` (approx `6px`) for cards and buttons.")
    content.append("- **Elevation Strategy**: Subtle Layering (Borders + Background shifts). **NO HEAVY DROP SHADOWS**.")
    content.append("\n## Signature Patterns")
    content.append("*(Add specific component variations here once established with the user, e.g., \"All primary CTA buttons must have a subtle gradient border\")*")
    content.append("- TBD\n")

    # Write to memory file
    memory_dir = base_path / ".agent" / "memory"
    memory_dir.mkdir(parents=True, exist_ok=True)
    memory_file = memory_dir / "design-system.md"
    
    with open(memory_file, "w") as f:
        f.write("\n".join(content))
        
    print(f"Successfully synced UI dependency state to {memory_file}")
    if ui_kits:
        print(f"Detected stack: {', '.join(ui_kits)}")
    if local_components:
        print(f"Detected {len(local_components)} local UI components.")

if __name__ == "__main__":
    pwd = Path.cwd()
    generate_memory_file(pwd)
