# 🐉 LUO KAI — LONG TERM MEMORY SYSTEM
# Remembers EVERYTHING forever, learns patterns, gets smarter over time

import json
import os
from datetime import datetime

MEMORY_DB = "memory/long_memory.json"

def load_db():
    try:
        with open(MEMORY_DB, "r") as f:
            return json.load(f)
    except:
        return {
            "facts": [],
            "wins": [],
            "failures": [],
            "patterns": [],
            "skills_learned": [],
            "people": {},
            "topics": {},
            "total_tasks": 0
        }

def save_db(db):
    os.makedirs("memory", exist_ok=True)
    with open(MEMORY_DB, "w") as f:
        json.dump(db, f, indent=2)

def remember(task, result, task_type, success=True):
    """Save any task to long term memory"""
    db = load_db()
    entry = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "task": task[:200],
        "result_summary": result[:300],
        "type": task_type,
        "success": success
    }
    if success:
        db["wins"].append(entry)
        if len(db["wins"]) > 500:
            db["wins"] = db["wins"][-500:]
    else:
        db["failures"].append(entry)
        if len(db["failures"]) > 100:
            db["failures"] = db["failures"][-100:]

    # Track topics
    words = task.lower().split()
    for word in words:
        if len(word) > 4:
            db["topics"][word] = db["topics"].get(word, 0) + 1

    db["total_tasks"] += 1
    save_db(db)

def recall(query, limit=5):
    """Find relevant memories for current task"""
    db = load_db()
    query_words = set(query.lower().split())
    scored = []
    for win in db["wins"]:
        task_words = set(win["task"].lower().split())
        score = len(query_words & task_words)
        if score > 0:
            scored.append((score, win))
    scored.sort(reverse=True)
    return [w for _, w in scored[:limit]]

def learn_pattern(pattern, outcome):
    """Save a learned pattern"""
    db = load_db()
    db["patterns"].append({
        "date": datetime.now().strftime("%Y-%m-%d"),
        "pattern": pattern,
        "outcome": outcome
    })
    if len(db["patterns"]) > 200:
        db["patterns"] = db["patterns"][-200:]
    save_db(db)

def get_stats():
    """Get memory statistics"""
    db = load_db()
    top_topics = sorted(db["topics"].items(), key=lambda x: x[1], reverse=True)[:10]
    return {
        "total_tasks": db["total_tasks"],
        "wins": len(db["wins"]),
        "failures": len(db["failures"]),
        "patterns": len(db["patterns"]),
        "top_topics": top_topics
    }

def get_relevant_context(task):
    """Get relevant past experience for current task"""
    memories = recall(task, limit=3)
    if not memories:
        return ""
    context = "RELEVANT PAST EXPERIENCE:\n"
    for m in memories:
        context += f"- [{m['date']}] Did: {m['task'][:100]} → {m['result_summary'][:150]}\n"
    return context

print("🧠 Long Term Memory loaded!")
