import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(".env")

username = os.getenv("GMAIL_USERNAME")
password = os.getenv("GMAIL_PASSWORD")
receiver = os.getenv("RECEIVER")
sender = username


# Create the email
msg = MIMEMultipart()
msg["From"] = sender
msg["To"] = receiver
msg["Subject"] = "Test email with attachment"

# Add body
body = "Hi, this is a test email with an attachment sent from Python."
msg.attach(MIMEText(body, "plain"))

# File to attach
filepath = Path("automating_emails/send_email_with_attachments/hello.txt")

with open(filepath, mode="rb") as fr:
    mime_base = MIMEBase("application", "octet-stream")
    mime_base.set_payload(fr.read())


# Encode to base64
encoders.encode_base64(mime_base)
mime_base.add_header("Content-Disposition", f"attachment; filename={filepath.name}")
msg.attach(mime_base)


# Send email using Gmail SMTP server
try:
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()  # Secure the connection
        server.login(username, password)
        server.sendmail(sender, receiver, msg.as_string())
        print("✅ Email sent successfully")
except Exception as e:
    print("❌ Error:", e)
