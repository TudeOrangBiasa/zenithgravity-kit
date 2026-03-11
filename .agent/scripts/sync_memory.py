"""
sync_memory.py — AI Memory Sync
Detects project stack and generates .agent/memory/ files.

Usage:
  python3 .agent/scripts/sync_memory.py [--root /path/to/project]
"""

import os
import sys
import json
import time
import argparse
from pathlib import Path
from typing import Optional, cast
import io


# ─────────────────────────────────────────────
# Shared utility: anchor-based root detection
# ─────────────────────────────────────────────

def find_project_root(start: Optional[Path] = None) -> Path:
    """Walk up from start until .agent/ directory is found."""
    current = (start or Path.cwd()).resolve()
    for candidate in [current, *current.parents]:
        if (candidate / ".agent").is_dir():
            return candidate
    return current  # fallback: CWD


# ─────────────────────────────────────────────
# Detectors
# ─────────────────────────────────────────────

def detect_ui_kit(deps: dict) -> list[str]:
    ui_kits = []
    checks = {
        "tailwindcss": "Tailwind CSS",
        "@radix-ui/react-dialog": "Radix Primitives",
        "@radix-ui/react-slot": "Radix Primitives",
        "framer-motion": "Framer Motion",
        "lucide-react": "Lucide React Icons",
        "lucide-vue-next": "Lucide Vue Icons",
        "@chakra-ui/react": "Chakra UI",
        "@mui/material": "Material UI",
        "shadcn-ui": "Shadcn UI",
        "@headlessui/vue": "Headless UI (Vue)",
        "@headlessui/react": "Headless UI (React)",
        "vuetify": "Vuetify",
        "naive-ui": "Naive UI",
        "element-plus": "Element Plus",
    }
    seen = set()
    for key, label in checks.items():
        if key in deps and label not in seen:
            ui_kits.append(label)
            seen.add(label)
    return ui_kits


def detect_backend_stack(deps: dict) -> list[str]:
    tools = []
    checks = {
        "prisma": "Prisma ORM",
        "@prisma/client": "Prisma ORM",
        "typeorm": "TypeORM",
        "mongoose": "Mongoose (MongoDB)",
        "express": "Express.js",
        "@nestjs/core": "NestJS",
        "graphql": "GraphQL",
        "@adonisjs/core": "AdonisJS",
        "lucid": "Lucid ORM",
        "@adonisjs/lucid": "Lucid ORM",
        "sequelize": "Sequelize",
        "drizzle-orm": "Drizzle ORM",
        "knex": "Knex.js",
        "hono": "Hono",
        "fastify": "Fastify",
    }
    seen = set()
    for key, label in checks.items():
        if key in deps and label not in seen:
            tools.append(label)
            seen.add(label)
    return tools


def detect_php_backend(composer_data: dict) -> list[str]:
    reqs = {**composer_data.get("require", {}), **composer_data.get("require-dev", {})}
    tools = []
    if "laravel/framework" in reqs: tools.append("Laravel")
    if "symfony/symfony" in reqs: tools.append("Symfony")
    if "doctrine/orm" in reqs: tools.append("Doctrine ORM")
    if "slim/slim" in reqs: tools.append("Slim Framework")
    return tools


def detect_python_backend(content: str) -> list[str]:
    tools = []
    checks = {
        "django": "Django",
        "fastapi": "FastAPI",
        "flask": "Flask",
        "sqlalchemy": "SQLAlchemy",
        "tortoise-orm": "Tortoise ORM",
        "starlette": "Starlette",
    }
    lower = content.lower()
    for key, label in checks.items():
        if key in lower:
            tools.append(label)
    return tools


def detect_qa_tools(pkg_data: dict, composer_data: dict, req_content: str) -> list[str]:
    qa_tools = []
    deps = {**pkg_data.get("dependencies", {}), **pkg_data.get("devDependencies", {})}

    node_qa = {"jest": "Jest", "vitest": "Vitest", "cypress": "Cypress (E2E)",
                "@playwright/test": "Playwright (E2E)", "mocha": "Mocha", "@testing-library/vue": "Testing Library"}
    for key, label in node_qa.items():
        if key in deps: qa_tools.append(label)

    reqs = {**composer_data.get("require", {}), **composer_data.get("require-dev", {})}
    if "phpunit/phpunit" in reqs: qa_tools.append("PHPUnit")
    if "pestphp/pest" in reqs: qa_tools.append("Pest")

    if "pytest" in req_content: qa_tools.append("PyTest")
    if "unittest" in req_content: qa_tools.append("Unittest")

    return qa_tools


