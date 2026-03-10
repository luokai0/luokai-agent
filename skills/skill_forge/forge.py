from core.router import ask
from core.files import write_file
from core.git_sync import git_push
from datetime import datetime
import os
import importlib.util

FORGE_DIR = "skills/skill_forge"
os.makedirs(FORGE_DIR, exist_ok=True)

def timestamp():
    return datetime.now().strftime("%Y%m%d_%H%M%S")

def forge_skill(skill_name, skill_description):
    """Agent writes a brand new skill by itself"""
    print(f"⚒️  Forging new skill: {skill_name}...")

    prompt = f"""You are an expert Python developer building skills for an AI agent called Luo Kai Agent.

Write a complete Python skill module for:
Skill name: {skill_name}
Description: {skill_description}

STRICT RULES:
1. Import only: from core.router import ask | from core.files import write_file | from core.search import search, search_news | from datetime import datetime | import os
2. Every function must use ask() to think and write_file() to save results
3. Include 3-7 related functions
4. End with a SKILLS dict mapping name to function
5. Add print statement showing how many skills loaded
6. Write clean, working Python code only — no explanations

Return ONLY the Python code, nothing else."""

    code = ask(prompt)

    # Clean the code
    if "```python" in code:
        code = code.split("```python")[1].split("```")[0].strip()
    elif "```" in code:
        code = code.split("```")[1].split("```")[0].strip()

    # Save the skill file
    filename = skill_name.lower().replace(" ", "_")
    filepath = f"{FORGE_DIR}/{filename}.py"
    with open(filepath, "w") as f:
        f.write(code)

    print(f"✅ New skill forged: {filepath}")

    with open("memory/MEMORY.md", "a") as f:
        f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M')}] Forged new skill: {skill_name}\n")

    # AUTO PUSH TO GITHUB 🚀
    git_push(f"🧬 Forged new skill: {skill_name}")

    return filepath, code

def load_forged_skills():
    """Load all self-forged skills automatically"""
    forged = {}
    if not os.path.exists(FORGE_DIR):
        return forged

    for filename in os.listdir(FORGE_DIR):
        if filename.endswith(".py") and filename not in ["forge.py", "__init__.py"]:
            try:
                spec = importlib.util.spec_from_file_location(
                    filename[:-3],
                    os.path.join(FORGE_DIR, filename)
                )
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                if hasattr(module, "SKILLS"):
                    forged.update(module.SKILLS)
                    print(f"🔄 Loaded forged skill: {filename}")
            except Exception as e:
                print(f"⚠️ Could not load {filename}: {e}")

    return forged

def analyze_and_forge(task_history):
    """Agent analyzes its own task history and decides what skill to forge next"""
    print("🧠 Agent analyzing task history to decide next skill to forge...")

    prompt = f"""You are Luo Kai Agent analyzing your own task history to decide what ONE new skill to build.

Task history:
{task_history}

Pick the SINGLE most valuable skill to build next.

Respond in EXACTLY this format with no numbering, no extra text:
SKILL_NAME: example_skill_name
SKILL_DESCRIPTION: one sentence describing what it does
REASON: why this skill will be valuable"""

    response = ask(prompt)
    print(f"🤔 Agent decided:\n{response}")

    skill_name = ""
    skill_desc = ""

    for line in response.strip().split("\n"):
        line = line.strip()
        if line.startswith("SKILL_NAME:"):
            skill_name = line.replace("SKILL_NAME:", "").strip()
        elif line.startswith("SKILL_DESCRIPTION:"):
            skill_desc = line.replace("SKILL_DESCRIPTION:", "").strip()

    if skill_name and skill_desc:
        return forge_skill(skill_name, skill_desc)
    else:
        print("⚠️ Parsing failed — forging most valuable skill directly...")
        return forge_skill("data_analysis", "Analyze data and extract insights to help make money decisions")

print("⚒️  Skill Forge loaded — Agent can now create its own skills!")
