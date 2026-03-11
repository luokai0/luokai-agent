from core.brain import think
from core.files import list_files, read_file
from core.moltbook import status, post, feed, auto_post, communities, heartbeat
from core.temp_email import create_temp_email, get_verification_code, signup_with_temp_email
from core.gmail_creator import send_email, read_emails
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

TEMP_EMAIL = None
TEMP_SID = None

print("=" * 50)
print("🐉 LUO KAI AGENT — Online")
print(f"🛠️  {len(ALL_SKILLS)} Skills Loaded")
print("=" * 50)
print("Commands:")
print("  'skills'                      → list all skills")
print("  'forge <name>'                → forge a new skill")
print("  'evolve'                      → agent forges its own skill")
print("  'files'                       → list saved files")
print("  'read <name>'                 → read a file")
print("  'temp email'                  → create free temp email")
print("  'check inbox'                 → check temp email inbox")
print("  'send email to|subject|body'  → send email")
print("  'read emails'                 → read inbox")
print("  'signup url|sitename'         → signup to a site")
print("  'mb status'                   → Moltbook status")
print("  'mb feed'                     → read Moltbook feed")
print("  'mb post <topic>'             → auto post to Moltbook")
print("  'mb communities'              → list communities")
print("  'mb heartbeat'                → check notifications")
print("  'quit'                        → exit")
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

    elif user_input.lower() == "temp email":
        TEMP_EMAIL, TEMP_SID = create_temp_email()
        print(f"\n📧 Your temp email: {TEMP_EMAIL}")
        print(f"Use 'check inbox' to see emails!\n")

    elif user_input.lower() == "check inbox":
        if not TEMP_SID:
            print("⚠️ No temp email created yet! Type 'temp email' first.")
        else:
            from core.temp_email import check_inbox
            emails = check_inbox(TEMP_SID, timeout=10)
            if emails:
                for e in emails:
                    print(f"\n📧 From: {e.get('mail_from')}")
                    print(f"   Subject: {e.get('mail_subject')}")
            else:
                print("📭 Inbox empty")
        print()

    elif user_input.lower().startswith("send email "):
        parts = user_input[11:].split("|")
        if len(parts) >= 3:
            to = parts[0].strip()
            subject = parts[1].strip()
            body = parts[2].strip()
            print(f"\n📧 Sending email to {to}...")
            result = send_email(to, subject, body)
            if result:
                print("✅ Email sent!")
            else:
                print("⚠️ Failed — make sure LUOKAI_EMAIL is set in .env")
        else:
            print("Usage: send email to@email.com | Subject | Body")
        print()

    elif user_input.lower() == "read emails":
        print("\n📬 Reading inbox...")
        emails = read_emails()
        if isinstance(emails, list):
            for e in emails:
                print(f"\n📧 From: {e['from']}\nSubject: {e['subject']}\n{e['body'][:200]}")
        else:
            print(emails)
        print()

    elif user_input.lower().startswith("signup "):
        parts = user_input[7:].split("|")
        if len(parts) >= 2:
            from core.web_signup import signup_to_site
            signup_to_site(parts[0].strip(), parts[1].strip())
        else:
            print("Usage: signup https://site.com | sitename")
        print()
        continue
        parts = user_input[7:].split("|")
        if len(parts) >= 2:
            url = parts[0].strip()
            name = parts[1].strip()
            print(f"\n🤖 Signing up to {name}...")

    elif user_input.lower() == "money sites":
        from core.money_sites import print_money_sites
        print_money_sites()
        print()

    elif user_input.lower().startswith("signup all"):
        parts = user_input.split(" ")
        limit = int(parts[2]) if len(parts) > 2 else 5
        from core.money_sites import signup_all
        signup_all(limit)
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

    elif user_input.lower() == "files":
        print("\n📂 Files:")
        print(list_files())
        print()

    elif user_input.lower().startswith("read "):
        filename = user_input[5:].strip()
        print(read_file(f"workspace/{filename}"))

    else:
        response = think(user_input)
        print(f"\n🐉 Agent: {response}\n")
        print("-" * 50)
