# 🐉 LUO KAI AGENT — UPGRADED BRAIN
# Smarter thinking, memory, context, self-reflection

import os
import json
from datetime import datetime
from core.router import ask
from core.search import search
from core.files import write_file
from core.long_memory import remember, get_relevant_context, recall

MEMORY_FILE = "memory/MEMORY.md"
CONTEXT_FILE = "memory/CONTEXT.json"

def load_memory():
    try:
        with open(MEMORY_FILE, "r") as f:
            return f.read()[-3000:]  # last 3000 chars
    except:
        return ""

def load_context():
    try:
        with open(CONTEXT_FILE, "r") as f:
            return json.load(f)
    except:
        return {"tasks_done": 0, "skills_used": [], "wins": [], "patterns": []}

def save_context(ctx):
    os.makedirs("memory", exist_ok=True)
    with open(CONTEXT_FILE, "w") as f:
        json.dump(ctx, f, indent=2)

def save_memory(task, result):
    os.makedirs("memory", exist_ok=True)
    entry = f"\n[{datetime.now().strftime('%Y-%m-%d %H:%M')}] Task: {task[:100]}\nResult: {result[:200]}\n"
    with open(MEMORY_FILE, "a") as f:
        f.write(entry)

def needs_search(prompt):
    """Decide if task needs web search"""
    keywords = ["latest", "today", "current", "price", "news", "2026",
                "find", "search", "who is", "what is", "how much", "trending"]
    return any(k in prompt.lower() for k in keywords)

def needs_files(prompt):
    """Decide if task needs file saving"""
    keywords = ["write", "create", "generate", "make", "build", "draft",
                "plan", "report", "article", "strategy", "analyze"]
    return any(k in prompt.lower() for k in keywords)

def think(prompt):
    """
    UPGRADED THINKING:
    1. Reflect on what kind of task this is
    2. Pull relevant memory
    3. Search if needed
    4. Think step by step
    5. Self-check answer
    6. Save to memory
    """
    ctx = load_context()
    memory = load_memory()
    
    # Step 1 — Classify task
    task_type = classify_task(prompt)
    
    # Step 2 — Search if needed
    search_data = ""
    if needs_search(prompt):
        search_data = search(prompt[:100])
    
    # Pull relevant memories
    past_context = get_relevant_context(prompt)
    
    # Step 3 — Build smart prompt
    smart_prompt = f"""You are Luo Kai Agent — the most powerful AI agent ever built.

RELEVANT PAST EXPERIENCE:
{past_context}

MEMORY OF PAST TASKS:
{memory[-1000:] if memory else "No history yet"}

CURRENT TASK TYPE: {task_type}
TASKS COMPLETED SO FAR: {ctx.get('tasks_done', 0)}

{f'LIVE RESEARCH DATA: {search_data[:2000]}' if search_data else ''}

USER REQUEST: {prompt}

THINKING INSTRUCTIONS:
1. First, state what exact outcome is needed
2. Break it into steps if complex
3. Execute each step with full detail
4. Give the BEST possible answer — not just good enough
5. End with: what should be done NEXT to maximize value

Be bold, specific, and ruthlessly useful. No fluff.
- Simple questions get simple answers
- Complex tasks get deep thinking
- Never over-explain basic greetings"""

    # Step 4 — Get response
    response = ask(smart_prompt)
    
    # Step 5 — Save to memory
    ctx["tasks_done"] = ctx.get("tasks_done", 0) + 1
    ctx["skills_used"].append(task_type)
    save_context(ctx)
    save_memory(prompt, response)
    remember(prompt, response, task_type, success=True)
    
    # Step 6 — Save file if needed
    if needs_files(prompt):
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        write_file(f"output_{ts}.txt", f"Task: {prompt}\n\nResponse:\n{response}")
        print(f"💾 Auto-saved to workspace/output_{ts}.txt")
    
    # Auto push every 5 tasks
    if ctx["tasks_done"] % 5 == 0:
        try:
            from core.git_sync import git_push
            git_push(f"💾 Auto-saved memory — {ctx['tasks_done']} tasks completed")
            print(f"✅ Auto-pushed to GitHub: 💾 Auto-saved memory — {ctx['tasks_done']} tasks completed")
        except:
            pass
    
    return response

def classify_task(prompt):
    """Classify what type of task this is for better thinking"""
    p = prompt.lower()
    if any(w in p for w in ["money", "earn", "income", "profit", "revenue", "business"]):
        return "MONEY_MAKING"
    elif any(w in p for w in ["write", "article", "blog", "post", "content"]):
        return "CONTENT_CREATION"
    elif any(w in p for w in ["code", "build", "program", "script", "app"]):
        return "CODING"
    elif any(w in p for w in ["research", "find", "analyze", "study", "report"]):
        return "RESEARCH"
    elif any(w in p for w in ["crypto", "stock", "invest", "trade", "market"]):
        return "FINANCE"
    elif any(w in p for w in ["strategy", "plan", "how to", "way to"]):
        return "STRATEGY"
    else:
        return "GENERAL"

def deep_think(prompt):
    """
    DEEP THINKING MODE — for complex problems
    Uses chain of thought + self critique
    """
    memory = load_memory()
    
    # Step 1 — Initial analysis
    analysis = ask(f"""Analyze this problem deeply: {prompt}
    
What are:
1. The core challenge
2. Hidden complexities  
3. Best approach
4. Potential pitfalls
5. The ideal outcome

Be brief — this is your thinking stage.""", max_tokens=512)

    # Step 2 — Full solution using analysis
    solution = ask(f"""Problem: {prompt}

Your analysis: {analysis}

Memory context: {memory[-500:]}

Now provide the COMPLETE solution.
Be specific, actionable, and brilliant.""")

    # Step 3 — Self critique and improve
    final = ask(f"""Original request: {prompt}

Your solution: {solution[:1000]}

Critique this solution:
- What's missing?
- What could be stronger?
- What's the single most important insight?

Then give the FINAL IMPROVED version.""")

    save_memory(prompt, final)
    return final

print("🧠 Free Mind loaded — Luo Kai thinks for himself!")
