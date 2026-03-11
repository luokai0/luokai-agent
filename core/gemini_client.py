import os
from dotenv import load_dotenv
load_dotenv()

def ask_gemini_direct(prompt, key, max_tokens=2048):
    try:
        import requests
        response = requests.post(
            f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={key}",
            json={"contents": [{"parts": [{"text": prompt}]}]},
            timeout=30
        )
        data = response.json()
        if "candidates" in data:
            return data["candidates"][0]["content"]["parts"][0]["text"]
    except Exception as e:
        print(f"⚠️ Gemini error: {e}")
    return None
