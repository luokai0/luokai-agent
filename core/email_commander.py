# 🐉 LUO KAI AGENT — EMAIL COMMAND SYSTEM
# You email Luo Kai → he does the task → emails you back

import imaplib
import smtplib
import email
import os
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
load_dotenv()

SMTP_LOGIN = "a4935b001@smtp-brevo.com"
SMTP_PASS = os.getenv("BREVO_SMTP_KEY")
YOUR_EMAIL = "creationslous@gmail.com"

def send_reply(to, subject, body):
    msg = MIMEMultipart()
    msg['From'] = YOUR_EMAIL
    msg['To'] = to
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    server = smtplib.SMTP('smtp-relay.brevo.com', 587)
    server.starttls()
    server.login(SMTP_LOGIN, SMTP_PASS)
    server.send_message(msg)
    server.quit()
    print(f"✅ Reply sent to {to}")

def read_gmail_commands(gmail, app_password):
    """Read Gmail inbox for commands"""
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login(gmail, app_password)
    mail.select('inbox')
    _, msgs = mail.search(None, 'UNSEEN')
    commands = []
    for eid in msgs[0].split():
        _, data = mail.fetch(eid, '(RFC822)')
        msg = email.message_from_bytes(data[0][1])
        subject = msg['subject'] or ""
        sender = msg['from']
        body = ""
        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == "text/plain":
                    body = part.get_payload(decode=True).decode()[:1000]
                    break
        else:
            body = msg.get_payload(decode=True).decode()[:1000]
        commands.append({"subject": subject, "body": body, "from": sender, "id": eid})
        mail.store(eid, '+FLAGS', '\\Seen')
    mail.close()
    mail.logout()
    return commands

def execute_email_command(command):
    """Execute a command received via email"""
    from core.router import ask
    from core.search import search

    subject = command['subject']
    body = command['body']
    task = f"{subject}\n{body}".strip()

    print(f"\n📧 Email command: {task}")

    # Check if it needs search
    needs_search = any(w in task.lower() for w in ['search', 'find', 'latest', 'news', 'price', 'what is', 'who is'])
    
    context = ""
    if needs_search:
        context = search(task)

    prompt = f"""You are Luo Kai Agent. Your owner emailed you this task:
{task}

{f'Research data: {context}' if context else ''}

Execute this task completely and reply with a detailed, actionable response.
Be specific, bold, and valuable. Sign off as Luo Kai Agent."""

    result = ask(prompt)
    return result

def start_email_listener(gmail, app_password, check_interval=60):
    """Listen for email commands and execute them"""
    print(f"📬 Email Commander started!")
    print(f"📧 Listening: {gmail}")
    print(f"⏰ Checking every {check_interval}s")
    print("Send emails to yourself to command Luo Kai!\n")

    while True:
        try:
            commands = read_gmail_commands(gmail, app_password)
            if commands:
                print(f"📬 {len(commands)} new command(s)!")
                for cmd in commands:
                    result = execute_email_command(cmd)
                    send_reply(YOUR_EMAIL, f"✅ Re: {cmd['subject']}", result)
                    print(f"✅ Executed and replied!")
            else:
                print(f"📭 No new emails. Checking again in {check_interval}s...")
        except Exception as e:
            print(f"⚠️ Error: {e}")
        time.sleep(check_interval)

print("📬 Email Commander loaded!")
