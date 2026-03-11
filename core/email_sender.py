import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
load_dotenv()

def send_email(to, subject, body):
    msg = MIMEMultipart()
    msg['From'] = 'creationslous@gmail.com'
    msg['To'] = to
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    try:
        server = smtplib.SMTP('smtp-relay.brevo.com', 587)
        server.starttls()
        server.login('a4935b001@smtp-brevo.com', 'gRdLtGja5cr9pxvJ')
        server.send_message(msg)
        server.quit()
        print(f"✅ Email sent to {to}!")
        return True
    except Exception as e:
        print(f"⚠️ Failed: {e}")
        return False

print("📧 Email sender loaded!")
