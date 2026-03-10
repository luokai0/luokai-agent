import os
import time
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

# Load all keys dynamically
API_KEYS = []
for i in range(1, 51):
    key = os.getenv(f"GROQ_API_KEY_{i}")
    if key:
        API_KEYS.append({"index": i, "key": key, "fails": 0, "last_used": 0})

print(f"🔑 Loaded {len(API_KEYS)} Groq API keys")

current_index = 0

def get_best_key():
    """Get the key that was used least recently"""
    global current_index
    current_index = (current_index + 1) % len(API_KEYS)
    return API_KEYS[current_index]

def ask(prompt, memory=""):
    """Try all keys in rotation until one works"""
    full = f"{memory}\n\nUser: {prompt}" if memory else prompt

    for attempt in range(len(API_KEYS)):
        key_obj = API_KEYS[(current_index + attempt) % len(API_KEYS)]
        try:
            client = Groq(api_key=key_obj["key"])
            response = client.chat.completions.create(
                model="llama3-70b-8192",
                messages=[{"role": "user", "content": full}],
                max_tokens=2048
            )
            key_obj["fails"] = 0
            key_obj["last_used"] = time.time()
            print(f"✅ Key {key_obj['index']} responded")
            get_best_key()
            return response.choices[0].message.content
        except Exception as e:
            err = str(e)[:80]
            key_obj["fails"] += 1
            print(f"⚠️ Key {key_obj['index']} failed ({key_obj['fails']} fails): {err}")
            time.sleep(0.5)
            continue

    return "❌ All keys failed. Add more keys to .env"
