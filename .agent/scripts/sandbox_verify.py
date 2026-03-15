"""
sandbox_verify.py — Sandbox Static Verification
Detects project stack and runs lightweight static checks (lint, type-check, analysis).
Does NOT run heavy test suites or start servers.

Usage:
  python3 .agent/scripts/sandbox_verify.py [--root /path/to/project]
"""

import sys
import json
import argparse
import subprocess
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


def tail_lines(lines: list[str], n: int) -> list[str]:
    """Return last n lines from a list — avoids Pyre2 slice inference issues."""
    start_idx: int = max(0, len(lines) - n)
    result: list[str] = []
    for i in range(start_idx, len(lines)):
        result.append(lines[i])
    return result


# ─────────────────────────────────────────────
# Output helpers
# ─────────────────────────────────────────────

def run_check(label: str, cmd: str, cwd: Path) -> bool:
    print(f"  ▶ {label}: \033[90m{cmd}\033[0m")
    try:
        result = subprocess.run(
            cmd, shell=True, capture_output=True, text=True, cwd=str(cwd), timeout=120
        )
        if result.returncode == 0:
            print(f"    \033[92m✅ PASS\033[0m")
            return True
        else:
            print(f"    \033[91m❌ FAIL (exit: {result.returncode})\033[0m")
            if result.stdout.strip():
                all_out: list[str] = cast(list[str], result.stdout.strip().splitlines())
                for line in tail_lines(all_out, 10):
                    print(f"    {line}")
            if result.stderr.strip():
                all_err: list[str] = cast(list[str], result.stderr.strip().splitlines())
                for line in tail_lines(all_err, 10):
                    print(f"    \033[91m{line}\033[0m")
            return False
    except subprocess.TimeoutExpired:
        print(f"    \033[91m⏱  TIMEOUT (120s)\033[0m")
        return False
    except Exception as e:
        print(f"    \033[91m🔴 ERROR: {e}\033[0m")
        return False


# ─────────────────────────────────────────────
# Stack detectors → checks
# ─────────────────────────────────────────────

def verify_node(root: Path, results: list):
    pkg_path = root / "package.json"
    if not pkg_path.exists():
        return

    print("\n\033[1m📦 Node.js / Frontend\033[0m")
    try:
        data = json.loads(pkg_path.read_text())
    except Exception:
        print("  ⚠️  Could not parse package.json")
        return

    scripts = data.get("scripts", {})
    
    # Automatically map target scripts without forcing specific lint names
    for target in ["lint", "typecheck", "test", "build"]:
        if target in scripts:
            results.append(run_check(f"npm run {target}", f"npm run {target} 2>&1 | head -50", root))


def verify_php(root: Path, results: list):
    if not (root / "composer.json").exists():
        return

    print("\n\033[1m🐘 PHP\033[0m")
    phpstan = root / "vendor" / "bin" / "phpstan"
    pint = root / "vendor" / "bin" / "pint"

    if phpstan.exists():
        results.append(run_check("PHPStan", "./vendor/bin/phpstan analyse --memory-limit=256M", root))
    if pint.exists():
        results.append(run_check("Laravel Pint (dry-run)", "./vendor/bin/pint --test", root))


def verify_python(root: Path, results: list):
    has_req = (root / "requirements.txt").exists()
    has_setup = (root / "pyproject.toml").exists()
    has_manage = (root / "manage.py").exists()

    if not (has_req or has_setup or has_manage):
        return

    print("\n\033[1m🐍 Python\033[0m")
    if has_manage:
        results.append(run_check("Django system check", "python3 manage.py check", root))

    # Try ruff as a fast linter
    try:
        subprocess.run("ruff --version", shell=True, capture_output=True, check=True)
        results.append(run_check("Ruff lint", "ruff check .", root))
    except Exception:
        pass


def verify_go(root: Path, results: list):
    if not (root / "go.mod").exists():
        return
    print("\n\033[1m🐹 Go\033[0m")
    results.append(run_check("go build", "go build ./...", root))
    results.append(run_check("go vet", "go vet ./...", root))


def verify_rust(root: Path, results: list):
    if not (root / "Cargo.toml").exists():
        return
    print("\n\033[1m🦀 Rust\033[0m")
    results.append(run_check("cargo check", "cargo check", root))
    results.append(run_check("cargo clippy", "cargo clippy -- -D warnings", root))


# ─────────────────────────────────────────────
# Main
# ─────────────────────────────────────────────

def detect_and_verify(root: Path):
    print(f"\033[1m🔬 Sandbox Verification\033[0m")
    print(f"   Root: {root}")

    results: list[bool] = []

    verify_node(root, results)
    verify_php(root, results)
    verify_python(root, results)
    verify_go(root, results)
    verify_rust(root, results)

    if not results:
        print("\n⚠️  No recognizable stack found in project root.")
        print("   Provide --root if running from a different directory.")
        sys.exit(0)

    passed = sum(1 for r in results if r)
    failed = len(results) - passed

    print(f"\n{'─'*40}")
    if failed == 0:
        print(f"\033[92m✅ All {passed} check(s) passed.\033[0m")
    else:
        print(f"\033[91m❌ {failed} check(s) failed, {passed} passed.\033[0m")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description="Run sandbox static verification on the project."
    )
    parser.add_argument(
        "--root", type=str, default=None,
        help="Project root path. Defaults to nearest ancestor containing .agent/"
    )
    args = parser.parse_args()

    root = Path(args.root).resolve() if args.root else find_project_root()
    detect_and_verify(root)


if __name__ == "__main__":
    main()
