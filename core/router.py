# 🐉 LUO KAI — SMART DUAL BRAIN ROUTER
# Primary: Groq (fast, smart)
# Backup: Ollama local (free, unlimited, no API key ever)

import os
import time
import requests
from groq import Groq
from dotenv import load_dotenv
from core.master_control import MASTER_LAWS

load_dotenv()

KEYS = []
for i in range(1, 51):
    key = os.getenv(f"GROQ_API_KEY_{i}")
    if key:
        KEYS.append(key)

print(f"🔑 Loaded {len(KEYS)} Groq API keys")

key_cooldown = {k: 0 for k in KEYS}
current_index = [0]

def get_next_key():
    now = time.time()
    for _ in range(len(KEYS)):
        i = current_index[0] % len(KEYS)
        current_index[0] += 1
        key = KEYS[i]
        if key_cooldown[key] <= now:
            return key, i
    best = min(KEYS, key=lambda k: key_cooldown[k])
    wait = key_cooldown[best] - now
    if wait > 0:
        print(f"⏳ Waiting {wait:.0f}s for key cooldown...")
        time.sleep(wait + 1)
    return best, 0

def ask_ollama(prompt, max_tokens=2048):
    """Use local Ollama — free, unlimited, no API key"""
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3.2",
                "prompt": f"{MASTER_LAWS}\n\nTask: {prompt}",
                "stream": False,
                "options": {"num_predict": max_tokens}
            },
            timeout=120
        )
        if response.status_code == 200:
            result = response.json().get("response", "")
            print("🖥️  Ollama (local) responded!")
            return result
    except Exception as e:
        print(f"⚠️ Ollama failed: {e}")
    return None

def ask_groq(prompt, max_tokens=2048, temperature=0.8):
    """Use Groq API — fast and smart"""
    full_prompt = f"{MASTER_LAWS}\n\nTask: {prompt}"
    key, index = get_next_key()
    try:
        client = Groq(api_key=key)
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": full_prompt}],
            max_tokens=max_tokens,
            temperature=temperature
        )
        key_cooldown[key] = 0
        print(f"✅ Key {index+1} responded")
        return response.choices[0].message.content
    except Exception as e:
        err = str(e)
        if "rate_limit" in err or "429" in err:
            key_cooldown[key] = time.time() + 60
            print(f"⏸️  Key {index+1} rate limited — switching to Ollama...")
        else:
            print(f"⚠️ Key {index+1} failed: {err[:50]}")
        return None

def ask(prompt, max_tokens=2048, temperature=0.8):
    """Smart router — Groq first, Ollama backup"""
    
    # Try Groq first
    result = ask_groq(prompt, max_tokens, temperature)
    if result:
        return result
    
    # All Groq keys exhausted — use Ollama
    print("🔄 Groq exhausted — switching to local Ollama brain...")
    result = ask_ollama(prompt, max_tokens)
    if result:
        return result
    
    return "❌ Both Groq and Ollama failed. Check your setup."

def ask_fast(prompt, max_tokens=512, temperature=0.7):
    return ask(prompt, max_tokens=max_tokens, temperature=temperature)

def ask_deep(prompt, max_tokens=4096, temperature=0.9):
    return ask(prompt, max_tokens=max_tokens, temperature=temperature)

print("🧠 Dual Brain Router loaded — Groq + Ollama ready!")
