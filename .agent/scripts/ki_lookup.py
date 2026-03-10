import os
import sys

def lookup_ki(topic):
    ki_dir = "/home/todayz/.gemini/antigravity/knowledge"
    if not os.path.exists(ki_dir):
        print(f"⚠️ KI directory not found at {ki_dir}")
        return

    print(f"🔍 Searching Knowledge Items for: '{topic}'")
    matches = []
    
    # Simple keyword-based scan of KI names and summaries
    for root, dirs, files in os.walk(ki_dir):
        for file in files:
            if file == "metadata.json":
                path = os.path.join(root, file)
                try:
                    with open(path, 'r') as f:
                        content = f.read().lower()
                        if topic.lower() in content:
                            # Extract KI name from path
                            ki_name = os.path.basename(root)
                            matches.append(ki_name)
                except:
                    continue

    if matches:
        print(f"✅ Found {len(matches)} relevant Knowledge Items:")
        for match in set(matches):
            print(f" - {match}")
    else:
        print(f"ℹ️ No relevant Knowledge Items found for '{topic}'.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        topic = " ".join(sys.argv[1:])
        lookup_ki(topic)
    else:
        print("Usage: python ki_lookup.py <topic_keyword>")
