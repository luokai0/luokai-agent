# 🐉 LUO KAI AGENT — TEMP EMAIL SYSTEM
# Free unlimited emails, no phone needed

import requests
import time
import random

BASE = "https://api.guerrillamail.com/ajax.php"

def create_temp_email():
    """Create a free temp email instantly"""
    r = requests.get(BASE, params={"f": "get_email_address"})
    data = r.json()
    email = data["email_addr"]
    sid = data["sid_token"]
    print(f"📧 Temp email created: {email}")
    return email, sid

def check_inbox(sid, timeout=60):
    """Wait for emails to arrive"""
    print(f"⏳ Waiting for emails...")
    for i in range(timeout // 5):
        time.sleep(5)
        r = requests.get(BASE, params={"f": "get_email_list", "offset": 0, "sid_token": sid})
        data = r.json()
        emails = data.get("list", [])
        if emails:
            print(f"✅ Got {len(emails)} email(s)!")
            return emails
    return []

def read_email(mail_id, sid):
    """Read a specific email"""
    r = requests.get(BASE, params={"f": "fetch_email", "email_id": mail_id, "sid_token": sid})
    return r.json()

def get_verification_code(sid, timeout=120):
    """Wait for and extract verification code from email"""
    import re
    print("⏳ Waiting for verification code...")
    for i in range(timeout // 5):
        time.sleep(5)
        r = requests.get(BASE, params={"f": "get_email_list", "offset": 0, "sid_token": sid})
        emails = r.json().get("list", [])
        if emails:
            mail = read_email(emails[0]["mail_id"], sid)
            body = mail.get("mail_body", "")
            # Find 4-8 digit codes
            codes = re.findall(r'\b\d{4,8}\b', body)
            if codes:
                print(f"✅ Verification code: {codes[0]}")
                return codes[0]
            # Find links
            links = re.findall(r'https?://[^\s<>"]+', body)
            if links:
                print(f"✅ Verification link: {links[0]}")
                return links[0]
    return None

def signup_with_temp_email(service_url, service_name):
    """Create temp email and use it to sign up for a service"""
    from core.router import ask
    
    email, sid = create_temp_email()
    
    prompt = f"""You are Luo Kai Agent signing up for {service_name} at {service_url}.
The email to use is: {email}
Generate a realistic profile:
Return JSON only: {{"username": "...", "password": "...", "first_name": "...", "last_name": "...", "bio": "..."}}"""
    
    import json
    response = ask(prompt)
    try:
        if "```" in response:
            response = response.split("```")[1].replace("json","").strip()
        profile = json.loads(response.strip())
        profile["email"] = email
        profile["sid"] = sid
        
        print(f"✅ Profile ready for {service_name}:")
        print(f"   Email: {email}")
        print(f"   Username: {profile.get('username')}")
        print(f"   Password: {profile.get('password')}")
        
        # Save credentials
        with open(f"workspace/creds_{service_name}.txt", "w") as f:
            f.write(f"Service: {service_name}\n")
            for k, v in profile.items():
                if k != "sid":
                    f.write(f"{k}: {v}\n")
        
        return profile
    except Exception as e:
        print(f"⚠️ Profile generation failed: {e}")
        return {"email": email, "sid": sid}

print("📧 Temp Email system loaded!")
