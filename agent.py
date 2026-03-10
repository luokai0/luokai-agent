from core.brain import think
from core.files import list_files, read_file
from skills.batch_01.skills import SKILLS as BATCH01
from skills.batch_01.emotional_intelligence import EQ_SKILLS
from skills.batch_02.skills import SKILLS as BATCH02
from skills.batch_03.skills import SKILLS as BATCH03
from skills.skill_forge.forge import forge_skill, load_forged_skills, analyze_and_forge

FORGED_SKILLS = load_forged_skills()
ALL_SKILLS = {**BATCH01, **EQ_SKILLS, **BATCH02, **BATCH03, **FORGED_SKILLS}

print("=" * 50)
print("🐉 LUO KAI AGENT — Online")
print(f"🛠️  {len(ALL_SKILLS)} Skills Loaded")
print("=" * 50)
print("Commands:")
print("  'skills'          → list all skills")
print("  'forge <name>'    → forge a new skill")
print("  'evolve'          → agent forges its own skill")
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
        name = parts[0].strip()
        desc = parts[1].strip() if len(parts) > 1 else input("  Describe this skill: ").strip()
        filepath, code = forge_skill(name, desc)
        if filepath:
            FORGED_SKILLS = load_forged_skills()
            ALL_SKILLS.update(FORGED_SKILLS)
            print(f"🔥 Total skills: {len(ALL_SKILLS)}")

    elif user_input.lower() == "evolve":
        print("🧬 Evolving...\n")
        try:
            with open("memory/MEMORY.md", "r") as f:
                history = f.read()
        except:
            history = "No history yet"
        filepath, code = analyze_and_forge(history)
        if filepath:
            FORGED_SKILLS = load_forged_skills()
            ALL_SKILLS.update(FORGED_SKILLS)
            print(f"🧬 Total skills: {len(ALL_SKILLS)}")

    elif user_input.lower() == "files":
        print("\n📂 Workspace files:")
        print(list_files())
        print()

    elif user_input.lower().startswith("read "):
        filename = user_input[5:].strip()
        print(read_file(f"workspace/{filename}"))

    else:
        response = think(user_input)
        print(f"\n🐉 Agent: {response}\n")
        print("-" * 50)
