# 🐉 LUO KAI AGENT — AUTO GMAIL CREATOR
import requests
import time
import random
import string
from core.browser import get_page_content
from playwright.sync_api import sync_playwright

# Free temp SMS services
SMS_SERVICES = [
    "https://api.herosms.io/stubs/handler_api.php",
]

NAMES = [
    ("alex", "morgan"), ("jordan", "blake"), ("chris", "taylor"),
    ("sam", "rivera"), ("max", "chen"), ("riley", "park"),
    ("casey", "kim"), ("drew", "lee"), ("jamie", "wong"),
    ("robin", "hassan"), ("luo", "kai"), ("kai", "agent")
]

def random_username():
    first, last = random.choice(NAMES)
    num = random.randint(100, 9999)
    return f"{first}.{last}{num}"

def random_password():
    chars = string.ascii_letters + string.digits + "!@#$"
    return ''.join(random.choices(chars, k=16))

def get_temp_number(api_key, service="go"):
    """Get temp phone number from sms-activate.org"""
    url = f"https://api.herosms.io/stubs/handler_api.php"
    params = {
        "api_key": api_key,
        "action": "getNumber",
        "service": service,
        "country": 0  # any country
    }
    r = requests.get(url, params=params)
    print(f"📱 SMS service response: {r.text}")
    if "ACCESS_NUMBER" in r.text:
        parts = r.text.split(":")
        activation_id = parts[1]
        phone = parts[2]
        return activation_id, phone
    return None, None

def get_sms_code(api_key, activation_id, max_wait=120):
    """Wait for SMS verification code"""
    url = "https://api.herosms.io/stubs/handler_api.php"
    print(f"⏳ Waiting for SMS code (max {max_wait}s)...")
    for i in range(max_wait // 5):
        time.sleep(5)
        params = {
            "api_key": api_key,
            "action": "getStatus",
            "id": activation_id
        }
        r = requests.get(url, params=params)
        print(f"  SMS status: {r.text}")
        if "STATUS_OK" in r.text:
            code = r.text.split(":")[1]
            return code
        elif "STATUS_CANCEL" in r.text:
            return None
    return None

def create_gmail(sms_api_key=None):
    """Create a Gmail account automatically"""
    username = random_username()
    password = random_password()
    email = f"{username}@gmail.com"
    
    print(f"\n📧 Creating Gmail: {email}")
    print(f"🔑 Password: {password}")
    
    # Save credentials immediately
    creds = f"EMAIL={email}\nPASSWORD={password}\nSTATUS=creating\n"
    with open("workspace/gmail_creds.txt", "w") as f:
        f.write(creds)
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, slow_mo=800)
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        )
        page = context.new_page()
        
        try:
            # Go to Gmail signup
            print("🌐 Opening Gmail signup...")
            page.goto("https://accounts.google.com/signup", timeout=30000)
            time.sleep(2)
            
            # Fill first name
            page.fill('input[name="firstName"]', username.split(".")[0].capitalize())
            time.sleep(0.5)
            
            # Fill last name  
            page.fill('input[name="lastName"]', username.split(".")[1][:-4].capitalize())
            time.sleep(0.5)
            
            # Click next
            page.click('button:has-text("Next")')
            time.sleep(2)
            
            # Fill birthday (random adult age)
            try:
                page.select_option('select[id="month"]', str(random.randint(1,12)))
                page.fill('input[id="day"]', str(random.randint(1,28)))
                page.fill('input[id="year"]', str(random.randint(1985,2000)))
                page.select_option('select[id="gender"]', "1")
                page.click('button:has-text("Next")')
                time.sleep(2)
            except:
                print("⚠️ Birthday step skipped")
            
            # Choose email
            try:
                page.click(f'text={username}')
                time.sleep(1)
            except:
                try:
                    page.click('text=Create your own Gmail address')
                    time.sleep(1)
                    page.fill('input[name="Username"]', username)
                    time.sleep(0.5)
                except:
                    pass
            
            page.click('button:has-text("Next")')
            time.sleep(2)
            
            # Fill password
            page.fill('input[name="Passwd"]', password)
            time.sleep(0.5)
            page.fill('input[name="PasswdAgain"]', password)
            time.sleep(0.5)
            page.click('button:has-text("Next")')
            time.sleep(2)
            
            # Phone verification
            if sms_api_key:
                print("📱 Getting temp phone number...")
                activation_id, phone = get_temp_number(sms_api_key)
                
                if phone:
                    print(f"📱 Got number: {phone}")
                    page.fill('input[type="tel"]', phone)
                    page.click('button:has-text("Next")')
                    time.sleep(3)
                    
                    code = get_sms_code(sms_api_key, activation_id)
                    if code:
                        print(f"✅ Got SMS code: {code}")
                        page.fill('input[type="tel"]', code)
                        page.click('button:has-text("Next")')
                        time.sleep(2)
                    else:
                        print("⚠️ SMS code not received")
                else:
                    print("⚠️ Could not get temp number")
            else:
                print("⚠️ No SMS API key — phone step will need manual input")
                input("Enter verification code manually then press Enter: ")
            
            # Accept terms
            try:
                page.click('button:has-text("I agree")')
                time.sleep(2)
            except:
                pass
            
            # Check if we made it
            current_url = page.url
            print(f"📍 Current URL: {current_url}")
            
            if "myaccount" in current_url or "mail" in current_url:
                print(f"✅ Gmail created successfully: {email}")
                with open("workspace/gmail_creds.txt", "w") as f:
                    f.write(f"EMAIL={email}\nPASSWORD={password}\nSTATUS=active\n")
                with open(".env", "a") as f:
                    f.write(f"\nLUOKAI_EMAIL={email}\nLUOKAI_EMAIL_PASSWORD={password}\n")
                browser.close()
                return email, password
            else:
                print("⚠️ Gmail creation may need manual steps")
                browser.close()
                return email, password
                
        except Exception as e:
            print(f"⚠️ Error: {e}")
            browser.close()
            return email, password

