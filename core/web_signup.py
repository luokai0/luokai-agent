# 🐉 LUO KAI AGENT — AUTO WEB SIGNUP
from playwright.sync_api import sync_playwright
from core.router import ask
from core.email_sender import send_email
import time
import json

YOUR_EMAIL = "creationslous@gmail.com"

def signup_to_site(url, site_name, extra_info=""):
    """Sign up to any website automatically"""
    
    print(f"\n🤖 Signing up to {site_name}...")
    print(f"🌐 URL: {url}")
    
    # Generate profile
    prompt = f"""Generate a realistic profile for signing up to {site_name}.
Return ONLY JSON:
{{"first_name": "...", "last_name": "...", "username": "...", "password": "LuoKai@{site_name[:4]}2026!", "bio": "..."}}"""
    
    resp = ask(prompt)
    try:
        if "```" in resp:
            resp = resp.split("```")[1].replace("json","").strip()
        profile = json.loads(resp.strip())
    except:
        profile = {"first_name": "Luo", "last_name": "Kai", "username": f"luokai{int(time.time())%9999}", "password": "LuoKai@2026!"}
    
    profile["email"] = YOUR_EMAIL
    print(f"👤 Profile: {profile['first_name']} {profile['last_name']} | {profile['email']}")

    # Save credentials
    with open(f"workspace/signup_{site_name}.txt", "w") as f:
        for k,v in profile.items():
            f.write(f"{k}: {v}\n")
    print(f"💾 Credentials saved to workspace/signup_{site_name}.txt")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, slow_mo=600)
        page = browser.new_page(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36")
        
        try:
            page.goto(url, timeout=20000)
            time.sleep(2)
            
            # Try filling common signup fields
            fields = [
                ('input[name="email"], input[type="email"], input[placeholder*="email" i]', profile["email"]),
                ('input[name="firstName"], input[name="first_name"], input[placeholder*="first" i]', profile["first_name"]),
                ('input[name="lastName"], input[name="last_name"], input[placeholder*="last" i]', profile["last_name"]),
                ('input[name="username"], input[name="user_name"], input[placeholder*="username" i]', profile["username"]),
                ('input[name="password"], input[type="password"]', profile["password"]),
            ]
            
            filled = 0
            for selector, value in fields:
                for sel in selector.split(", "):
                    try:
                        page.fill(sel.strip(), value, timeout=2000)
                        print(f"  ✅ Filled: {sel.strip()[:30]}")
                        filled += 1
                        time.sleep(0.3)
                        break
                    except:
                        continue
            
            print(f"  📝 Filled {filled} fields")
            
            # Try clicking signup button
            for btn in ['button[type="submit"]', 'button:has-text("Sign up")', 'button:has-text("Register")', 'button:has-text("Create")', 'button:has-text("Join")', 'input[type="submit"]']:
                try:
                    page.click(btn, timeout=2000)
                    print(f"  ✅ Clicked signup button")
                    time.sleep(3)
                    break
                except:
                    continue
            
            final_url = page.url
            print(f"  📍 Final URL: {final_url}")
            
        except Exception as e:
            print(f"  ⚠️ Error: {e}")
        
        browser.close()
    
    # Email summary
    summary = f"""🐉 Luo Kai Agent — Signup Report
    
Site: {site_name}
URL: {url}
Email: {profile['email']}
Username: {profile.get('username')}
Password: {profile.get('password')}

✅ Signup attempted! Check your Gmail for verification email.
Credentials saved to workspace/signup_{site_name}.txt
"""
    send_email(YOUR_EMAIL, f"✅ Signed up to {site_name}", summary)
    print(f"\n✅ Done! Check your Gmail for verification email from {site_name}!")
    return profile

print("🤖 Web Signup loaded!")
