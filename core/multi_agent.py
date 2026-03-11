# 🐉 LUO KAI — MULTI AGENT MODE
# Runs 5 Luo Kais simultaneously on different tasks

import threading
import time
import json
from datetime import datetime
from core.router import ask
from core.search import search
from core.files import write_file
from core.long_memory import remember, get_relevant_context

def run_single_agent(agent_id, task, results, errors):
    """One agent working on one task"""
    try:
        print(f"  🐉 Agent {agent_id} starting: {task[:50]}...")
        
        # Get relevant memory
        context = get_relevant_context(task)
        
        # Check if needs search
        needs_web = any(w in task.lower() for w in 
            ["latest", "today", "current", "price", "news", "find", "search", "trending"])
        
        search_data = ""
        if needs_web:
            search_data = search(task[:80])
        
        prompt = f"""You are Luo Kai Agent #{agent_id} — one of 5 parallel agents working simultaneously.
Your specific task: {task}

{context}
{f'Live data: {search_data[:1000]}' if search_data else ''}

Execute this task completely and brilliantly.
Be specific and deliver maximum value."""

        result = ask(prompt)
        results[agent_id] = {"task": task, "result": result, "status": "✅ done"}
        remember(task, result, "multi_agent", success=True)
        
        # Save result
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        write_file(f"agent{agent_id}_{ts}.txt", f"Agent {agent_id} Task: {task}\n\nResult:\n{result}")
        print(f"  ✅ Agent {agent_id} done!")
        
    except Exception as e:
        results[agent_id] = {"task": task, "result": str(e), "status": "⚠️ failed"}
        errors[agent_id] = str(e)
        print(f"  ⚠️ Agent {agent_id} failed: {e}")

def run_multi_agent(tasks):
    """Run multiple tasks in parallel with separate agents"""
    if len(tasks) > 5:
        tasks = tasks[:5]
    
    print(f"\n🚀 MULTI-AGENT MODE — {len(tasks)} agents launching simultaneously!")
    print("=" * 50)
    
    results = {}
    errors = {}
    threads = []
    
    start_time = time.time()
    
    # Launch all agents at once
    for i, task in enumerate(tasks, 1):
        t = threading.Thread(
            target=run_single_agent,
            args=(i, task, results, errors)
        )
        t.daemon = True
        threads.append(t)
    
    # Start all simultaneously
    for t in threads:
        t.start()
        time.sleep(2)  # 2 second gap to avoid rate limits
    
    # Wait for all to finish
    for t in threads:
        t.join(timeout=120)
    
    elapsed = time.time() - start_time
    
    # Print summary
    print(f"\n{'='*50}")
    print(f"🐉 MULTI-AGENT COMPLETE — {elapsed:.0f}s")
    print(f"{'='*50}")
    for agent_id, res in results.items():
        print(f"\n{res['status']} Agent {agent_id}: {res['task'][:60]}")
        print(f"   Result preview: {res['result'][:150]}...")
    
    return results

def auto_decompose_and_run(big_goal):
    """Give one big goal — agent breaks it into 5 subtasks and runs them all"""
    from core.router import ask
    
    print(f"\n🎯 Auto-decomposing goal: {big_goal}")
    
    # Break into subtasks
    decompose_prompt = f"""Break this goal into exactly 5 parallel subtasks that can be worked on simultaneously:
Goal: {big_goal}

Return ONLY a JSON array of 5 task strings:
["task1", "task2", "task3", "task4", "task5"]

Make each task specific and independently executable."""

    response = ask(decompose_prompt, max_tokens=512)
    
    try:
        if "```" in response:
            response = response.split("```")[1].replace("json","").strip()
        tasks = json.loads(response.strip())
        print(f"📋 Decomposed into {len(tasks)} subtasks:")
        for i, t in enumerate(tasks, 1):
            print(f"  {i}. {t}")
    except:
        # Fallback tasks
        tasks = [
            f"Research the best approach for: {big_goal}",
            f"Find market opportunities related to: {big_goal}",
            f"Create an action plan for: {big_goal}",
            f"Identify obstacles and solutions for: {big_goal}",
            f"Build a monetization strategy for: {big_goal}"
        ]
    
    return run_multi_agent(tasks)

print("🤖 Multi-Agent Mode loaded — 5 Luo Kais ready!")
