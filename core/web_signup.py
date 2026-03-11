# 🐉 LUO KAI AGENT — AUTO WEB SIGNUP
from playwright.sync_api import sync_playwright
from core.router import ask
from core.email_sender import send_email
import time
import json

YOUR_EMAIL = "creationslous@gmail.com"

def signup_to_site(url, site_name):
    print(f"\n🤖 Signing up to {site_name}...")
    
    # Generate profile
    prompt = f"""Generate a realistic person profile for signing up to {site_name}.
Return ONLY JSON, nothing else:
{{"first_name": "...", "last_name": "...", "username": "...", "password": "LuoKai@2026!"}}"""
    resp = ask(prompt)
    try:
        if "```" in resp:
            resp = resp.split("```")[1].replace("json","").strip()
        profile = json.loads(resp.strip())
    except:
        profile = {"first_name": "Luo", "last_name": "Kai", "username": "luokai2026", "password": "LuoKai@2026!"}
    
    profile["email"] = YOUR_EMAIL
    print(f"👤 {profile['first_name']} {profile['last_name']} | {YOUR_EMAIL}")

    with open(f"workspace/signup_{site_name}.txt", "w") as f:
        for k,v in profile.items():
            f.write(f"{k}: {v}\n")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, slow_mo=500)
        page = browser.new_page(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36")
        
        try:
            # Go to signup page
            signup_url = url if 'signup' in url or 'register' in url else url.rstrip('/') + '/signup'
            print(f"🌐 Opening: {signup_url}")
            page.goto(signup_url, timeout=20000)
            time.sleep(3)

            # Fill by placeholder
            fills = [
                ('First Name', profile['first_name']),
                ('Last Name', profile['last_name']),
                ('Email', YOUR_EMAIL),
                ('Password', profile['password']),
            ]
            
            filled = 0
            for placeholder, value in fills:
                try:
                    page.fill(f'input[placeholder="{placeholder}"]', value, timeout=3000)
                    print(f"  ✅ {placeholder}: {value}")
                    filled += 1
                    time.sleep(0.4)
                except:
                    # Try case insensitive
                    try:
                        page.fill(f'input[placeholder*="{placeholder}" i]', value, timeout=2000)
                        print(f"  ✅ {placeholder}: {value}")
                        filled += 1
                        time.sleep(0.4)
                    except:
                        print(f"  ⚠️ Could not fill: {placeholder}")

            print(f"  📝 Filled {filled} fields")

            # Click signup button
            for btn in [
                'button[type="submit"]',
                'button:has-text("Sign up")',
                'button:has-text("Register")',
                'button:has-text("Create Account")',
                'button:has-text("Join")',
                'input[type="submit"]'
            ]:
                try:
                    page.click(btn, timeout=3000)
                    print(f"  ✅ Clicked signup!")
                    time.sleep(4)
                    break
                except:
                    continue

            final_url = page.url
            print(f"  📍 Final URL: {final_url}")

            # Check success
            if final_url != signup_url:
                print("  🎉 Signup successful!")
            else:
                print("  ⚠️ May need verification — check your Gmail!")

        except Exception as e:
            print(f"  ⚠️ Error: {e}")
        
        browser.close()

    # Email report
    report = f"""🐉 Luo Kai Agent — Signup Report

Site: {site_name}
Email: {YOUR_EMAIL}
Password: {profile['password']}
Name: {profile['first_name']} {profile['last_name']}

✅ Check your Gmail for verification email from {site_name}!
Credentials saved to workspace/signup_{site_name}.txt
"""
    send_email(YOUR_EMAIL, f"✅ Signed up to {site_name}", report)
    print(f"\n✅ Report emailed to {YOUR_EMAIL}!")
    return profile

print("🤖 Web Signup loaded!")
