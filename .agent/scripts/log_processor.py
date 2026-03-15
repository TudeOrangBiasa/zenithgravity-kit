import sys
import re

# ── Error patterns covering TypeScript, Vite/ESBuild, PHP, Python, Go, Rust ──
ERROR_PATTERNS: list[re.Pattern] = [
    re.compile(r'(Error|Exception|Fail(?:ure|ed)?)\b.*', re.IGNORECASE),  # Generic
    re.compile(r'TS\d{4}:', re.IGNORECASE),           # TypeScript: TS2304: Cannot find name
    re.compile(r'\[ERROR\]'),                          # Vite / ESBuild / Maven
    re.compile(r'\[FAIL\]', re.IGNORECASE),            # Generic fail marker
    re.compile(r'^\s*(FAIL|FAILED)\s', re.IGNORECASE), # Jest/Vitest test runner
    re.compile(r'error\[E\d+\]', re.IGNORECASE),       # Rust compiler: error[E0308]
    re.compile(r'panic:'),                             # Go panic
    re.compile(r'Illuminate\\'),                       # Laravel/PHP exception namespace
    re.compile(r'PHP (?:Fatal|Parse|Warning|Notice)'), # PHP interpreter errors
    re.compile(r'SyntaxError:|TypeError:|ReferenceError:'), # JS runtime errors
]

# ── Success markers — keep these to confirm task completion ──
SUCCESS_PATTERNS: list[re.Pattern] = [
    re.compile(r'(PASS(?:ED)?|✓|✅)', re.IGNORECASE),
    re.compile(r'Built in \d'),          # Vite build success
    re.compile(r'Compiled successfully'),# Webpack / CRA
    re.compile(r'Done in \d'),           # Yarn success
    re.compile(r'Tests:\s+\d+ passed'),
    re.compile(r'No (issues|errors) found', re.IGNORECASE),
]

# ── Warning patterns ──
WARNING_PATTERNS: list[re.Pattern] = [
    re.compile(r'\[WARN(?:ING)?\]', re.IGNORECASE),
    re.compile(r'\bwarning\b', re.IGNORECASE),
]


def is_error(line: str) -> bool:
    return any(p.search(line) for p in ERROR_PATTERNS)

def is_success(line: str) -> bool:
    return any(p.search(line) for p in SUCCESS_PATTERNS)

def is_warning(line: str) -> bool:
    return any(p.search(line) for p in WARNING_PATTERNS)


def process_logs(input_text: str) -> str:
    lines = input_text.splitlines()
    if len(lines) <= 50:
        return input_text

    print(f"--- [ LOG SUMMARY: {len(lines)} lines reduced ] ---")

    seen_errors: set[str] = set()
    summary: list[str] = []
    trace_mode = False
    trace_count = 0

    for line in lines:
        # ── Stack trace detection (JS/Python/Java/PHP) ──
        is_trace_line = bool(
            re.search(r'\bat\s+\S+\(|\bFile\s+"|\bTraceback\b', line) or
            (trace_mode and re.match(r'\s{2,}', line))  # continuation indent
        )
        if is_trace_line:
            if not trace_mode:
                trace_mode = True
                trace_count = 0
                summary.append("--- [ Stack Trace ] ---")
            if trace_count < 10:
                summary.append(line)
                trace_count += 1
            elif trace_count == 10:
                summary.append("  ... (trace truncated) ...")
                trace_count += 1
            continue
        else:
            trace_mode = False

        # ── Deduplicate errors by message text ──
        if is_error(line):
            key = re.sub(r'\d+', 'N', line.strip())  # normalize line numbers
            key = "".join(key[i] for i in range(min(120, len(key))))  # trim, Pyre2-safe
            if key not in seen_errors:
                seen_errors.add(key)
                summary.append(line)
            continue

        # ── Always keep success/warning markers ──
        if is_success(line) or is_warning(line):
            summary.append(line)
            continue

        # ── Keep important terminal markers ──
        if any(m in line.upper() for m in ["EXIT CODE", "TIMEOUT", "CRITICAL", "ABORT"]):
            summary.append(line)
            continue

    if not summary:
        head = "\n".join(lines[i] for i in range(min(10, len(lines))))
        tail = "\n".join(lines[i] for i in range(max(0, len(lines) - 10), len(lines)))
        return head + "\n... (omitted) ...\n" + tail

    return "\n".join(summary)


if __name__ == "__main__":
    if not sys.stdin.isatty():
        raw_input = sys.stdin.read()
        print(process_logs(raw_input))
    else:
        print("Usage: cat log_file | python3 log_processor.py")

