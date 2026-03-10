from core.brain import think
from core.files import list_files, read_file
from skills.batch_01.skills import SKILLS

print("=" * 50)
print("🐉 LUO KAI AGENT — Online")
print(f"🛠️  {len(SKILLS)} Skills Loaded")
print("=" * 50)
print("Commands:")
print("  'skills'       → list all skills")
print("  'files'        → list saved files")
print("  'read <name>'  → read a saved file")
print("  'quit'         → exit")
print("-" * 50 + "\n")

while True:
    user_input = input("You: ").strip()
    if not user_input:
        continue

    if user_input.lower() == "quit":
        print("🐉 Luo Kai Agent signing off. See you soon.")
        break

    elif user_input.lower() == "skills":
        print("\n🛠️  Available Skills:")
        for i, skill in enumerate(SKILLS.keys(), 1):
            print(f"  {i}. {skill}")
        print()

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
