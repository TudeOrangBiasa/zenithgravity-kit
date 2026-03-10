import sys
import subprocess
import os
from datetime import datetime

def log_message(message, log_file=".agent/logs/verification.log"):
    os.makedirs(os.path.dirname(log_file), exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a") as f:
        f.write(f"[{timestamp}] {message}\n")

def main():
    print("\033[91mERROR: No verification command provided.\033[0m")
    sys.exit(1)

    command = sys.argv[1]
    
    print(f"VERIFICATION: {command}")
    
    log_message(f"RUN: {command}")

    try:
        # Use shell=True to support shell built-ins and pipes
        result = subprocess.run(command, shell=True, capture_output=False)
        exit_code = result.returncode
    except Exception as e:
        print(f"\033[91m🔴 EXECUTION ERROR: {str(e)}\033[0m")
        exit_code = 1

    if exit_code == 0:
        print("\033[92mPASSED\033[0m")
        log_message(f"PASS: {command}")
        sys.exit(0)
    else:
        print(f"\033[91mFAILED (Code: {exit_code})\033[0m")
        log_message(f"FAIL: {command} (Code: {exit_code})")
        sys.exit(exit_code)

if __name__ == "__main__":
    main()
