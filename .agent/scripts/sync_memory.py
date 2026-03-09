import os
import json
from pathlib import Path

def detect_ui_kit(package_json):
    """Detects UI kit definitions from package.json dependencies."""
    deps = {**package_json.get("dependencies", {}), **package_json.get("devDependencies", {})}
    
    ui_kits = []
    if "tailwindcss" in deps: ui_kits.append("Tailwind CSS")
    if "@radix-ui/react-dialog" in deps or "@radix-ui/react-slot" in deps: ui_kits.append("Radix Primitives")
    if "framer-motion" in deps: ui_kits.append("Framer Motion")
    if "lucide-react" in deps: ui_kits.append("Lucide React Icons")
    if "@chakra-ui/react" in deps: ui_kits.append("Chakra UI")
    if "@mui/material" in deps: ui_kits.append("Material UI")
    return ui_kits

def detect_backend_stack(pkg_data, is_node=True):
    """Detects backend/fullstack tools and ORMs."""
    if not is_node: return []
    deps = {**pkg_data.get("dependencies", {}), **pkg_data.get("devDependencies", {})}
    tools = []
    if "prisma" in deps or "@prisma/client" in deps: tools.append("Prisma ORM")
    if "typeorm" in deps: tools.append("TypeORM")
    if "mongoose" in deps: tools.append("Mongoose (MongoDB)")
    if "express" in deps: tools.append("Express.js")
    if "@nestjs/core" in deps: tools.append("NestJS")
    if "graphql" in deps: tools.append("GraphQL")
    if "@adonisjs/core" in deps: tools.append("AdonisJS")
    if "lucid" in deps or "@adonisjs/lucid" in deps: tools.append("Lucid ORM")
    if "sequelize" in deps: tools.append("Sequelize")
    return tools

def detect_php_backend(composer_data):
    reqs = {**composer_data.get("require", {}), **composer_data.get("require-dev", {})}
    tools = []
    if "laravel/framework" in reqs: tools.append("Laravel")
    if "symfony/symfony" in reqs: tools.append("Symfony")
    if "doctrine/orm" in reqs: tools.append("Doctrine ORM")
    return tools

def detect_python_backend(req_content):
    tools = []
    if "Django" in req_content or "django" in req_content: tools.append("Django")
    if "FastAPI" in req_content or "fastapi" in req_content: tools.append("FastAPI")
    if "Flask" in req_content or "flask" in req_content: tools.append("Flask")
    if "SQLAlchemy" in req_content or "sqlalchemy" in req_content: tools.append("SQLAlchemy")
    return tools

def detect_architecture_patterns(base_path):
    """
    Recursively scans up to depth 3 to detect overarching structural patterns.
    """
    patterns = []
    has_apps = (base_path / "apps").is_dir()
    has_packages = (base_path / "packages").is_dir()
    
    if has_apps and has_packages:
        patterns.append("Monorepo Structure (apps/ and packages/)")
    
    # Check for DDD / Clean Architecture layers
    src_path = base_path / "src"
    search_base = src_path if src_path.exists() else base_path
    
    # Collect all directory names down 2 levels
    directories = set()
    for root, dirs, files in os.walk(search_base):
        depth = Path(root).relative_to(search_base).parts
        if len(depth) > 2:
            dirs[:] = []  # Don't go deeper
            continue
        directories.update(dirs)
        
    # Pattern Logic
    if {"domain", "infrastructure", "application"}.issubset(directories):
        patterns.append("Clean Architecture / Domain-Driven Design (DDD)")
        
    if {"features", "shared"} & directories or {"modules"} & directories:
        patterns.append("Feature-Sliced Design / Modular Monolith")
        
    if {"atoms", "molecules", "organisms"}.issubset(directories):
        patterns.append("Atomic Design (Frontend component hierarchy detected)")
        
    if {"controllers", "models", "views"}.issubset(directories):
        patterns.append("MVC (Model-View-Controller)")
        
    return patterns

def detect_qa_tools(pkg_data, composer_data, req_content):
    """Detects testing frameworks across ecosystems."""
    qa_tools = []
    
    # Node QA
    deps = {**pkg_data.get("dependencies", {}), **pkg_data.get("devDependencies", {})}
    if "jest" in deps: qa_tools.append("Jest")
    if "vitest" in deps: qa_tools.append("Vitest")
    if "cypress" in deps: qa_tools.append("Cypress (E2E)")
    if "@playwright/test" in deps: qa_tools.append("Playwright (E2E)")
    
    # PHP QA
    reqs = {**composer_data.get("require", {}), **composer_data.get("require-dev", {})}
    if "phpunit/phpunit" in reqs: qa_tools.append("PHPUnit")
    if "pestphp/pest" in reqs: qa_tools.append("Pest")
    
    # Python QA
    if "pytest" in req_content: qa_tools.append("PyTest")
    if "unittest" in req_content: qa_tools.append("Unittest")
    
    return qa_tools

def detect_cicd_pipelines(base_path):
    """Detects CI/CD footprints and Container configs."""
    pipelines = []
    if (base_path / ".github" / "workflows").is_dir(): pipelines.append("GitHub Actions")
    if (base_path / ".gitlab-ci.yml").exists(): pipelines.append("GitLab CI")
    if (base_path / "Dockerfile").exists(): pipelines.append("Docker Containerized")
    if (base_path / "docker-compose.yml").exists(): pipelines.append("Docker Compose")
    if (base_path / "Jenkinsfile").exists(): pipelines.append("Jenkins")
    
    return pipelines

