import pandas as pd
from datetime import datetime, timedelta
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

FILE = "payments.xlsx"
REMINDER_DAYS = 7  # remind client a week before due date


def send_email(to, cc_list, subject, body):
    sender = "sales@swag-official.com"
    password = "vjqs pfgk afue hbti"

    msg = MIMEText(body, "plain")
    msg["From"] = sender
    msg["To"] = to
    msg["Cc"] = ", ".join(cc_list)
    msg["Subject"] = subject

    all_recipients = [to] + cc_list

    try:
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(sender, password)
        server.sendmail(sender, all_recipients, msg.as_string())
        server.quit()
        print(f"[EMAIL SENT] → {all_recipients}")
    except Exception as e:
        print(f"[ERROR] {e}")


def check_payments():
    df = pd.read_excel(FILE)
    today = datetime.now().date()

    for _, row in df.iterrows():
        due = pd.to_datetime(row["due_date"]).date()
        days_left = (due - today).days

        # CC list → accountant manager + sales team 
        cc_emails = [
            row["accountantmanager_email"],
        ]

        # ===== UPCOMING PAYMENT =====
        if days_left == REMINDER_DAYS:
            subject = f"⏳ Payment Reminder — Due in {days_left} days"
            body = f"""
Dear {row['client_name']},

This is a reminder that your upcoming payment for **{row['project']}** 
is due on **{due}**.

Amount Due: {row['amount']} EGP  
Days Remaining: {days_left}

Best regards,  
SWAG For Contracting & Real Estate Development Payment System
            """
            send_email(row["email_client"], cc_emails, subject, body)

        # ===== PAYMENT DUE TODAY =====
        elif days_left == 0:
            subject = "📌 Payment Due Today"
            body = f"""
Dear {row['client_name']},

Your payment for **{row['project']}** (Amount: {row['amount']} EGP) 
is due **today**.

Please complete the due amount as soon as possible.

Best regards,  
SWAG For Contracting & Real Estate Development Payment System
            """
            send_email(row["email_client"], cc_emails, subject, body)

        # ===== OVERDUE PAYMENT =====
        elif days_left < 0:
            overdue_days = abs(days_left)
            subject = f"⚠️ Overdue Payment — {overdue_days} days late"
            body = f"""
Dear {row['client_name']},

Your payment for **{row['project']}** is now **{overdue_days} days overdue**.

Amount Due: {row['amount']} EGP  
Due Date: {due}

Please settle the payment urgently.

Best regards,  
SWAG For Contracting & Real Estate Development Payment System
            """
            send_email(row["email_client"], cc_emails, subject, body)

if __name__ == "__main__":
    check_payments()
