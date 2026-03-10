import os
import json
import subprocess
import sys

def run_command(cmd):
    print(f"Sandbox Validation: {cmd}")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        print("SUCCESS")
        return True
    else:
        print(f"FAILED (Exit Code: {result.returncode})")
        print(result.stdout)
        print(result.stderr)
        return False

def detect_and_verify():
    # 1. Detect Stack via package.json or common files
    if os.path.exists("package.json"):
        with open("package.json", "r") as f:
            data = json.load(f)
            scripts = data.get("scripts", {})
            if "lint" in scripts:
                if not run_command("npm run lint"): sys.exit(1)
            if "test" in scripts:
                print("Skipping heavy tests, running targeted linter.")
    
    if os.path.exists("composer.json"):
        if os.path.exists("vendor/bin/phpstan"):
            if not run_command("./vendor/bin/phpstan analyse"): sys.exit(1)

    if os.path.exists("manage.py"): # Django
        if not run_command("python3 manage.py check"): sys.exit(1)

    print("Sandbox verification complete.")

if __name__ == "__main__":
    detect_and_verify()
