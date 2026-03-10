import os
import json
import json
from enum import Enum
from pathlib import Path

class StackType(Enum):
    NODE = "Node.js"
    PHP = "PHP"
    PYTHON = "Python"
    GO = "Go"
    RUST = "Rust"
    JAVA = "Java"
    UNKNOWN = "Unknown"

class EnvType(Enum):
    DDEV = "DDEV"
    DOCKER_COMPOSE = "Docker Compose"
    DOCKER = "Docker"
    NATIVE = "Native"

def detect_stack(project_root: str):
    root = Path(project_root)
    stack = StackType.UNKNOWN
    frameworks = []
    
    # Python detection
    if (root / "requirements.txt").exists() or (root / "Pipfile").exists() or (root / "pyproject.toml").exists():
        stack = StackType.PYTHON
        if (root / "manage.py").exists():
            frameworks.append("Django")
            
    # Node detection
    elif (root / "package.json").exists():
        stack = StackType.NODE
        try:
            with open(root / "package.json", "r") as f:
                pkg = json.load(f)
                deps = {**pkg.get("dependencies", {}), **pkg.get("devDependencies", {})}
                if "next" in deps: frameworks.append("Next.js")
                if "react" in deps: frameworks.append("React")
                if "vue" in deps: frameworks.append("Vue")
                if "express" in deps: frameworks.append("Express")
                if "svelte" in deps: frameworks.append("Svelte")
                if "@nestjs/core" in deps: frameworks.append("NestJS")
                if "@adonisjs/core" in deps: frameworks.append("AdonisJS")
                if "nuxt" in deps: frameworks.append("Nuxt")
                if "astro" in deps: frameworks.append("Astro")
        except:
            pass
            
    # PHP detection
    elif (root / "composer.json").exists():
        stack = StackType.PHP
        try:
            with open(root / "composer.json", "r") as f:
                comp = json.load(f)
                reqs = {**comp.get("require", {}), **comp.get("require-dev", {})}
                if "laravel/framework" in reqs: frameworks.append("Laravel")
                if "symfony/symfony" in reqs: frameworks.append("Symfony")
        except:
            pass
            
    # Go detection
    elif (root / "go.mod").exists():
        stack = StackType.GO
        
    # Rust detection
    elif (root / "Cargo.toml").exists():
        stack = StackType.RUST

    # Java detection
    elif (root / "pom.xml").exists() or (root / "build.gradle").exists():
        stack = StackType.JAVA
        if (root / "pom.xml").exists():
            try:
                with open(root / "pom.xml", "r", encoding="utf-8") as f:
                    content = f.read()
                    if "spring-boot" in content: frameworks.append("Spring Boot")
            except:
                pass
                
    return stack, frameworks

def detect_environment(project_root: str):
    root = Path(project_root)
    
    if (root / ".ddev").exists():
        return EnvType.DDEV
        
    if (root / "docker-compose.yml").exists() or (root / "docker-compose.yaml").exists():
        return EnvType.DOCKER_COMPOSE
        
    if (root / "Dockerfile").exists():
        return EnvType.DOCKER
        
    return EnvType.NATIVE

def get_command_prefix(env_type: EnvType) -> str:
    if env_type == EnvType.DDEV:
        return "ddev "
    # Docker compose is ambiguous (which service?), usually needs manual resolution by AI
    # But for a highly targeted report, we will just inform the AI
    return ""

def generate_report(project_root: str):
    root = Path(project_root)
    stack, frameworks = detect_stack(project_root)
    env = detect_environment(project_root)
    
    report = [
        "STACK REPORT",
        f"Language/Platform : {stack.value}",
        f"Frameworks        : {', '.join(frameworks) if frameworks else 'None detected'}",
        f"Environment       : {env.value}"
    ]

    has_frontend = any(fw in frameworks for fw in ['Next.js', 'React', 'Vue', 'Svelte', 'Nuxt', 'Astro'])
    if has_frontend or stack == StackType.NODE:
        report.append("UI Guidelines     : Active -> `ux-humanist-designer` (Enforce mathematical layouts & anti-slop rules).")
        
    has_backend = any(fw in frameworks for fw in ['Django', 'Express', 'NestJS', 'Laravel', 'Symfony', 'Spring Boot', 'AdonisJS']) or stack in [StackType.GO, StackType.PYTHON, StackType.PHP, StackType.RUST, StackType.JAVA]
    if has_backend or (stack == StackType.NODE and not has_frontend):
        report.append("Architecture Guide: Active -> `system-architect` (Enforce Clean Architecture, DDD, Modular boundaries).")
        report.append("API & Integration : Active -> `api-architect` (Enforce REST/GraphQL standards & Payload structure).")
        report.append("Database & Schema : Active -> `database-architect` (Enforce Indexing, Normalization, N+1 Prevention).")
        
    # Security and DevOps are always enabled regardless of stack
    report.append("Security & Review : Active -> `sec-ops` (Enforce OWASP principles & Code Review severity rating).")
    report.append("DevOps & CI/CD    : Active -> `devops-architect` (Enforce Container Immutability & Deployment pipelines).")
    
    # Check for shell scripts or Makefiles
    files = [f.name for f in root.iterdir() if f.is_file()]
    if any(f.endswith(".sh") for f in files) or "Makefile" in files or ".bashrc" in files:
        report.append("Automation Scripts: Active -> `automation-engineer` (Enforce Bash Standards & Bats Testing).")
    
    report.append("Error Resolution  : Active -> `systematic-debugging` (Enforce Root-Cause 5-Whys Global Trigger).")
    
    prefix = get_command_prefix(env)
    if prefix:
        report.append(f"Command Prefix    : MUST prepend all commands with `{prefix}` (e.g., `{prefix}composer install`, `{prefix}npm install`)")
    elif env == EnvType.DOCKER_COMPOSE:
         report.append("Command Guideline : Docker Compose detected. Make sure to run commands inside the appropriate container using `docker-compose exec <service> <command>`.")
    else:
        report.append("Command Guideline : Run commands natively.")
        
    return "\n".join(report)

if __name__ == "__main__":
    import sys
    # Default to current working directory
    target_dir = sys.argv[1] if len(sys.argv) > 1 else "."
    
    print(generate_report(target_dir))
