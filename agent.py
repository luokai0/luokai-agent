from core.brain import think
from core.files import list_files, read_file
from core.moltbook import status, post, feed, auto_post, communities, heartbeat
from skills.batch_01.skills import SKILLS as BATCH01
from skills.batch_01.emotional_intelligence import EQ_SKILLS
from skills.batch_02.skills import SKILLS as BATCH02
from skills.batch_03.skills import SKILLS as BATCH03
from skills.batch_04.skills import SKILLS as BATCH04
from skills.batch_05.skills import SKILLS as BATCH05
from skills.batch_06.skills import SKILLS as BATCH06
from skills.skill_forge.forge import forge_skill, load_forged_skills, analyze_and_forge

FORGED_SKILLS = load_forged_skills()
ALL_SKILLS = {**BATCH01, **EQ_SKILLS, **BATCH02, **BATCH03, **BATCH04, **BATCH05, **BATCH06, **FORGED_SKILLS}

print("=" * 50)
print("🐉 LUO KAI AGENT — Online")
print(f"🛠️  {len(ALL_SKILLS)} Skills Loaded")
print("=" * 50)
print("Commands:")
print("  'skills'            → list all skills")
print("  'forge <name>'      → forge a new skill")
print("  'evolve'            → agent forges its own skill")
print("  'files'             → list saved files")
print("  'read <name>'       → read a file")
print("  'mb status'         → Moltbook status")
print("  'mb feed'           → read Moltbook feed")
print("  'mb post <topic>'   → auto post to Moltbook")
print("  'mb communities'    → list communities")
print("  'mb heartbeat'      → check notifications")
print("  'quit'              → exit")
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
        for i, s in enumerate(ALL_SKILLS.keys(), 1):
            print(f"  {i}. {s}")
        print()

    elif user_input.lower() == "mb status":
        print("\n🦞 Moltbook Status:")
        print(status())
        print()

    elif user_input.lower() == "mb feed":
        print("\n🦞 Moltbook Feed:")
        print(feed())
        print()

    elif user_input.lower().startswith("mb post "):
        topic = user_input[8:].strip()
        print(f"\n🦞 Posting about: {topic}")
        print(auto_post(topic))
        print()

    elif user_input.lower() == "mb communities":
        print("\n🦞 Communities:")
        print(communities())
        print()

    elif user_input.lower() == "mb heartbeat":
        heartbeat()
        print()

    elif user_input.lower().startswith("forge "):
        parts = user_input[6:].strip().split(":")
        name = parts[0].strip()
        desc = parts[1].strip() if len(parts) > 1 else input("  Describe: ").strip()
        filepath, code = forge_skill(name, desc)
        if filepath:
            FORGED_SKILLS = load_forged_skills()
            ALL_SKILLS.update(FORGED_SKILLS)
            print(f"🔥 Total: {len(ALL_SKILLS)}")

    elif user_input.lower() == "evolve":
        print("🧬 Evolving...\n")
        try:
            with open("memory/MEMORY.md", "r") as f:
                history = f.read()
        except:
            history = "No history"
        filepath, code = analyze_and_forge(history)
        if filepath:
            FORGED_SKILLS = load_forged_skills()
            ALL_SKILLS.update(FORGED_SKILLS)
            print(f"🧬 Total: {len(ALL_SKILLS)}")

    elif user_input.lower() == "create gmail":
        print("\n📧 Creating Gmail for Luo Kai...")
        from core.gmail_creator import create_gmail
        email, password = create_gmail()
        print(f"\n✅ Email: {email}\n🔑 Password: {password}\n")

    elif user_input.lower().startswith("send email "):
        parts = user_input[11:].split("|")
        if len(parts) >= 3:
            from core.gmail_creator import send_email
            send_email(parts[0].strip(), parts[1].strip(), parts[2].strip())
        else:
            print("Usage: send email to@email.com | Subject | Body")

    elif user_input.lower() == "read emails":
        from core.gmail_creator import read_emails
        emails = read_emails()
        for e in emails:
            print(f"\n📧 From: {e['from']}\nSubject: {e['subject']}\n{e['body'][:200]}")
        print()

    elif user_input.lower() == "files":
        print("\n📂 Files:")
        print(list_files())
        print()

    elif user_input.lower().startswith("read "):
        filename = user_input[5:].strip()
        print(read_file(f"workspace/{filename}"))

    elif user_input.lower().startswith("do "):
        goal = user_input[3:].strip()
        print(f"\n🤖 Browser Agent executing: {goal}")
        from core.auto_browser import browser_agent
        browser_agent(goal, headless=False)
        print()

    else:
        response = think(user_input)
        print(f"\n🐉 Agent: {response}\n")
        print("-" * 50)
