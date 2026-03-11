"""
verify_agent.py — Agent Kit Health Check
Validates that all required .agent/ files and structures are present.

Usage:
  python3 .agent/scripts/verify_agent.py [--root /path/to/project]
"""

import os
import sys
import argparse
from pathlib import Path
from typing import Optional


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
# Checks
# ─────────────────────────────────────────────

def ok(msg: str):
    print(f"  \033[92m✅ {msg}\033[0m")

def fail(msg: str):
    print(f"  \033[91m❌ {msg}\033[0m")

def info(msg: str):
    print(f"  \033[93m⚠️  {msg}\033[0m")


REQUIRED_SCRIPTS = [
    "sync_memory.py",
    "verify_agent.py",
    "verify_changes.py",
    "ki_lookup.py",
    "sandbox_verify.py",
    "detect_stack.py",
]

REQUIRED_MEMORY_FILES = [
    "design-system.md",
    "system-architecture.md",
]


def verify_kit(root_dir: Path) -> bool:
    agent_dir = root_dir / ".agent"
    errors: list[str] = []
    warnings: list[str] = []

    print(f"\n\033[1m🔍 Agent Kit Verification\033[0m")
    print(f"   Root: {root_dir}\n")

    # ── 1. .agent directory ──────────────────────────
    if not agent_dir.is_dir():
        fail(".agent/ directory not found — is this a zenithgravity-kit project?")
        return False
    ok(".agent/ directory exists")

    # ── 2. Core rules ─────────────────────────────────
    rules_dir = agent_dir / "rules"
    if (rules_dir / "GEMINI.md").is_file():
        ok("rules/GEMINI.md")
    else:
        errors.append("Missing core rule: rules/GEMINI.md")
        fail("rules/GEMINI.md")

    # ── 3. ARCHITECTURE.md ────────────────────────────
    if (agent_dir / "ARCHITECTURE.md").is_file():
        ok("ARCHITECTURE.md")
    else:
        errors.append("Missing ARCHITECTURE.md")
        fail("ARCHITECTURE.md")

    # ── 4. Skills ─────────────────────────────────────
    skills_dir = agent_dir / "skills"
    if skills_dir.is_dir():
        missing_skills = []
        for item in sorted(skills_dir.iterdir()):
            if item.is_dir():
                if not (item / "SKILL.md").is_file():
                    missing_skills.append(item.name)
                    errors.append(f"Skill '{item.name}' is missing SKILL.md")
                    fail(f"skills/{item.name}/SKILL.md")
                else:
                    ok(f"skills/{item.name}/SKILL.md")
    else:
        warnings.append("No skills/ directory found")
        info("skills/ directory not found")

    # ── 5. Workflows ──────────────────────────────────
    workflows_dir = agent_dir / "workflows"
    if workflows_dir.is_dir():
        wf_count = len(list(workflows_dir.glob("*.md")))
        ok(f"workflows/ ({wf_count} workflows)")
    else:
        warnings.append("No workflows/ directory found")
        info("workflows/ directory not found")

    # ── 6. Required scripts ───────────────────────────
    scripts_dir = agent_dir / "scripts"
    if scripts_dir.is_dir():
        for script in REQUIRED_SCRIPTS:
            if (scripts_dir / script).is_file():
                ok(f"scripts/{script}")
            else:
                errors.append(f"Missing required script: scripts/{script}")
                fail(f"scripts/{script}")
    else:
        errors.append("Missing scripts/ directory entirely")
        fail("scripts/ directory not found")

    # ── 7. Memory files ───────────────────────────────
    memory_dir = agent_dir / "memory"
    if memory_dir.is_dir():
        for mf in REQUIRED_MEMORY_FILES:
            if (memory_dir / mf).is_file():
                ok(f"memory/{mf}")
            else:
                warnings.append(f"Memory file not synced: memory/{mf} — run sync_memory.py")
                info(f"memory/{mf} — run `python3 .agent/scripts/sync_memory.py` to generate")
    else:
        warnings.append("memory/ directory not present — run sync_memory.py first")
        info("memory/ directory missing — run sync_memory.py")

    # ── Summary ───────────────────────────────────────
    print()
    if errors:
        print(f"\033[91m✗ Verification FAILED — {len(errors)} error(s), {len(warnings)} warning(s)\033[0m")
        return False
    elif warnings:
        print(f"\033[93m⚠ Verification PASSED with {len(warnings)} warning(s)\033[0m")
        return True
    else:
        print(f"\033[92m✓ Agent Verification PASSED — System is healthy.\033[0m")
        return True


def main():
    parser = argparse.ArgumentParser(
        description="Verify agent kit structure and required files."
    )
    parser.add_argument(
        "--root", type=str, default=None,
        help="Project root. Defaults to nearest ancestor containing .agent/"
    )
    args = parser.parse_args()

    if args.root:
        root = Path(args.root).resolve()
    else:
        root = find_project_root()

    passed = verify_kit(root)
    sys.exit(0 if passed else 1)


if __name__ == "__main__":
    main()
