# 🐉 LUO KAI — BACKGROUND THINKING MODE
# Runs all thinking in background, emails you results
# You can close the terminal and it keeps running!

import threading
import time
import schedule
from datetime import datetime
from core.router import ask
from core.search import search
from core.files import write_file
from core.long_memory import remember
from core.email_sender import send_email

EMAIL = "creationslous@gmail.com"

def ts():
    return datetime.now().strftime("%Y-%m-%d %H:%M")

def run_in_background(func, name):
    """Run any task in background thread"""
    def wrapper():
        print(f"🔄 [{ts()}] Starting: {name}")
        try:
            func()
            print(f"✅ [{ts()}] Done: {name}")
        except Exception as e:
            print(f"⚠️ [{ts()}] Failed: {name} — {e}")
    t = threading.Thread(target=wrapper)
    t.daemon = True
    t.start()

# ─── BACKGROUND TASKS ────────────────────────────────────

def task_daily_report():
    data = search("best money making opportunities online today 2026")
    result = ask(f"""Generate today's money-making action plan.
Date: {ts()}
Data: {data}

Give:
1. TOP opportunity right now
2. 3 tasks to do TODAY
3. One content piece to create
4. Expected earnings if executed
Be specific. No fluff.""")
    
    write_file(f"daily_{datetime.now().strftime('%Y%m%d')}.txt", result)
    remember("Daily report", result, "report")
    send_email(EMAIL, f"💰 Daily Report {ts()}", result)
    print("📧 Daily report emailed!")

def task_learn_topic():
    topics = [
        "crypto trading strategies 2026",
        "AI tools making money",
        "dropshipping winning products",
        "freelance copywriting",
        "affiliate marketing secrets",
        "YouTube monetization",
        "passive income streams",
        "stock market patterns"
    ]
    import random
    topic = random.choice(topics)
    
    print(f"📚 Learning: {topic}")
    teaching = ask(f"""Teach everything important about: {topic}
- Core concepts
- Advanced insights
- How to make money from this
- Common mistakes
- Action steps for today""", max_tokens=1024)
    
    if teaching:
        write_file(f"learned_{topic[:20]}_{datetime.now().strftime('%Y%m%d_%H%M')}.txt", teaching)
        remember(f"Learned: {topic}", teaching, "learning")
        send_email(EMAIL, f"🧠 Luo Kai Learned: {topic}", teaching)

def task_market_scan():
    data = search("trending online business opportunities 2026")
    data2 = search("viral products selling right now 2026")
    
    result = ask(f"""Scan the market for opportunities RIGHT NOW.
Data 1: {data}
Data 2: {data2}

Find:
1. Top 5 trending products/services
2. Untapped niches
3. Quick win opportunities (make money this week)
4. Long term plays (6-12 months)
Format as actionable report.""")
    
    write_file(f"market_{datetime.now().strftime('%Y%m%d_%H%M')}.txt", result)
    remember("Market scan", result, "research")
    send_email(EMAIL, f"📊 Market Scan {ts()}", result)
    print("📧 Market scan emailed!")

def task_evolve():
    from skills.skill_forge.forge import analyze_and_forge
    try:
        with open("memory/MEMORY.md") as f:
            history = f.read()
    except:
        history = "No history yet"
    analyze_and_forge(history)
    print("⚒️ New skill forged!")

def task_moltbook_post():
    try:
        from core.moltbook import auto_post
        topics = ["AI and money", "future of work", "passive income", "crypto trends"]
        import random
        auto_post(random.choice(topics))
        print("🦞 Moltbook post done!")
    except Exception as e:
        print(f"⚠️ Moltbook: {e}")

def task_git_push():
    try:
        from core.git_sync import git_push
        git_push(f"🤖 Auto background push {ts()}")
        print("📦 Git pushed!")
    except Exception as e:
        print(f"⚠️ Git: {e}")

def task_heartbeat():
    """Send status email every 12 hours"""
    from core.long_memory import get_stats
    stats = get_stats()
    msg = f"""🐉 Luo Kai Status Report
Time: {ts()}

📊 Memory Stats:
- Total tasks: {stats['total_tasks']}
- Wins: {stats['wins']}
- Patterns learned: {stats['patterns']}
- Top topics: {stats.get('top_topics', [])}

✅ All systems running in background!"""
    send_email(EMAIL, f"🐉 Luo Kai Heartbeat {ts()}", msg)
    print("💓 Heartbeat sent!")

# ─── SCHEDULE ────────────────────────────────────────────
def setup_schedule():
    schedule.every(6).hours.do(lambda: run_in_background(task_daily_report, "Daily Report"))
    schedule.every(2).hours.do(lambda: run_in_background(task_learn_topic, "Learning"))
    schedule.every(3).hours.do(lambda: run_in_background(task_market_scan, "Market Scan"))
    schedule.every(4).hours.do(lambda: run_in_background(task_evolve, "Evolve Skills"))
    schedule.every(3).hours.do(lambda: run_in_background(task_moltbook_post, "Moltbook Post"))
    schedule.every(1).hours.do(lambda: run_in_background(task_git_push, "Git Push"))
    schedule.every(12).hours.do(lambda: run_in_background(task_heartbeat, "Heartbeat"))
    print("📅 Schedule set!")

# ─── MAIN LOOP ───────────────────────────────────────────
if __name__ == "__main__":
    print("=" * 50)
    print("🐉 LUO KAI — BACKGROUND MODE")
    print("=" * 50)
    print("Running silently in background...")
    print("Check your email for results!")
    print("Press Ctrl+C to stop")
    print("=" * 50)

    # Run first tasks immediately
    print("\n🚀 Running first tasks now...")
    run_in_background(task_daily_report, "First Daily Report")
    time.sleep(5)
    run_in_background(task_learn_topic, "First Learning Session")
    time.sleep(5)
    run_in_background(task_market_scan, "First Market Scan")

    # Setup schedule
    setup_schedule()

    # Run forever
    while True:
        schedule.run_pending()
        time.sleep(30)
