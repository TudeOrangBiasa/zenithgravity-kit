"""
verify_changes.py — Change Verification Runner
Runs one or more shell commands and logs pass/fail results.

Usage:
  python3 .agent/scripts/verify_changes.py "cmd1" ["cmd2" ...]
  python3 .agent/scripts/verify_changes.py --timeout 120 "npm run lint" "npm run typecheck"
"""

import sys
import subprocess
import argparse
from datetime import datetime
from pathlib import Path


# ─────────────────────────────────────────────
# Log path: always absolute, relative to script
# ─────────────────────────────────────────────

SCRIPT_DIR = Path(__file__).resolve().parent
LOG_FILE = SCRIPT_DIR.parent / "logs" / "verification.log"


def log_message(message: str):
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        f.write(f"[{timestamp}] {message}\n")


def run_command(command: str, timeout: int) -> bool:
    print(f"\n\033[1m▶ VERIFICATION:\033[0m {command}")
    log_message(f"RUN: {command}")

    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            timeout=timeout,
        )

        # Always show stdout/stderr so agent can see output
        if result.stdout.strip():
            print(result.stdout.rstrip())
        if result.stderr.strip():
            print(result.stderr.rstrip(), file=sys.stderr)

        if result.returncode == 0:
            print(f"\033[92m✅ PASSED\033[0m")
            log_message(f"PASS: {command}")
            return True
        else:
            print(f"\033[91m❌ FAILED (exit code: {result.returncode})\033[0m")
            log_message(f"FAIL: {command} (Code: {result.returncode})")
            return False

    except subprocess.TimeoutExpired:
        print(f"\033[91m⏱  TIMEOUT after {timeout}s\033[0m")
        log_message(f"TIMEOUT: {command} (after {timeout}s)")
        return False
    except Exception as e:
        print(f"\033[91m🔴 EXECUTION ERROR: {e}\033[0m")
        log_message(f"ERROR: {command} — {e}")
        return False


def main():
    parser = argparse.ArgumentParser(
        description="Run shell verification commands and log results."
    )
    parser.add_argument(
        "commands", nargs="+",
        help="One or more shell commands to verify"
    )
    parser.add_argument(
        "--timeout", type=int, default=120,
        help="Timeout in seconds per command (default: 120)"
    )
    args = parser.parse_args()

    print(f"\033[1m🔍 Running {len(args.commands)} verification command(s) — timeout: {args.timeout}s\033[0m")

    results: list[bool] = []

    for cmd in args.commands:
        results.append(run_command(cmd, args.timeout))

    passed: int = sum(1 for r in results if r)
    failed: int = sum(1 for r in results if not r)

    print(f"\n\033[1mSummary:\033[0m {passed} passed, {failed} failed")

    if failed > 0:
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
