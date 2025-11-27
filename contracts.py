import pandas as pd
from datetime import datetime, timedelta
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

CONTRACT_FILE = "contracts.xlsx" 
ALERT_DAYS = 30  # alert for contracts expiring within a month


load_dotenv()

def send_email(to, cc_list, subject, body):
    sender = os.getenv("EMAIL_USER")
    password = os.getenv("EMAIL_PASS")

    msg = MIMEText(body)
    msg["From"] = sender
    msg["To"] = to
    msg["Subject"] = subject

    try:
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(sender, password)
        server.sendmail(sender, to, msg.as_string())
        server.quit()
        print(f"[EMAIL SENT] → {to}")
    except Exception as e:
        print(f"[ERROR] Email sending failed: {e}")


def check_contracts():
    df = pd.read_excel(CONTRACT_FILE)
    today = datetime.now().date()

    print("Checking contract expiration status...\n")

    for _, row in df.iterrows():
        expiry = pd.to_datetime(row["expiry_date"], format="%d-%m-%Y").date()

        days_left = (expiry - today).days

        # Skip expired or long-term contracts
        if days_left <= 0:
            continue
        if days_left > ALERT_DAYS:
            continue

        # Build email body
        message = f"""
Dear Team,

The following contract is about to expire:

Contract ID: {row['contract_id']}
Contractor : {row['contractor_name']}
Type       : {row['contract_type']}
Expiry     : {expiry} (in {days_left} days)

Please take the necessary renewal actions.

Regards,
Swag For Contracting & Real Estate Development Contract Automation System
        """

        # Send alert
        send_email(
            to=row["email"],
            subject=f"⚠️ Contract Expiry Alert – {row['contract_id']} ({days_left} days left)",
            body=message
        )

        print(f"[ALERT] {row['contract_id']} expires in {days_left} days")


if __name__ == "__main__":
    check_contracts()
