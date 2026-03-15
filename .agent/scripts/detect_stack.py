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
    DOTNET = ".NET / C#"
    DART = "Dart / Flutter"
    KOTLIN = "Kotlin"
    SWIFT = "Swift"
    UNKNOWN = "Unknown"


class EnvType(Enum):
    DDEV = "DDEV"
    DOCKER_COMPOSE = "Docker Compose"
    DOCKER = "Docker"
    PODMAN = "Podman"
    NIX = "Nix Shell"
    NATIVE = "Native"


# ─────────────────────────────────────────────
# Detection — multi-pass (not elif chain)
# ─────────────────────────────────────────────

def detect_stacks(root: Path) -> list[tuple[StackType, list[str]]]:
    """Returns list of (StackType, frameworks) for ALL detected stacks in this project."""
    results = []

    # ── Python ────────────────────────────────────────────────────────────────
    has_py = any((root / f).exists() for f in ["requirements.txt", "Pipfile", "pyproject.toml", "setup.py", "setup.cfg"])
    if has_py:
        frameworks: list[str] = []
        if (root / "manage.py").exists():
            frameworks.append("Django")
        try:
            _buf: io.StringIO = io.StringIO()
            for fname in ["requirements.txt", "Pipfile", "pyproject.toml"]:
                p = root / fname
                if p.exists():
                    _buf.write(p.read_text().lower())
            req: str = _buf.getvalue()
            fw_signals = {
                "fastapi": "FastAPI", "flask": "Flask", "litestar": "Litestar",
                "sanic": "Sanic", "tornado": "Tornado", "aiohttp": "aiohttp",
                "celery": "Celery", "dramatiq": "Dramatiq",
                "sqlalchemy": "SQLAlchemy", "alembic": "Alembic",
                "pydantic": "Pydantic", "strawberry-graphql": "Strawberry GraphQL",
            }
            for signal, label in fw_signals.items():
                if signal in req:
                    frameworks.append(label)
        except Exception:
            pass
        results.append((StackType.PYTHON, frameworks))

    # ── Node.js ───────────────────────────────────────────────────────────────
    pkg_path = root / "package.json"
    if pkg_path.exists():
        frameworks = []
        try:
            pkg = json.loads(pkg_path.read_text())
            deps = {**pkg.get("dependencies", {}), **pkg.get("devDependencies", {})}
            fw_map = {
                # Meta-frameworks
                "next": "Next.js", "nuxt": "Nuxt", "astro": "Astro",
                "@remix-run/node": "Remix", "@remix-run/react": "Remix",
                # UI frameworks
                "react": "React", "vue": "Vue.js", "svelte": "Svelte",
                "solid-js": "SolidJS", "@builder.io/qwik": "Qwik",
                "@angular/core": "Angular", "preact": "Preact",
                # Backend / API
                "express": "Express.js", "@nestjs/core": "NestJS",
                "@adonisjs/core": "AdonisJS", "fastify": "Fastify",
                "hono": "Hono", "koa": "Koa",
                "elysia": "Elysia (Bun)", "bun": "Bun",
                # Mobile / Desktop
                "react-native": "React Native", "electron": "Electron",
                "@capacitor/core": "Capacitor", "expo": "Expo",
                # Build tools as signals
                "vite": "Vite", "webpack": "Webpack", "esbuild": "ESBuild",
                # State management (important context)
                "zustand": "Zustand", "pinia": "Pinia", "@reduxjs/toolkit": "Redux Toolkit",
                # tRPC / GraphQL
                "@trpc/server": "tRPC", "graphql": "GraphQL", "@apollo/client": "Apollo",
                # ORM / DB
                "prisma": "Prisma", "drizzle-orm": "Drizzle ORM",
                "@supabase/supabase-js": "Supabase",
            }
            for key, label in fw_map.items():
                if key in deps:
                    frameworks.append(label)
        except Exception:
            pass
        results.append((StackType.NODE, frameworks))

    # ── PHP ───────────────────────────────────────────────────────────────────
    composer_path = root / "composer.json"
    if composer_path.exists():
        frameworks = []
        try:
            comp = json.loads(composer_path.read_text())
            reqs = {**comp.get("require", {}), **comp.get("require-dev", {})}
            fw_map = {
                "laravel/framework": "Laravel",
                "laravel/lumen-framework": "Lumen",
                "symfony/symfony": "Symfony", "symfony/framework-bundle": "Symfony",
                "slim/slim": "Slim", "cakephp/cakephp": "CakePHP",
                "yiisoft/yii2": "Yii2", "codeigniter4/framework": "CodeIgniter 4",
                "filament/filament": "Filament (Admin)",
                "livewire/livewire": "Livewire",
                "api-platform/core": "API Platform",
            }
            for key, label in fw_map.items():
                if key in reqs:
                    frameworks.append(label)
        except Exception:
            pass
        results.append((StackType.PHP, frameworks))

    # ── Go ────────────────────────────────────────────────────────────────────
    if (root / "go.mod").exists():
        frameworks = []
        try:
            gomod = (root / "go.mod").read_text().lower()
            fw_signals = {
                "github.com/gin-gonic/gin": "Gin",
                "github.com/gofiber/fiber": "Fiber",
                "github.com/labstack/echo": "Echo",
                "github.com/go-chi/chi": "Chi",
                "github.com/gorilla/mux": "Gorilla Mux",
                "github.com/go-gorm/gorm": "GORM",
                "github.com/uptrace/bun": "Bun (Go)",
            }
            for signal, label in fw_signals.items():
                if signal in gomod:
                    frameworks.append(label)
        except Exception:
            pass
        results.append((StackType.GO, frameworks))

    # ── Rust ──────────────────────────────────────────────────────────────────
    if (root / "Cargo.toml").exists():
        frameworks = []
        try:
            cargo = (root / "Cargo.toml").read_text().lower()
            fw_signals = {
                "axum": "Axum", "actix-web": "Actix-web", "rocket": "Rocket",
                "warp": "Warp", "poem": "Poem", "salvo": "Salvo",
                "sea-orm": "SeaORM", "diesel": "Diesel", "sqlx": "SQLx",
                "tokio": "Tokio", "tonic": "Tonic (gRPC)",
            }
            for signal, label in fw_signals.items():
                if signal in cargo:
                    frameworks.append(label)
        except Exception:
            pass
        results.append((StackType.RUST, frameworks))

    # ── Java / Kotlin ─────────────────────────────────────────────────────────
    has_java = (root / "pom.xml").exists() or (root / "build.gradle").exists()
    has_kotlin = (root / "build.gradle.kts").exists()

    if has_java or has_kotlin:
        frameworks = []
        try:
            _java_buf: io.StringIO = io.StringIO()
            for fname in ["pom.xml", "build.gradle", "build.gradle.kts"]:
                p = root / fname
                if p.exists():
                    _java_buf.write(p.read_text().lower())
            build_text: str = _java_buf.getvalue()
            fw_signals = {
                "spring-boot": "Spring Boot", "spring.boot": "Spring Boot",
                "io.quarkus": "Quarkus", "micronaut": "Micronaut",
                "ktor": "Ktor", "vertx": "Vert.x",
                "jakarta": "Jakarta EE", "javax.enterprise": "Jakarta EE",
                "hibernate": "Hibernate",
            }
            for signal, label in fw_signals.items():
                if signal in build_text:
                    frameworks.append(label)
        except Exception:
            pass
        stack_type = StackType.KOTLIN if has_kotlin and not has_java else StackType.JAVA
        results.append((stack_type, frameworks))

    # ── Ruby ──────────────────────────────────────────────────────────────────
    if (root / "Gemfile").exists():
        frameworks = []
        try:
            gemfile = (root / "Gemfile").read_text().lower()
            fw_signals = {
                "rails": "Ruby on Rails", "sinatra": "Sinatra",
                "hanami": "Hanami", "grape": "Grape API",
                "roda": "Roda", "padrino": "Padrino",
            }
            for signal, label in fw_signals.items():
                if signal in gemfile:
                    frameworks.append(label)
        except Exception:
            pass
        results.append((StackType.RUBY, frameworks))

    # ── Elixir ────────────────────────────────────────────────────────────────
    if (root / "mix.exs").exists():
        frameworks = []
        try:
            mix = (root / "mix.exs").read_text().lower()
            if "phoenix" in mix:
                frameworks.append("Phoenix")
            if "ecto" in mix:
                frameworks.append("Ecto")
            if "broadway" in mix:
                frameworks.append("Broadway")
            if "oban" in mix:
                frameworks.append("Oban")
        except Exception:
            pass
        results.append((StackType.ELIXIR, frameworks))

    # ── .NET / C# ─────────────────────────────────────────────────────────────
    csproj_files = list(root.glob("*.csproj")) + list(root.glob("**/*.csproj"))
    if csproj_files or list(root.glob("*.sln")):
        frameworks = []
        try:
            _csproj_count = 0
            for csproj in csproj_files:
                if _csproj_count >= 3:
                    break
                _csproj_count += 1
                text = csproj.read_text().lower()
                if "microsoft.aspnetcore" in text:
                    frameworks.append("ASP.NET Core")
                if "microsoft.entityframeworkcore" in text:
                    frameworks.append("Entity Framework Core")
                if "maui" in text:
                    frameworks.append(".NET MAUI")
                if "blazor" in text:
                    frameworks.append("Blazor")
        except Exception:
            pass
        results.append((StackType.DOTNET, frameworks))

    # ── Dart / Flutter ────────────────────────────────────────────────────────
    if (root / "pubspec.yaml").exists():
        frameworks = []
        try:
            pubspec = (root / "pubspec.yaml").read_text().lower()
            if "flutter" in pubspec:
                frameworks.append("Flutter")
            if "dart_frog" in pubspec:
                frameworks.append("Dart Frog")
        except Exception:
            pass
        results.append((StackType.DART, frameworks))

    # ── Swift ─────────────────────────────────────────────────────────────────
    if (root / "Package.swift").exists():
        frameworks = []
        try:
            pkg = (root / "Package.swift").read_text().lower()
            if "vapor" in pkg:
                frameworks.append("Vapor")
            if "hummingbird" in pkg:
                frameworks.append("Hummingbird")
            if "swiftui" in pkg:
                frameworks.append("SwiftUI")
        except Exception:
            pass
        results.append((StackType.SWIFT, frameworks))

    if not results:
        results.append((StackType.UNKNOWN, []))

    return results


def detect_environment(root: Path) -> EnvType:
    if (root / ".ddev").exists():
        return EnvType.DDEV
    if (root / "podman-compose.yml").exists() or (root / "podman-compose.yaml").exists():
        return EnvType.PODMAN
    if (root / "docker-compose.yml").exists() or (root / "docker-compose.yaml").exists():
        return EnvType.DOCKER_COMPOSE
    if (root / "Dockerfile").exists():
        return EnvType.DOCKER
    if (root / "flake.nix").exists() or (root / "shell.nix").exists():
        return EnvType.NIX
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
