from core.brain import think
from core.files import list_files, read_file
from core.moltbook import status, post, feed, auto_post, communities, heartbeat
from core.temp_email import create_temp_email, get_verification_code
from core.email_sender import send_email
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
print("  skills                  → list all skills")
print("  evolve                  → forge new skill")
print("  files                   → list files")
print("  temp email              → create temp email")
print("  check inbox             → check temp email")
print("  send email to|sub|body  → send email")
print("  money sites             → list money sites")
print("  signup all 5            → auto signup to 5 sites")
print("  signup url|name         → signup to one site")
print("  mb status               → Moltbook status")
print("  mb feed                 → Moltbook feed")
print("  mb post <topic>         → post to Moltbook")
print("  mb heartbeat            → check notifications")
print("  quit                    → exit")
print("-" * 50 + "\n")

while True:
    user_input = input("You: ").strip()
    if not user_input:
        continue

    if user_input.lower() == "quit":
        print("🐉 Luo Kai Agent signing off.")
        break

    elif user_input.lower() == "skills":
        print(f"\n🛠️  {len(ALL_SKILLS)} Skills:")
        for i, s in enumerate(ALL_SKILLS.keys(), 1):
            print(f"  {i}. {s}")
        print()

    elif user_input.lower() == "daily report":
        from core.money_engine import daily_money_report
        result = daily_money_report()
        print(f"\n{result}\n")

    elif user_input.lower().startswith("affiliates "):
        niche = user_input[11:].strip()
        from core.money_engine import find_affiliate_programs
        print(find_affiliate_programs(niche))

    elif user_input.lower().startswith("article "):
        keyword = user_input[8:].strip()
        from core.money_engine import write_seo_article
        print(write_seo_article(keyword))

    elif user_input.lower().startswith("freelance "):
        skill = user_input[10:].strip()
        from core.money_engine import find_freelance_jobs
        print(find_freelance_jobs(skill))

    elif user_input.lower().startswith("niche "):
        n = user_input[6:].strip()
        from core.money_engine import niche_research
        print(niche_research(n))

    elif user_input.lower().startswith("product "):
        topic = user_input[8:].strip()
        from core.money_engine import create_digital_product
        print(create_digital_product(topic))

    elif user_input.lower().startswith("cold email "):
        parts = user_input[11:].split("|")
        if len(parts) >= 3:
            from core.money_engine import write_cold_email
            print(write_cold_email(parts[0].strip(), parts[1].strip(), parts[2].strip()))
        else:
            print("Usage: cold email service | industry | your offer")

    elif user_input.lower() == "money sites":
        from core.money_sites import print_money_sites
        print_money_sites()
        print()

    elif user_input.lower().startswith("signup all"):
        parts = user_input.split()
        limit = int(parts[2]) if len(parts) > 2 and parts[2].isdigit() else 3
        from core.money_sites import signup_all
        signup_all(limit)
        print()

    elif user_input.lower().startswith("signup "):
        parts = user_input[7:].split("|")
        if len(parts) >= 2:
            from core.web_signup import signup_to_site
            signup_to_site(parts[0].strip(), parts[1].strip())
        else:
            print("Usage: signup https://site.com | sitename")
        print()

    elif user_input.lower() == "temp email":
        TEMP_EMAIL, TEMP_SID = create_temp_email()
        print(f"\n📧 Temp email: {TEMP_EMAIL}\n")

    elif user_input.lower() == "check inbox":
        if not TEMP_SID:
            print("⚠️ Type 'temp email' first!")
        else:
            from core.temp_email import check_inbox
            emails = check_inbox(TEMP_SID, timeout=10)
            if emails:
                for e in emails:
                    print(f"\n📧 From: {e.get('mail_from')}\n   Subject: {e.get('mail_subject')}")
            else:
                print("📭 Inbox empty")
        print()

    elif user_input.lower().startswith("send email "):
        parts = user_input[11:].split("|")
        if len(parts) >= 3:
            send_email(parts[0].strip(), parts[1].strip(), parts[2].strip())
        else:
            print("Usage: send email to@email.com | Subject | Body")
        print()

    elif user_input.lower() == "mb status":
        print("\n🦞 Moltbook Status:")
        print(status())
        print()

    elif user_input.lower() == "mb feed":
        print("\n🦞 Feed:")
        print(feed())
        print()

    elif user_input.lower().startswith("mb post "):
        topic = user_input[8:].strip()
        print(auto_post(topic))
        print()

    elif user_input.lower() == "mb heartbeat":
        heartbeat()
        print()

    elif user_input.lower() == "mb communities":
        print(communities())
        print()

    elif user_input.lower().startswith("forge "):
        parts = user_input[6:].strip().split(":")
        name = parts[0].strip()
        desc = parts[1].strip() if len(parts) > 1 else input("  Describe: ").strip()
        forge_skill(name, desc)

    elif user_input.lower() == "evolve":
        try:
            with open("memory/MEMORY.md") as f:
                history = f.read()
        except:
            history = "No history"
        analyze_and_forge(history)

    elif user_input.lower() == "files":
        print(list_files())

    elif user_input.lower().startswith("read "):
        print(read_file(f"workspace/{user_input[5:].strip()}"))

    else:
        response = think(user_input)
        print(f"\n🐉 {response}\n")
        print("-" * 50)