def detect_cicd_pipelines(base_path: Path) -> list[str]:
    pipelines = []
    if (base_path / ".github" / "workflows").is_dir(): pipelines.append("GitHub Actions")
    if (base_path / ".gitlab-ci.yml").exists(): pipelines.append("GitLab CI")
    if (base_path / "Dockerfile").exists(): pipelines.append("Docker")
    if (base_path / "docker-compose.yml").exists() or (base_path / "docker-compose.yaml").exists():
        pipelines.append("Docker Compose")
    if (base_path / "Jenkinsfile").exists(): pipelines.append("Jenkins")
    if (base_path / ".circleci" / "config.yml").exists(): pipelines.append("CircleCI")
    return pipelines


def detect_architecture_patterns(base_path: Path) -> list[str]:
    patterns = []
    has_apps = (base_path / "apps").is_dir()
    has_packages = (base_path / "packages").is_dir()
    if has_apps and has_packages:
        patterns.append("Monorepo Structure (apps/ + packages/)")

    src_path = base_path / "src"
    search_base = src_path if src_path.exists() else base_path

    directories: set[str] = set()
    for root, dirs, _ in os.walk(search_base):
        depth = Path(root).relative_to(search_base).parts
        if len(depth) > 2:
            dirs.clear()
            continue
        directories.update(dirs)

    if {"domain", "infrastructure", "application"}.issubset(directories):
        patterns.append("Clean Architecture / DDD")
    if {"features", "shared"} & directories or {"modules"} & directories:
        patterns.append("Feature-Sliced / Modular Monolith")
    if {"atoms", "molecules", "organisms"}.issubset(directories):
        patterns.append("Atomic Design (Frontend)")
    if {"controllers", "models", "views"}.issubset(directories):
        patterns.append("MVC")
    if {"composables", "stores", "pages"}.issubset(directories):
        patterns.append("Vue Composition Pattern (Composables/Stores/Pages)")

    return patterns


def scan_components(base_path: Path) -> list[str]:
    """Scan for locally defined UI components across multiple extensions."""
    candidates = [
        base_path / "components" / "ui",
        base_path / "src" / "components" / "ui",
        base_path / "src" / "components",
        base_path / "components",
    ]
    target_dir = next((d for d in candidates if d.exists()), None)
    if not target_dir:
        return []

    extensions = ["*.tsx", "*.jsx", "*.vue", "*.svelte", "*.js"]
    components = []
    for ext in extensions:
        components += [f"`<{f.stem}>`" for f in target_dir.glob(ext)]
    return sorted(set(components))


# ─────────────────────────────────────────────
# Main generator
# ─────────────────────────────────────────────

