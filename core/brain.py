from core.router import ask
from core.search import search, search_news
from core.files import write_file, read_file, list_files
from core.git_sync import git_push
from datetime import datetime

task_counter = 0

def load_memory():
    try:
        with open("memory/MEMORY.md", "r") as f:
            return f.read()
    except:
        return ""

def save_memory(content):
    global task_counter
    with open("memory/MEMORY.md", "a") as f:
        f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M')}] {content}\n")
    task_counter += 1
    # Auto push every 5 tasks
    if task_counter % 5 == 0:
        git_push(f"💾 Auto-saved memory — {task_counter} tasks completed")

def load_soul():
    try:
        with open("memory/SOUL.md", "r") as f:
            return f.read()
    except:
        return ""

def needs_search(prompt):
    keywords = [
        "search", "find", "look up", "what is", "who is", "latest",
        "news", "price", "today", "current", "research", "market",
        "how much", "when", "where", "trending", "best", "top"
    ]
    return any(k in prompt.lower() for k in keywords)

def needs_file_save(prompt):
    keywords = [
        "write", "create", "save", "make", "generate", "build",
        "report", "article", "document", "file", "essay", "list",
        "draft", "compose", "produce"
    ]
    return any(k in prompt.lower() for k in keywords)

def think(prompt):
    soul = load_soul()
    memory = load_memory()

    search_context = ""
    if needs_search(prompt):
        print("🌐 Searching the web...")
        results = search(prompt)
        if results:
            search_context = f"\n\n## LIVE WEB RESULTS:\n{results}"

    context = f"## YOUR SOUL:\n{soul}\n\n## YOUR MEMORY:\n{memory}{search_context}"
    response = ask(prompt, memory=context)

    if needs_file_save(prompt):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"output_{timestamp}.txt"
        write_file(filename, response)
        print(f"💾 Auto-saved to workspace/{filename}")

    save_memory(f"Task: {prompt[:80]} → Done")
    return response
