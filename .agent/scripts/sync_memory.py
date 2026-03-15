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

def get_raw_dependencies(pkg_data: dict, composer_data: dict, req_content: str) -> list[str]:
    raw_deps = set()
    
    deps = {**pkg_data.get("dependencies", {}), **pkg_data.get("devDependencies", {})}
    for dep in deps.keys():
        raw_deps.add(dep)
        
    reqs = {**composer_data.get("require", {}), **composer_data.get("require-dev", {})}
    for req in reqs.keys():
        raw_deps.add(req)
        
    for line in req_content.splitlines():
        line = line.strip()
        if line and not line.startswith('#'):
            pkg_name = line.split('==')[0].split('>')[0].split('<')[0]
            raw_deps.add(pkg_name)
            
    return sorted(list(raw_deps))


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
    """
    Dynamically discover UI components by traversing the project tree.
    This approach is framework-agnostic and eliminates false-negatives from static path whitelists.
    
    Strategy:
    - Walk the entire project (up to reasonable depth)
    - Skip known noise directories (node_modules, vendor, dist, .git, cache, etc.)
    - Detect component files by extension AND PascalCase naming convention
    - Deduplicate by stem name (same component name from multiple dirs = 1 entry)
    """
    # Directories to fully prune/skip — no components will ever live here
    SKIP_DIRS: set[str] = {
        "node_modules", "vendor", ".git", ".svn", ".hg",
        "dist", "build", "out", ".next", ".nuxt", ".svelte-kit",
        "__pycache__", ".cache", ".temp", ".tmp",
        "coverage", ".nyc_output", "storybook-static",
        "public", "storage", "bootstrap", "bin",
        ".agent", ".idea", ".vscode",
    }

    # File extensions that indicate a UI component file
    COMPONENT_EXTENSIONS: set[str] = {
        ".tsx", ".jsx", ".vue", ".svelte", ".astro", ".blade.php",
    }

    # Max depth to recurse (prevents traversing entire filesystem for edge-case paths)
    MAX_DEPTH = 8

    components: set[str] = set()

    def _walk(current: Path, depth: int) -> None:
        if depth > MAX_DEPTH:
            return
        try:
            for entry in current.iterdir():
                if not entry.exists():
                    continue
                if entry.is_dir():
                    if entry.name in SKIP_DIRS or entry.name.startswith("."):
                        continue
                    _walk(entry, depth + 1)
                elif entry.is_file():
                    # Handle compound extensions like .blade.php
                    suffix = "".join(entry.suffixes).lower()
                    if suffix not in COMPONENT_EXTENSIONS:
                        # Fallback single suffix check
                        if entry.suffix.lower() not in {s for s in COMPONENT_EXTENSIONS if "." in s}:
                            continue

                    # PascalCase heuristic: component names start with uppercase
                    stem = entry.name
                    for ext in [".blade.php", ".stories.tsx", ".stories.jsx", ".stories.vue", ".test.tsx", ".spec.tsx"]:
                        stem = stem.replace(ext, "")
                    stem = stem.replace(entry.suffix, "")

                    if stem and stem[0].isupper() and not stem.startswith("_"):
                        components.add(f"`<{stem}>`")
        except PermissionError:
            pass

    _walk(base_path, depth=0)
    return sorted(list(components))


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

    raw_deps = get_raw_dependencies(pkg_data, comp_data, req_content)
    local_components = scan_components(base_path)
    arch_patterns = detect_architecture_patterns(base_path)
    cicd_pipelines = detect_cicd_pipelines(base_path)

    memory_dir = base_path / ".agent" / "memory"
    memory_dir.mkdir(parents=True, exist_ok=True)

    # ── 1. DESIGN SYSTEM MEMORY ──────────────────────
    ui_content = [
        "# Design System Memory (State Anchor)\n",
        "> **Purpose:** Single source of truth for UI generation. AI agents MUST read this file before designing components.\n",
        "## Framework Context & Literacy",
        f"- **Detected Raw Dependencies**: {', '.join(raw_deps) if raw_deps else 'None'}",
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
    ]

    impeccable_path = memory_dir / "teach-impeccable.md"
    if impeccable_path.exists():
        ui_content.append(f"\n## Visual Tokens (from @teach-impeccable)\n")
        try:
            ui_content.append(impeccable_path.read_text())
        except Exception as e:
            ui_content.append(f"> ⚠️ Failed to read teach-impeccable.md: {e}")
    else:
        ui_content.append("- **Reference Data**: Run `@teach-impeccable` to initialize brand & UI constraints.")

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

    if raw_deps:
        sys_content.append(f"- **Detected Raw Dependencies**: {', '.join(raw_deps)}")
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
    print(f"   design-system.md    → Components: {len(local_components)}")
    print(f"   system-architecture.md → Patterns: {', '.join(arch_patterns) or 'None'}")
    print(f"   Total raw dependencies synced: {len(raw_deps)}")


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
