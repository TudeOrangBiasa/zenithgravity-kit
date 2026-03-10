import sys
import re

def process_logs(input_text):
    lines = input_text.splitlines()
    if len(lines) <= 50:
        return input_text

    print(f"--- [ LOG SUMMARY: {len(lines)} lines reduced ] ---")
    
    # Simple deduplication and trace extraction
    seen_errors = set()
    summary = []
    trace_mode = False
    trace_count = 0

    for line in lines:
        # Detect stack trace patterns
        if "at " in line or "stack trace" in line.lower() or "File \"" in line:
            if not trace_mode:
                trace_mode = True
                trace_count = 0
                summary.append("--- [ Stack Trace Detected ] ---")
            
            if trace_count < 10:
                summary.append(line)
                trace_count += 1
            elif trace_count == 10:
                summary.append("... (trace truncated) ...")
                trace_count += 1
            continue
        else:
            trace_mode = False

        # Detect error patterns for deduplication
        error_match = re.search(r'(Error|Exception|Fail): (.*)', line, re.IGNORECASE)
        if error_match:
            error_msg = error_match.group(2).strip()
            if error_msg not in seen_errors:
                seen_errors.add(error_msg)
                summary.append(line)
            continue

        # Keep important markers
        if any(marker in line.upper() for marker in ["PASSED", "FAILED", "WARNING", "CRITICAL", "EXIT CODE"]):
            summary.append(line)
            continue

    if not summary:
        return "\n".join(lines[:10]) + "\n... (omitted) ...\n" + "\n".join(lines[-10:])
        
    return "\n".join(summary)

if __name__ == "__main__":
    if not sys.stdin.isatty():
        raw_input = sys.stdin.read()
        print(process_logs(raw_input))
    else:
        print("Usage: cat log_file | python log_processor.py")