def generate_memory_files(base_path: Path):
    t_start = time.monotonic()
    print(f"📂 Project root: {base_path}")

    pkg_data: dict = {}
    comp_data: dict = {}
    req_content: str = ""

    pkg_path = base_path / "package.json"
    if pkg_path.exists():
        try:
            with open(pkg_path, "r") as f:
                pkg_data = json.load(f)
        except json.JSONDecodeError as e:
            print(f"  ⚠️  package.json parse error: {e}")

    composer_path = base_path / "composer.json"
    if composer_path.exists():
        try:
            with open(composer_path, "r") as f:
                comp_data = json.load(f)
        except json.JSONDecodeError as e:
            print(f"  ⚠️  composer.json parse error: {e}")

    _req_buf: io.StringIO = io.StringIO()
    for req_file in ["requirements.txt", "Pipfile"]:
        req_path = base_path / req_file
        if req_path.exists():
            try:
                _req_buf.write(req_path.read_text())
            except Exception:
                pass
    req_content: str = _req_buf.getvalue()

    all_deps = {**pkg_data.get("dependencies", {}), **pkg_data.get("devDependencies", {})}
    ui_kits = detect_ui_kit(all_deps)
    be_tools = detect_backend_stack(all_deps)
    be_tools.extend(detect_php_backend(comp_data))
    be_tools.extend(detect_python_backend(req_content))

    local_components = scan_components(base_path)
    arch_patterns = detect_architecture_patterns(base_path)
    qa_tools = detect_qa_tools(pkg_data, comp_data, req_content)
    cicd_pipelines = detect_cicd_pipelines(base_path)

    memory_dir = base_path / ".agent" / "memory"
    memory_dir.mkdir(parents=True, exist_ok=True)

    # ── 1. DESIGN SYSTEM MEMORY ──────────────────────
    ui_content = [
        "# Design System Memory (State Anchor)\n",
        "> **Purpose:** Single source of truth for UI generation. AI agents MUST read this file before designing components.\n",
        "## Framework Context & Literacy",
        f"- **Detected UI Stack**: {', '.join(ui_kits) if ui_kits else 'Vanilla / Undetermined'}",
    ]

    if local_components:
        ui_content.append("- **Detected Local Components** (use before building from scratch):")
        for i in range(0, len(local_components), 5):
            chunk_str: str = ", ".join(cast(list[str], local_components[i:i+5]))
            ui_content.append("  " + chunk_str)
        ui_content.append("> **Constraint**: Prefer these locally available components.")
    else:
        ui_content.append("> **Constraint**: No local UI components detected in `components/ui/`.")

    ui_content += [
        "\n## Design & Aesthetic Constraints (frontend-design / impeccable)",
        "- **Bold Intent**: Choose a clear aesthetic direction (minimalist, luxury, brutalist, etc.) and stick to it.",
        "- **Anti-Slop Ban**: NEVER use generic purple/indigo gradients, lazy Inter/Arial fonts, or meaningless shadow.",
        "- **Typography**: Use modular scales, fluid sizing, and distinctive font pairings.",
        "- **Color**: Modern OKLCH palettes, tint neutrals to brand hue, avoid pure black/white.",
        "- **Space & Layout**: Visual rhythm through varied padding/gap. Break out of generic identical card grids.",
        "- **Reference Data**: UI elements must align with `@teach-impeccable` context if exists.",
    ]

    (memory_dir / "design-system.md").write_text("\n".join(ui_content))

    # ── 2. SYSTEM ARCHITECTURE MEMORY ────────────────
    sys_content = [
        "# System Architecture Memory (State Anchor)\n",
        "> **Purpose:** Defines structural boundaries. AI MUST respect these when generating logic or files.\n",
        "## Topological Context",
    ]

    if arch_patterns:
        sys_content.append("- **Detected Architecture Patterns**:")
        for p in arch_patterns:
            sys_content.append(f"  - {p}")
    else:
        sys_content.append("- **Detected Architecture Patterns**: Standard/Flat (No explicit macro-architecture found).")

    if be_tools:
        sys_content.append(f"- **Detected Core Tools & ORMs**: {', '.join(be_tools)}")
    if qa_tools:
        sys_content.append(f"- **Testing & QA Stack**: {', '.join(qa_tools)}")
    if cicd_pipelines:
        sys_content.append(f"- **CI/CD & DevOps**: {', '.join(cicd_pipelines)}")

    sys_content += [
        "\n## Architectural Constraints (system-architect)",
        "- **Modularity Over Monoliths**: Keep code cohesive to its domain.",
        "- **Separation of Concerns**: Controllers MUST NOT have business logic. Extract to Use Cases / Services.",
        "- **Atomic Strictness**: Atoms cannot import Molecules/Organisms.",
        "\n## Signature Paths",
        "*(Update with critical system paths, e.g., 'API Routes → apps/api/src/routes')*",
        "- TBD\n",
    ]

    (memory_dir / "system-architecture.md").write_text("\n".join(sys_content))

    elapsed = time.monotonic() - t_start
    print(f"✅ Memory sync complete ({elapsed:.2f}s)")
    print(f"   design-system.md    → UI: {', '.join(ui_kits) or 'Vanilla'} | Components: {len(local_components)}")
    print(f"   system-architecture.md → Patterns: {', '.join(arch_patterns) or 'None'}")
    if be_tools:
        print(f"   Backend tools: {', '.join(be_tools)}")
    if qa_tools:
        print(f"   QA tools: {', '.join(qa_tools)}")


def main():
    parser = argparse.ArgumentParser(
        description="Sync AI memory files from project stack detection."
    )
    parser.add_argument(
        "--root", type=str, default=None,
        help="Project root path. Defaults to nearest ancestor containing .agent/"
    )
    args = parser.parse_args()

    if args.root:
        base_path = Path(args.root).resolve()
        if not base_path.exists():
            print(f"❌ Provided root does not exist: {base_path}")
            sys.exit(1)
    else:
        base_path = find_project_root()

    generate_memory_files(base_path)


if __name__ == "__main__":
    main()