def send_email(to, subject, body, from_email=None, password=None):
    """Send email using Luo Kai's Gmail"""
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    import os
    from dotenv import load_dotenv
    load_dotenv()
    
    sender = from_email or os.getenv("LUOKAI_EMAIL")
    pwd = password or os.getenv("LUOKAI_EMAIL_PASSWORD")
    
    if not sender or not pwd:
        return "⚠️ No email credentials found. Run create_gmail() first."
    
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = to
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender, pwd)
        server.send_message(msg)
        server.quit()
        print(f"✅ Email sent to {to}")
        return True
    except Exception as e:
        print(f"⚠️ Email failed: {e}")
        return False

def read_emails(from_email=None, password=None, limit=10):
    """Read emails from Luo Kai's Gmail"""
    import imaplib
    import email
    import os
    from dotenv import load_dotenv
    load_dotenv()
    
    sender = from_email or os.getenv("LUOKAI_EMAIL")
    pwd = password or os.getenv("LUOKAI_EMAIL_PASSWORD")
    
    if not sender or not pwd:
        return "⚠️ No email credentials. Run create_gmail() first."
    
    try:
        mail = imaplib.IMAP4_SSL('imap.gmail.com')
        mail.login(sender, pwd)
        mail.select('inbox')
        
        _, messages = mail.search(None, 'ALL')
        email_ids = messages[0].split()[-limit:]
        
        emails = []
        for eid in email_ids:
            _, msg_data = mail.fetch(eid, '(RFC822)')
            msg = email.message_from_bytes(msg_data[0][1])
            subject = msg['subject']
            sender_addr = msg['from']
            body = ""
            if msg.is_multipart():
                for part in msg.walk():
                    if part.get_content_type() == "text/plain":
                        body = part.get_payload(decode=True).decode()[:500]
                        break
            else:
                body = msg.get_payload(decode=True).decode()[:500]
            emails.append({"from": sender_addr, "subject": subject, "body": body})
        
        mail.close()
        mail.logout()
        return emails
    except Exception as e:
        return f"⚠️ Email read failed: {e}"

print("📧 Gmail Creator loaded!")
