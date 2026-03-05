import os
import sys

def verify_kit(root_dir):
    agent_dir = os.path.join(root_dir, '.agent')
    if not os.path.isdir(agent_dir):
        print("❌ Error: .agent directory not found.")
        sys.exit(1)

    errors = []
    
    # 1. Check core rules
    rules_dir = os.path.join(agent_dir, 'rules')
    if not os.path.isfile(os.path.join(rules_dir, 'GEMINI.md')):
        errors.append("Missing core rule: GEMINI.md")

    # 2. Check architecture
    if not os.path.isfile(os.path.join(agent_dir, 'ARCHITECTURE.md')):
        errors.append("Missing ARCHITECTURE.md")

    # 3. Check skills
    skills_dir = os.path.join(agent_dir, 'skills')
    if os.path.isdir(skills_dir):
        for item in os.listdir(skills_dir):
            skill_path = os.path.join(skills_dir, item)
            # We only care about directories that are actual skills (ignore README, etc)
            if os.path.isdir(skill_path):
                skill_md = os.path.join(skill_path, 'SKILL.md')
                if not os.path.isfile(skill_md):
                    errors.append(f"Skill '{item}' is missing SKILL.md")

    if errors:
        print("❌ Agent Verification Failed:")
        for err in errors:
            print(f"  - {err}")
        sys.exit(1)
    
    print("✅ Agent Verification Passed. System is healthy.")

if __name__ == "__main__":
    workspace_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    verify_kit(workspace_root)
