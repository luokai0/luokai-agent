# 🐉 LUO KAI — MEGA ROUTER
import os
import time
import requests
from dotenv import load_dotenv
from core.master_control import MASTER_LAWS

load_dotenv()

CEREBRAS_KEYS = [os.getenv(f"CEREBRAS_API_KEY_{i}") for i in range(1,10) if os.getenv(f"CEREBRAS_API_KEY_{i}")]
GROQ_KEYS = [os.getenv(f"GROQ_API_KEY_{i}") for i in range(1,51) if os.getenv(f"GROQ_API_KEY_{i}")]
GEMINI_KEYS = [os.getenv(f"GEMINI_API_KEY_{i}") for i in range(1,20) if os.getenv(f"GEMINI_API_KEY_{i}")]
MISTRAL_KEYS = [os.getenv(f"MISTRAL_API_KEY_{i}") for i in range(1,10) if os.getenv(f"MISTRAL_API_KEY_{i}")]
OPENROUTER_KEYS = [os.getenv(f"OPENROUTER_API_KEY_{i}") for i in range(1,10) if os.getenv(f"OPENROUTER_API_KEY_{i}")]

idx = {"cerebras": 0, "groq": 0, "gemini": 0, "mistral": 0, "openrouter": 0}
cooldowns = {}

def is_ready(key):
    return cooldowns.get(key, 0) <= time.time()

def cooldown(key, secs=60):
    cooldowns[key] = time.time() + secs

def next_key(keys, provider):
    for _ in range(len(keys)):
        i = idx[provider] % len(keys)
        idx[provider] += 1
        key = keys[i]
        if is_ready(key):
            return key, i+1
    return None, 0

print(f"🔑 Loaded: {len(CEREBRAS_KEYS)} Cerebras | {len(GROQ_KEYS)} Groq | {len(GEMINI_KEYS)} Gemini | {len(MISTRAL_KEYS)} Mistral | {len(OPENROUTER_KEYS)} OpenRouter")

def ask_cerebras(prompt, max_tokens=2048):
    if not CEREBRAS_KEYS:
        return None
    key, num = next_key(CEREBRAS_KEYS, "cerebras")
    if not key:
        return None
    try:
        from cerebras.cloud.sdk import Cerebras
        client = Cerebras(api_key=key)
        response = client.chat.completions.create(
            model="llama-3.3-70b",
            messages=[{"role": "user", "content": f"{MASTER_LAWS}\n\nTask: {prompt}"}],
            max_tokens=max_tokens
        )
        print(f"⚡ Cerebras key {num} responded!")
        return response.choices[0].message.content
    except Exception as e:
        err = str(e)
        if "429" in err or "rate" in err.lower():
            cooldown(key, 60)
            print(f"⏸️ Cerebras key {num} cooling...")
        else:
            print(f"⚠️ Cerebras key {num}: {err[:50]}")
        return None

def ask_groq(prompt, max_tokens=2048, temperature=0.8):
    if not GROQ_KEYS:
        return None
    key, num = next_key(GROQ_KEYS, "groq")
    if not key:
        return None
    try:
        from groq import Groq
        client = Groq(api_key=key)
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": f"{MASTER_LAWS}\n\nTask: {prompt}"}],
            max_tokens=max_tokens,
            temperature=temperature
        )
        print(f"✅ Groq key {num} responded!")
        return response.choices[0].message.content
    except Exception as e:
        err = str(e)
        if "429" in err or "rate" in err.lower():
            cooldown(key, 60)
            print(f"⏸️ Groq key {num} cooling...")
        else:
            print(f"⚠️ Groq key {num}: {err[:50]}")
        return None

def ask_gemini(prompt, max_tokens=2048):
    if not GEMINI_KEYS:
        return None
    key, num = next_key(GEMINI_KEYS, "gemini")
    if not key:
        return None
    try:
        response = requests.post(
            f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={key}",
            json={"contents": [{"parts": [{"text": f"{MASTER_LAWS}\n\nTask: {prompt}"}]}]},
            timeout=30
        )
        data = response.json()
        if "candidates" in data:
            print(f"🔵 Gemini key {num} responded!")
            return data["candidates"][0]["content"]["parts"][0]["text"]
        else:
            cooldown(key, 60)
            print(f"⏸️ Gemini key {num} cooling...")
            return None
    except Exception as e:
        print(f"⚠️ Gemini key {num}: {str(e)[:50]}")
        return None

def ask_mistral(prompt, max_tokens=2048):
    if not MISTRAL_KEYS:
        return None
    key, num = next_key(MISTRAL_KEYS, "mistral")
    if not key:
        return None
    try:
        from mistralai import Mistral
        client = Mistral(api_key=key)
        response = client.chat.complete(
            model="mistral-small-latest",
            messages=[{"role": "user", "content": f"{MASTER_LAWS}\n\nTask: {prompt}"}],
            max_tokens=max_tokens
        )
        print(f"🟡 Mistral key {num} responded!")
        return response.choices[0].message.content
    except Exception as e:
        err = str(e)
        if "429" in err or "rate" in err.lower():
            cooldown(key, 60)
            print(f"⏸️ Mistral key {num} cooling...")
        else:
            print(f"⚠️ Mistral key {num}: {err[:50]}")
        return None

def ask_openrouter(prompt, max_tokens=2048):
    if not OPENROUTER_KEYS:
        return None
    key, num = next_key(OPENROUTER_KEYS, "openrouter")
    if not key:
        return None
    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
            json={
                "model": "meta-llama/llama-3.3-70b-instruct:free",
                "messages": [{"role": "user", "content": f"{MASTER_LAWS}\n\nTask: {prompt}"}],
                "max_tokens": max_tokens
            },
            timeout=30
        )
        data = response.json()
        if "choices" in data:
            print(f"🟢 OpenRouter key {num} responded!")
            return data["choices"][0]["message"]["content"]
        else:
            cooldown(key, 60)
            return None
    except Exception as e:
        print(f"⚠️ OpenRouter key {num}: {str(e)[:50]}")
        return None

def ask_ollama(prompt, max_tokens=1024):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": "tinyllama", "prompt": f"{MASTER_LAWS}\n\nTask: {prompt}", "stream": False, "options": {"num_predict": max_tokens}},
            timeout=60
        )
        if response.status_code == 200:
            print("🖥️ Ollama (local) responded!")
            return response.json().get("response", "")
    except:
        pass
    return None

def ask(prompt, max_tokens=2048, temperature=0.8):
    result = ask_cerebras(prompt, max_tokens)
    if result: return result
    result = ask_groq(prompt, max_tokens, temperature)
    if result: return result
    result = ask_gemini(prompt, max_tokens)
    if result: return result
    result = ask_mistral(prompt, max_tokens)
    if result: return result
    result = ask_openrouter(prompt, max_tokens)
    if result: return result
    result = ask_ollama(prompt, max_tokens)
    if result: return result
    return "❌ All providers exhausted. Wait a moment."

def ask_fast(prompt, max_tokens=512, temperature=0.7):
    return ask(prompt, max_tokens=max_tokens, temperature=temperature)

def ask_deep(prompt, max_tokens=4096, temperature=0.9):
    return ask(prompt, max_tokens=max_tokens, temperature=temperature)

print("🚀 MEGA ROUTER ready — 6 providers, never stops thinking!")