def scan_components(base_path):
    """Scans for locally defined UI components."""
    components_dir = base_path / "components" / "ui"
    src_components_dir = base_path / "src" / "components" / "ui"
    
    target_dir = components_dir if components_dir.exists() else (src_components_dir if src_components_dir.exists() else None)
    if not target_dir: return []
        
    components = [f"`<{file.stem}>`" for file in target_dir.glob("*.tsx")]
    components += [f"`<{file.stem}>`" for file in target_dir.glob("*.js")]
    return sorted(components)

def generate_memory_files(base_path):
    pkg_path = base_path / "package.json"
    composer_path = base_path / "composer.json"
    req_path = base_path / "requirements.txt"
    ui_kits = []
    be_tools = []
    
    if pkg_path.exists():
        with open(pkg_path, "r") as f:
            try:
                pkg_data = json.load(f)
                ui_kits = detect_ui_kit(pkg_data)
                be_tools.extend(detect_backend_stack(pkg_data))
            except json.JSONDecodeError:
                pass
                
    if composer_path.exists():
        with open(composer_path, "r") as f:
            try:
                comp_data = json.load(f)
                be_tools.extend(detect_php_backend(comp_data))
            except json.JSONDecodeError:
                pass
                
    if req_path.exists():
        try:
            with open(req_path, "r") as f:
                content = f.read()
                be_tools.extend(detect_python_backend(content))
        except Exception:
            pass

    local_components = scan_components(base_path)
    arch_patterns = detect_architecture_patterns(base_path)
    
    # Ensure variables exist even if files were missing
    try: pkg_data
    except NameError: pkg_data = {}
    try: comp_data
    except NameError: comp_data = {}
    try: content
    except NameError: content = ""

    qa_tools = detect_qa_tools(pkg_data, comp_data, content)
    cicd_pipelines = detect_cicd_pipelines(base_path)
    
    memory_dir = base_path / ".agent" / "memory"
    memory_dir.mkdir(parents=True, exist_ok=True)
    
    # 1. UI DESIGN SYSTEM MEMORY
    ui_content = [
        "# Design System Memory (State Anchor)\n",
        "> **Purpose:** Single source of truth for UI generation. AI agents MUST read this file before designing components.\n",
        "## Framework Context & Literacy",
        f"- **Detected UI Stack**: {', '.join(ui_kits) if ui_kits else 'Vanilla / Undetermined'}"
    ]
    
    if local_components:
        ui_content.append("- **Detected Local Kits (e.g., Shadcn/Radix)**: Natively available components:")
        for i in range(0, len(local_components), 5):
            ui_content.append("  " + ", ".join(local_components[i:i+5]))
        ui_content.append("> **Constraint**: Use these locally available components before building from scratch.")
    else:
        ui_content.append("> **Constraint**: No local UI components detected (`@/components/ui/`).")

    ui_content.append("\n## Design & Aesthetic Constraints (ux-humanist-designer)")
    ui_content.append("- **Base Spacing Unit**: `8px` grid (`p-2`, `m-4`, etc.). All padding/margins must be multiples of 8.")
    ui_content.append("- **Base Border Radius**: `md` (approx `6px`) for cards and buttons.")
    ui_content.append("- **Elevation Strategy**: Subtle Layering (Borders + Background shifts). **NO HEAVY DROP SHADOWS**.")
    ui_content.append("- **Mathematical Patterns**: Enforce Golden Ratio proportions and Modular Typographic Scales.")
    ui_content.append("- **Anti-Slop Ban**: NEVER use generic purple/indigo gradients or Inter/Arial fonts.")
    
    with open(memory_dir / "design-system.md", "w") as f:
        f.write("\n".join(ui_content))
        
    # 2. SYSTEM ARCHITECTURE MEMORY
    sys_content = [
        "# System Architecture Memory (State Anchor)\n",
        "> **Purpose:** Defines the structural boundaries of the repository. AI MUST strictly respect these boundaries when generating logic or files.\n",
        "## Topological Context"
    ]
    
    if arch_patterns:
        sys_content.append("- **Detected Architecture Patterns**: ")
        for p in arch_patterns:
            sys_content.append(f"  - {p}")
    else:
        sys_content.append("- **Detected Architecture Patterns**: Standard/Flat (No explicit macro-architecture found).")
        
    if be_tools:
        sys_content.append(f"- **Detected Core Tools & ORMs**: {', '.join(be_tools)}")
        
    if qa_tools:
        sys_content.append(f"- **Testing & QA Stack (`quality-assurance`)**: {', '.join(qa_tools)}")
    
    if cicd_pipelines:
        sys_content.append(f"- **CI/CD & DevOps (`devops-architect`)**: {', '.join(cicd_pipelines)}")
        
    sys_content.append("\n## Architectural Constraints (`system-architect`)")
    sys_content.append("- **Modularity Over Monoliths**: If Feature-Sliced or Modular patterns are detected, keep code cohesive to its domain.")
    sys_content.append("- **Separation of Concerns**: Controllers MUST NOT have business logic. Extract to Use Cases / Services.")
    sys_content.append("- **Atomic Strictness**: If Atomic Design is detected on UI, Atoms cannot contain or import Molecules/Organisms.")
    
    sys_content.append("\n## Signature Paths")
    sys_content.append("*(Add critical system paths here, e.g., 'API Routes are in apps/api/src/routes')*")
    sys_content.append("- TBD\n")

    with open(memory_dir / "system-architecture.md", "w") as f:
        f.write("\n".join(sys_content))
        
    print(f"✅ Successfully synced Design System Memory to {memory_dir / 'design-system.md'}")
    print(f"✅ Successfully synced System Architecture Memory to {memory_dir / 'system-architecture.md'}")
    print(f"Architecture Patterns detected: {', '.join(arch_patterns) if arch_patterns else 'None'}")

if __name__ == "__main__":
    pwd = Path.cwd()
    generate_memory_files(pwd)
