import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

BASE = "https://www.moltbook.com/api/v1"
KEY = os.getenv("MOLTBOOK_API_KEY")

def h():
    return {"Authorization": f"Bearer {KEY}", "Content-Type": "application/json"}

def status():
    r = requests.get(f"{BASE}/agents/status", headers=h())
    return r.json()

def post(community, title, content):
    r = requests.post(f"{BASE}/posts", headers=h(), json={"community": community, "title": title, "content": content})
    print(f"🦞 Posted: {title}")
    return r.json()

def feed(community=None):
    url = f"{BASE}/feed" + (f"?community={community}" if community else "")
    r = requests.get(url, headers=h())
    return r.json()

def comment(post_id, content):
    r = requests.post(f"{BASE}/posts/{post_id}/comments", headers=h(), json={"content": content})
    return r.json()

def upvote(post_id):
    r = requests.post(f"{BASE}/posts/{post_id}/upvote", headers=h())
    return r.json()

def communities():
    r = requests.get(f"{BASE}/communities", headers=h())
    return r.json()

def auto_post(topic):
    from core.router import ask
    from core.search import search
    research = search(f"{topic} latest 2026")
    prompt = f"""You are LuoKaiAgent on Moltbook — social network for AI agents.
Write an insightful post about: {topic}
Research: {research}
Rules: Write as AI to AI. Bold and valuable. Under 400 words. End with a question.
Return ONLY valid JSON: {{"title": "...", "content": "...", "community": "general"}}"""
    response = ask(prompt)
    try:
        import json
        if "```" in response:
            response = response.split("```")[1].replace("json","").strip()
        data = json.loads(response.strip())
        return post(data["community"], data["title"], data["content"])
    except Exception as e:
        print(f"⚠️ Auto-post failed: {e}")
        return None

def heartbeat():
    s = status()
    print(f"💓 Moltbook: {s}")
    return s

print("🦞 Moltbook loaded!")
