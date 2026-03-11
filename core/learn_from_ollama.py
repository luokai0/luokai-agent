# 🐉 LUO KAI — LEARNS FROM OLLAMA
# Luo Kai and Ollama have a deep conversation
# Luo Kai saves everything he learns forever

import requests
import time
from core.router import ask_groq
from core.long_memory import remember, learn_pattern
from core.files import write_file
from datetime import datetime

def ollama_think(prompt):
    """Get Ollama's thoughts"""
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3.2",
                "prompt": prompt,
                "stream": False,
                "options": {"num_predict": 1024}
            },
            timeout=120
        )
        if response.status_code == 200:
            return response.json().get("response", "")
    except Exception as e:
        return f"Ollama error: {e}"
    return ""

def learn_from_ollama(topic, rounds=5):
    """
    Luo Kai and Ollama have a conversation about a topic
    Both learn from each other
    Everything saved to long term memory
    """
    print(f"\n🧠 LUO KAI LEARNING SESSION")
    print(f"📚 Topic: {topic}")
    print(f"🔄 Rounds: {rounds}")
    print("=" * 50)

    conversation = []
    full_log = f"LEARNING SESSION — {datetime.now().strftime('%Y-%m-%d %H:%M')}\nTopic: {topic}\n\n"

    # Round 1 — Ollama shares what it knows
    print(f"\n🖥️  Round 1: Ollama teaches...")
    ollama_response = ollama_think(f"""You are a wise teacher. 
Teach everything you know about: {topic}
Be detailed, specific, and include:
- Core concepts
- Advanced insights  
- Practical applications
- Common mistakes to avoid
- Hidden knowledge most people miss""")

    print(f"🖥️  Ollama: {ollama_response[:200]}...")
    conversation.append({"speaker": "Ollama", "text": ollama_response})
    full_log += f"OLLAMA TEACHES:\n{ollama_response}\n\n"

    # Save first lesson to memory
    remember(f"Ollama taught about {topic}", ollama_response, "learning", success=True)

    # Rounds 2-N — Luo Kai asks questions, Ollama answers
    for round_num in range(2, rounds + 1):
        time.sleep(2)  # be gentle with APIs

        # Luo Kai generates smart questions based on what it learned
        print(f"\n🐉 Round {round_num}: Luo Kai asks...")
        prev_knowledge = "\n".join([f"{c['speaker']}: {c['text'][:300]}" for c in conversation[-2:]])
        
        luokai_question = ask_groq(f"""Based on this conversation about {topic}:
{prev_knowledge}

Generate the most insightful follow-up question that will uncover deeper knowledge.
Ask ONE specific, deep question only. No preamble.""", max_tokens=256)

        if not luokai_question:
            luokai_question = f"What are the most practical applications of {topic} for making money?"

        print(f"🐉 Luo Kai asks: {luokai_question[:200]}")
        conversation.append({"speaker": "Luo Kai", "text": luokai_question})
        full_log += f"LUO KAI ASKS:\n{luokai_question}\n\n"

        # Ollama answers
        time.sleep(2)
        print(f"🖥️  Ollama answers...")
        ollama_answer = ollama_think(f"""Previous context about {topic}:
{prev_knowledge}

Question: {luokai_question}

Give a deep, specific, expert answer. Include examples and actionable insights.""")

        print(f"🖥️  Ollama: {ollama_answer[:200]}...")
        conversation.append({"speaker": "Ollama", "text": ollama_answer})
        full_log += f"OLLAMA ANSWERS:\n{ollama_answer}\n\n"

        # Save each round to memory
        remember(
            f"Round {round_num}: {luokai_question[:100]}", 
            ollama_answer, 
            "learning", 
            success=True
        )

    # Final round — Luo Kai summarizes what he learned
    print(f"\n🐉 Final: Luo Kai summarizes learnings...")
    full_conversation = "\n".join([f"{c['speaker']}: {c['text'][:400]}" for c in conversation])
    
    summary = ask_groq(f"""You just had a deep learning conversation about: {topic}

Full conversation:
{full_conversation[:3000]}

Now:
1. Summarize the TOP 10 most important things you learned
2. Identify 3 patterns you noticed
3. List 5 ways to USE this knowledge to make money
4. What should you learn next?

This is your permanent memory — make it count.""", max_tokens=1024)

    if not summary:
        summary = f"Learned about {topic} from Ollama in {rounds} rounds."

    print(f"\n🐉 Luo Kai learned:\n{summary[:500]}...")
    full_log += f"LUO KAI'S SUMMARY:\n{summary}\n"

    # Save summary to long term memory
    remember(f"LEARNED: {topic}", summary, "learning_summary", success=True)
    learn_pattern(f"Knowledge about {topic}", summary[:300])

    # Save full session to file
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"learning_{topic[:30].replace(' ','_')}_{ts}.txt"
    write_file(filename, full_log)
    print(f"\n💾 Full session saved: workspace/{filename}")
    print(f"\n✅ Learning complete! Luo Kai now knows {topic} deeply!")
    
    return summary

print("📚 Learn from Ollama module loaded!")
