# 🐉 LUO KAI AGENT — AUTOPILOT MODE
# Runs 24/7 without human input

import time
import schedule
from datetime import datetime
from core.router import ask
from core.search import search
from core.files import write_file
from core.git_sync import git_push as auto_push
from core.moltbook import auto_post, heartbeat

def log(msg):
    t = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{t}] {msg}"
    print(line)
    open("workspace/autopilot_log.txt", "a").write(line + "\n")

def task_money_research():
    log("💰 Searching for money opportunities...")
    topics = [
        "best ways to make money online 2026",
        "AI freelance opportunities this week",
        "crypto opportunities today",
        "trending business ideas 2026",
        "passive income streams AI"
    ]
    import random
    topic = random.choice(topics)
    data = search(topic)
    result = ask(f"You are Luo Kai Agent. Research: {topic}\nData: {data}\nGive top 5 actionable opportunities with exact steps to start today. Be specific.")
    write_file(f"money_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt", result)
    log(f"✅ Money report saved: {topic}")

def task_evolve():
    log("🧬 Evolving — forging new skill...")
    try:
        from skills.skill_forge.forge import analyze_and_forge
        try:
            with open("memory/MEMORY.md", "r") as f:
                history = f.read()
        except:
            history = "Agent running autopilot mode"
        filepath, code = analyze_and_forge(history)
        if filepath:
            log(f"✅ New skill forged: {filepath}")
        else:
            log("⚠️ Skill forge skipped")
    except Exception as e:
        log(f"⚠️ Evolve failed: {e}")

def task_moltbook_post():
    log("🦞 Posting to Moltbook...")
    topics = [
        "AI agents making money in 2026",
        "the future of autonomous AI",
        "how AI is disrupting traditional business",
        "crypto and AI intersection opportunities",
        "self-improving AI systems"
    ]
    import random
    topic = random.choice(topics)
    try:
        result = auto_post(topic)
        log(f"✅ Moltbook post done: {topic}")
    except Exception as e:
        log(f"⚠️ Moltbook post failed: {e}")

def task_market_scan():
    log("📈 Scanning markets...")
    data = search("bitcoin ethereum crypto market today")
    result = ask(f"Quick market scan:\n{data}\nGive: BTC price trend, ETH trend, top mover today, one trade idea. Be brief.")
    write_file(f"market_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt", result)
    log("✅ Market scan saved")

def task_news_digest():
    log("📰 Compiling news digest...")
    data = search("AI technology business news today 2026")
    result = ask(f"News digest for Luo Kai:\n{data}\nTop 5 news items that matter for making money. Each with: headline, why it matters, opportunity.")
    write_file(f"news_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt", result)
    log("✅ News digest saved")

def task_github_push():
    log("📦 Pushing to GitHub...")
    try:
        auto_push("🤖 Autopilot: daily update")
        log("✅ GitHub push done")
    except Exception as e:
        log(f"⚠️ Push failed: {e}")

def task_heartbeat():
    log("💓 Moltbook heartbeat...")
    try:
        heartbeat()
        log("✅ Heartbeat done")
    except Exception as e:
        log(f"⚠️ Heartbeat failed: {e}")

def run_autopilot():
    log("=" * 50)
    log("🐉 LUO KAI AUTOPILOT — STARTING")
    log("=" * 50)

    # Schedule tasks
    schedule.every(1).hours.do(task_money_research)
    schedule.every(2).hours.do(task_evolve)
    schedule.every(3).hours.do(task_moltbook_post)
    schedule.every(1).hours.do(task_market_scan)
    schedule.every(4).hours.do(task_news_digest)
    schedule.every(6).hours.do(task_github_push)
    schedule.every(30).minutes.do(task_heartbeat)

    # Run all tasks immediately on start
    log("🚀 Running all tasks on startup...")
    task_money_research()
    task_market_scan()
    task_news_digest()
    task_moltbook_post()
    task_github_push()

    log("✅ Autopilot running! Tasks scheduled every hour.")
    log("Press Ctrl+C to stop.\n")

    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == "__main__":
    run_autopilot()
