"""
ki_lookup.py — Knowledge Item Lookup
Search KI directory for topics matching one or more keywords.

Usage:
  python3 .agent/scripts/ki_lookup.py <keyword> [keyword2 ...]
  python3 .agent/scripts/ki_lookup.py vue component
"""

import os
import sys
import json
from pathlib import Path


# ─────────────────────────────────────────────
# KI directory: portable, uses HOME env var
# ─────────────────────────────────────────────

def get_ki_dir() -> Path:
    """Resolve KI directory dynamically from HOME, not hardcoded."""
    home = Path.home()
    # Try known locations in order
    candidates = [
        home / ".gemini" / "antigravity" / "knowledge",
        home / ".config" / "antigravity" / "knowledge",
    ]
    for candidate in candidates:
        if candidate.exists():
            return candidate
    # Return first candidate as default (will show not-found message)
    return candidates[0]


# ─────────────────────────────────────────────
# Lookup
# ─────────────────────────────────────────────

def score_match(content: str, keywords: list[str]) -> int:
    """Count how many keywords appear in content (case-insensitive)."""
    lower = content.lower()
    return sum(1 for kw in keywords if kw.lower() in lower)


def lookup_ki(keywords: list[str]):
    ki_dir = get_ki_dir()

    if not ki_dir.exists():
        print(f"⚠️  KI directory not found at: {ki_dir}")
        print("    Run the knowledge sync pipeline to populate it.")
        return

    query = " ".join(keywords)
    print(f"🔍 Searching Knowledge Items for: '{query}'")
    print(f"   KI Store: {ki_dir}\n")

    matches: list[tuple[int, str, str, str]] = []  # (score, ki_name, summary, artifact_path)

    for root, dirs, files in os.walk(ki_dir):
        if "metadata.json" in files:
            meta_path = os.path.join(root, "metadata.json")
            try:
                with open(meta_path, "r") as f:
                    raw = f.read()
                score = score_match(raw, keywords)

                # ── ENHANCEMENT: Also score from artifact file contents ──
                artifacts_dir = Path(root) / "artifacts"
                artifact_path = ""
                if artifacts_dir.exists():
                    artifact_files = sorted(artifacts_dir.iterdir())
                    if artifact_files:
                        artifact_path = str(artifact_files[0])
                        for af in artifact_files:
                            try:
                                artifact_score = score_match(af.read_text(encoding="utf-8", errors="ignore"), keywords)
                                score = max(score, artifact_score)  # take best match
                            except Exception:
                                pass

                if score > 0:
                    ki_name = os.path.basename(root)
                    try:
                        data = json.loads(raw)
                        summary = data.get("summary", "No summary available.")
                    except (json.JSONDecodeError, Exception):
                        summary = "(could not parse metadata)"

                    matches.append((score, ki_name, summary, artifact_path))
            except Exception:
                continue

    if not matches:
        print(f"ℹ️  No relevant Knowledge Items found for '{query}'.")
        return

    # Sort by relevance score descending
    matches.sort(key=lambda x: (x[0],), reverse=True)

    print(f"✅ Found {len(matches)} relevant Knowledge Item(s) (sorted by relevance):\n")
    for score, name, summary, artifact in matches:
        relevance = "●" * min(score, 5)  # max 5 dots
        print(f"  [{relevance}] \033[1m{name}\033[0m (score: {score})")
        # Trim summary to 120 chars — use join to avoid Pyre2 slice false-positive
        chars = list(summary)
        truncated = "".join(chars[i] for i in range(min(120, len(chars))))
        short_summary = (truncated + "...") if len(summary) > 120 else truncated
        print(f"       {short_summary}")
        if artifact:
            print(f"       📄 Artifact: {artifact}")
        print()


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 ki_lookup.py <keyword> [keyword2 ...]")
        print("Example: python3 ki_lookup.py vue component")
        sys.exit(0)

    keywords: list[str] = list(sys.argv[i] for i in range(1, len(sys.argv)))
    lookup_ki(keywords)


if __name__ == "__main__":
    main()
