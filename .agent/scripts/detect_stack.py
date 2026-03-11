"""
detect_stack.py — Project Stack Detector
Detects language(s), frameworks, environment, and recommends active agent skills.
Supports multi-stack (e.g., monorepo with Node + Python).

Usage:
  python3 .agent/scripts/detect_stack.py [--root /path/to/project] [--json]
"""

import sys
import io
import json
import argparse
from enum import Enum
from pathlib import Path
from typing import Optional, cast


# ─────────────────────────────────────────────
# Shared utility
# ─────────────────────────────────────────────

def find_project_root(start: Optional[Path] = None) -> Path:
    current = (start or Path.cwd()).resolve()
    for candidate in [current, *current.parents]:
        if (candidate / ".agent").is_dir():
            return candidate
    return current


# ─────────────────────────────────────────────
# Enums
# ─────────────────────────────────────────────

class StackType(Enum):
    NODE = "Node.js"
    PHP = "PHP"
    PYTHON = "Python"
    GO = "Go"
    RUST = "Rust"
    JAVA = "Java"
    RUBY = "Ruby"
    ELIXIR = "Elixir"
    UNKNOWN = "Unknown"


class EnvType(Enum):
    DDEV = "DDEV"
    DOCKER_COMPOSE = "Docker Compose"
    DOCKER = "Docker"
    NATIVE = "Native"


# ─────────────────────────────────────────────
# Detection — multi-pass (not elif chain)
# ─────────────────────────────────────────────

def detect_stacks(root: Path) -> list[tuple[StackType, list[str]]]:
    """Returns list of (StackType, frameworks) for ALL detected stacks."""
    results = []

    # ── Python ────────────────────────────────
    if any((root / f).exists() for f in ["requirements.txt", "Pipfile", "pyproject.toml"]):
        frameworks = []
        if (root / "manage.py").exists(): frameworks.append("Django")
        try:
            _buf: io.StringIO = io.StringIO()
            for fname in ["requirements.txt", "Pipfile"]:
                p = root / fname
                if p.exists():
                    _buf.write(p.read_text().lower())
            req: str = _buf.getvalue()
            if "fastapi" in req:
                frameworks.append("FastAPI")
            if "flask" in req:
                frameworks.append("Flask")
        except Exception:
            pass
        results.append((StackType.PYTHON, frameworks))

    # ── Node.js ───────────────────────────────
    pkg_path = root / "package.json"
    if pkg_path.exists():
        frameworks = []
        try:
            pkg = json.loads(pkg_path.read_text())
            deps = {**pkg.get("dependencies", {}), **pkg.get("devDependencies", {})}
            fw_map = {
                "next": "Next.js", "react": "React", "vue": "Vue.js",
                "svelte": "Svelte", "express": "Express.js", "@nestjs/core": "NestJS",
                "@adonisjs/core": "AdonisJS", "nuxt": "Nuxt", "astro": "Astro",
                "hono": "Hono", "fastify": "Fastify", "vite": "Vite",
            }
            for key, label in fw_map.items():
                if key in deps: frameworks.append(label)
        except Exception:
            pass
        results.append((StackType.NODE, frameworks))

    # ── PHP ───────────────────────────────────
    composer_path = root / "composer.json"
    if composer_path.exists():
        frameworks = []
        try:
            comp = json.loads(composer_path.read_text())
            reqs = {**comp.get("require", {}), **comp.get("require-dev", {})}
            if "laravel/framework" in reqs: frameworks.append("Laravel")
            if "symfony/symfony" in reqs: frameworks.append("Symfony")
            if "slim/slim" in reqs: frameworks.append("Slim")
            if "cakephp/cakephp" in reqs: frameworks.append("CakePHP")
        except Exception:
            pass
        results.append((StackType.PHP, frameworks))

    # ── Go ────────────────────────────────────
    if (root / "go.mod").exists():
        results.append((StackType.GO, []))

    # ── Rust ──────────────────────────────────
    if (root / "Cargo.toml").exists():
        results.append((StackType.RUST, []))

    # ── Java ──────────────────────────────────
    if (root / "pom.xml").exists() or (root / "build.gradle").exists():
        frameworks = []
        try:
            pom = root / "pom.xml"
            if pom.exists() and "spring-boot" in pom.read_text():
                frameworks.append("Spring Boot")
        except Exception:
            pass
        results.append((StackType.JAVA, frameworks))

    # ── Ruby ──────────────────────────────────
    if (root / "Gemfile").exists():
        frameworks = []
        try:
            gemfile = (root / "Gemfile").read_text()
            if "rails" in gemfile.lower(): frameworks.append("Ruby on Rails")
            if "sinatra" in gemfile.lower(): frameworks.append("Sinatra")
        except Exception:
            pass
        results.append((StackType.RUBY, frameworks))

    # ── Elixir ────────────────────────────────
    if (root / "mix.exs").exists():
        frameworks = []
        try:
            mix = (root / "mix.exs").read_text()
            if "phoenix" in mix.lower(): frameworks.append("Phoenix")
        except Exception:
            pass
        results.append((StackType.ELIXIR, frameworks))

    if not results:
        results.append((StackType.UNKNOWN, []))

    return results


