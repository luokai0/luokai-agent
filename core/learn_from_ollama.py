# 🐉 LUO KAI — SELF LEARNING SYSTEM
# Uses Groq to teach itself any topic
# Saves everything to long term memory forever

import time
from core.router import ask_groq
from core.long_memory import remember, learn_pattern
from core.files import write_file
from datetime import datetime

def learn_from_ollama(topic, rounds=3):
    """
    Luo Kai teaches itself through self-dialogue
    Teacher mode → Student mode → saves forever
    """
    print(f"\n🧠 LUO KAI SELF LEARNING SESSION")
    print(f"📚 Topic: {topic}")
    print(f"🔄 Rounds: {rounds}")
    print("=" * 50)

    full_log = f"LEARNING SESSION — {datetime.now().strftime('%Y-%m-%d %H:%M')}\nTopic: {topic}\n\n"
    conversation = []

    # Round 1 — Teacher mode: dump everything known
    print(f"\n📖 Round 1: Teaching phase...")
    teaching = ask_groq(f"""You are an expert teacher. 
Teach everything important about: {topic}

Include:
- Core concepts and fundamentals
- Advanced insights most people miss
- Practical real world applications
- Common mistakes to avoid
- Hidden knowledge and secrets
- How to use this to make money

Be extremely detailed and specific.""", max_tokens=1024)

    if not teaching:
        print("⚠️ Groq rate limited — try again in a minute!")
        return

    print(f"📖 Taught: {teaching[:150]}...")
    conversation.append(f"TEACHER: {teaching}")
    full_log += f"TEACHING:\n{teaching}\n\n"
    remember(f"Learned about {topic}", teaching, "learning", success=True)
    time.sleep(8)

    # Rounds 2-N — Student asks deep questions
    for round_num in range(2, rounds + 1):
        print(f"\n🤔 Round {round_num}: Asking deep question...")
        
        prev = "\n".join(conversation[-2:])
        
        question = ask_groq(f"""Based on this knowledge about {topic}:
{prev[-1000:]}

Generate ONE deeply insightful question that will uncover:
- Hidden connections
- Practical money-making applications  
- Things most people never think about

Ask only ONE specific question. No preamble.""", max_tokens=256)

        if not question:
            print("⚠️ Skipping round — rate limited")
            time.sleep(10)
            continue

        print(f"🤔 Question: {question[:150]}...")
        conversation.append(f"STUDENT: {question}")
        full_log += f"QUESTION:\n{question}\n\n"
        time.sleep(8)

        # Answer the question
        print(f"💡 Answering...")
        answer = ask_groq(f"""Topic: {topic}
Question: {question}
Context: {teaching[:500]}

Give a deep expert answer with:
- Specific examples
- Actionable insights
- Money making angles
- Surprising facts""", max_tokens=768)

        if not answer:
            time.sleep(10)
            continue

        print(f"💡 Answer: {answer[:150]}...")
        conversation.append(f"EXPERT: {answer}")
        full_log += f"ANSWER:\n{answer}\n\n"
        remember(f"Q&A about {topic}: {question[:80]}", answer, "learning", success=True)
        time.sleep(8)

    # Final — summarize all learnings
    print(f"\n🧠 Summarizing everything learned...")
    full_text = "\n".join(conversation)
    
    summary = ask_groq(f"""You just completed a deep learning session about: {topic}

Full session:
{full_text[:3000]}

Create your permanent memory summary:
1. TOP 10 most important things learned
2. 3 surprising insights
3. 5 ways to USE this knowledge to make money RIGHT NOW
4. What to learn next about this topic
5. One sentence summary for quick recall

This is saved to your long term memory forever — make it count.""", max_tokens=1024)

    if summary:
        print(f"\n🧠 Summary: {summary[:300]}...")
        remember(f"MASTER SUMMARY: {topic}", summary, "learning_summary", success=True)
        learn_pattern(f"Deep knowledge: {topic}", summary[:300])
        full_log += f"MASTER SUMMARY:\n{summary}\n"

    # Save full session
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"learning_{topic[:30].replace(' ','_')}_{ts}.txt"
    write_file(filename, full_log)
    
    print(f"\n💾 Saved: workspace/{filename}")
    print(f"✅ Luo Kai now knows {topic} deeply!")
    print(f"🧠 Saved to long term memory forever!")
    
    return summary

print("📚 Self Learning System loaded!")
