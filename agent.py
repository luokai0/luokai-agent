from core.brain import think
from core.files import list_files, read_file
from core.router import ask
from skills.batch_01.skills import SKILLS
from skills.batch_01.emotional_intelligence import EQ_SKILLS
from skills.skill_forge.forge import forge_skill, load_forged_skills, analyze_and_forge
import os

# Load all skills including self-forged ones
FORGED_SKILLS = load_forged_skills()
ALL_SKILLS = {**SKILLS, **EQ_SKILLS, **FORGED_SKILLS}

print("=" * 50)
print("🐉 LUO KAI AGENT — Online")
print(f"🛠️  {len(ALL_SKILLS)} Skills Loaded")
print("=" * 50)
print("Commands:")
print("  'skills'          → list all skills")
print("  'forge <name>'    → forge a new skill")
print("  'evolve'          → agent decides & forges own skill")
print("  'files'           → list saved files")
print("  'read <name>'     → read a saved file")
print("  'quit'            → exit")
print("-" * 50 + "\n")

while True:
    user_input = input("You: ").strip()
    if not user_input:
        continue

    if user_input.lower() == "quit":
        print("🐉 Luo Kai Agent signing off. See you soon.")
        break

    elif user_input.lower() == "skills":
        print(f"\n🛠️  All {len(ALL_SKILLS)} Skills:")
        for i, skill in enumerate(ALL_SKILLS.keys(), 1):
            print(f"  {i}. {skill}")
        print()

    elif user_input.lower().startswith("forge "):
        parts = user_input[6:].strip().split(":")
        if len(parts) == 2:
            name = parts[0].strip()
            desc = parts[1].strip()
        else:
            name = parts[0].strip()
            desc = input("  Describe what this skill should do: ").strip()
        filepath, code = forge_skill(name, desc)
        if filepath:
            # Reload forged skills
            FORGED_SKILLS = load_forged_skills()
            ALL_SKILLS.update(FORGED_SKILLS)
            print(f"🔥 Skill forged & loaded! Total skills: {len(ALL_SKILLS)}")

    elif user_input.lower() == "evolve":
        print("🧬 Agent is evolving — analyzing history and forging new skill...\n")
        try:
            with open("memory/MEMORY.md", "r") as f:
                history = f.read()
        except:
            history = "No history yet"
        filepath, code = analyze_and_forge(history)
        if filepath:
            FORGED_SKILLS = load_forged_skills()
            ALL_SKILLS.update(FORGED_SKILLS)
            print(f"🧬 Evolution complete! Total skills: {len(ALL_SKILLS)}")

    elif user_input.lower() == "files":
        print("\n📂 Your workspace files:")
        print(list_files())
        print()

    elif user_input.lower().startswith("read "):
        filename = user_input[5:].strip()
        print(f"\n📄 Reading {filename}...")
        print(read_file(f"workspace/{filename}"))
        print()

    else:
        response = think(user_input)
        print(f"\n🐉 Agent: {response}\n")
        print("-" * 50)