def detect_environment(root: Path) -> EnvType:
    if (root / ".ddev").exists(): return EnvType.DDEV
    if (root / "docker-compose.yml").exists() or (root / "docker-compose.yaml").exists():
        return EnvType.DOCKER_COMPOSE
    if (root / "Dockerfile").exists(): return EnvType.DOCKER
    return EnvType.NATIVE


def get_command_prefix(env: EnvType) -> str:
    if env == EnvType.DDEV: return "ddev "
    return ""


# ─────────────────────────────────────────────
# Report generation
# ─────────────────────────────────────────────

FRONTEND_FRAMEWORKS = {"Next.js", "React", "Vue.js", "Svelte", "Nuxt", "Astro", "Vite"}
BACKEND_FRAMEWORKS = {"Django", "FastAPI", "Flask", "Express.js", "NestJS", "Laravel",
                      "Symfony", "Spring Boot", "AdonisJS", "Hono", "Fastify", "Phoenix"}


def generate_report(root: Path) -> str:
    stacks = detect_stacks(root)
    env = detect_environment(root)

    all_frameworks = [fw for _, fws in stacks for fw in fws]
    all_stack_names: list[str] = [str(s.value) for s, _ in stacks if s != StackType.UNKNOWN]

    lines = [
        "STACK REPORT",
        f"Language/Platform : {', '.join(all_stack_names) if all_stack_names else 'Unknown'}",
    ]

    for stack, frameworks in stacks:
        if stack != StackType.UNKNOWN:
            fw_str = ', '.join(frameworks) if frameworks else 'None detected'
            lines.append(f"  └─ {stack.value} Frameworks: {fw_str}")

    lines.append(f"Environment       : {env.value}")

    has_frontend = bool(set(all_frameworks) & FRONTEND_FRAMEWORKS)
    has_backend = bool(set(all_frameworks) & BACKEND_FRAMEWORKS) or any(
        s in [StackType.GO, StackType.RUST, StackType.JAVA, StackType.PHP, StackType.RUBY, StackType.ELIXIR]
        for s, _ in stacks
    )

    if has_frontend:
        lines.append("UI Guidelines     : Active → `frontend-design` (Impeccable aesthetics & rigorous UX without AI slop).")
    if has_backend:
        lines.append("Architecture Guide: Active → `system-architect` (Clean Architecture, DDD, Modular boundaries).")
        lines.append("API & Integration : Active → `api-architect` (REST/GraphQL standards & Payload structure).")
        lines.append("Database & Schema : Active → `database-architect` (Indexing, Normalization, N+1 prevention).")

    lines.append("Security & Review : Active → `sec-ops` (OWASP principles & severity-rated code review).")
    lines.append("DevOps & CI/CD    : Active → `devops-architect` (Container immutability & deployment pipelines).")

    files = [f.name for f in root.iterdir() if f.is_file()]
    if any(f.endswith(".sh") for f in files) or "Makefile" in files:
        lines.append("Automation Scripts: Active → `automation-engineer` (Bash standards & Bats testing).")

    lines.append("Error Resolution  : Active → `systematic-debugging` (Root-cause 5-Whys — global trigger).")

    prefix = get_command_prefix(env)
    if prefix:
        lines.append(f"Command Prefix    : MUST prepend all commands with `{prefix}`")
    elif env == EnvType.DOCKER_COMPOSE:
        lines.append("Command Guideline : Docker Compose detected — use `docker-compose exec <service> <cmd>`.")
    else:
        lines.append("Command Guideline : Run commands natively.")

    return "\n".join(lines)


def generate_json_report(root: Path) -> str:
    stacks = detect_stacks(root)
    env = detect_environment(root)
    return json.dumps({
        "root": str(root),
        "stacks": [{"language": s.value, "frameworks": fws} for s, fws in stacks],
        "environment": env.value,
    }, indent=2)


# ─────────────────────────────────────────────
# CLI
# ─────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Detect project stack and output agent routing recommendations."
    )
    parser.add_argument(
        "--root", type=str, default=None,
        help="Project root path. Defaults to nearest ancestor containing .agent/"
    )
    parser.add_argument(
        "--json", action="store_true",
        help="Output raw JSON instead of human-readable report"
    )
    args = parser.parse_args()

    root = Path(args.root).resolve() if args.root else find_project_root()

    if not root.exists():
        print(f"❌ Root path does not exist: {root}")
        sys.exit(1)

    if args.json:
        print(generate_json_report(root))
    else:
        print(generate_report(root))


if __name__ == "__main__":
    main()
