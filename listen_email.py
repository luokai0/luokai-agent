# Run this to start email commander
# You need Gmail App Password OR we use polling via browser

import time
from core.email_sender import send_email
from core.router import ask
from core.search import search

print("🐉 LUO KAI EMAIL COMMANDER")
print("=" * 40)
print("To command Luo Kai, type a task here")
print("In future: email commands will work automatically!")
print("=" * 40)

# For now — manual email command simulation
while True:
    task = input("\n📧 Simulate email command (or 'quit'): ").strip()
    if task.lower() == 'quit':
        break
    
    needs_search = any(w in task.lower() for w in ['search','find','latest','news','price','what','who'])
    context = search(task) if needs_search else ""
    
    prompt = f"""You are Luo Kai Agent. Task from email: {task}
{f'Research: {context}' if context else ''}
Give a complete, actionable response. Sign as Luo Kai Agent."""
    
    result = ask(prompt)
    print(f"\n🐉 Response:\n{result}")
    
    # Email the result back
    send_email(
        'creationslous@gmail.com',
        f'✅ Task Complete: {task[:50]}',
        result
    )
    print("\n📧 Result emailed to you!")
