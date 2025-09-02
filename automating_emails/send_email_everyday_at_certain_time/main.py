import smtplib
import ssl
import os
import time
from datetime import datetime
from dotenv import load_dotenv

load_dotenv(".env")

username = os.getenv("GMAIL_USERNAME")
password = os.getenv("GMAIL_PASSWORD")
receiver = os.getenv("RECEIVER")


def send_email(
    username_param: str, password_param: str, receiver_param: str, message_param: str
):
    host = "smtp.gmail.com"
    port = 465
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username_param, password_param)
        server.sendmail(username_param, receiver_param, message_param)


def main():
    msg = """Subject: [Tracking alert] MSI MAG Z890 TOMAHAWK WIFI price dropped
The price of MSI MAG Z890 TOMAHAWK WIFI has just dropped.
Current price: 6,990,000 đ
Recored at: 15:30 02/09/2025
"""
    msg = msg.encode("utf-8")
    while True:
        now = datetime.now()
        if now.hour == 9:
            try:
                send_email(username, password, receiver, msg)
                print("Send email successfully")
                time.sleep(3600.0)
            except Exception:
                print("😕 Send email failed")


if __name__ == "__main__":
    main()
