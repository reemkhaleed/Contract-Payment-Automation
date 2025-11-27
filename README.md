# Contract-Payment-Automation
A Python automation system that monitors contract expirations and client payments. It automatically sends email alerts for upcoming contract renewals, upcoming payments, due payments, and overdue payments, helping the team stay on top of critical deadlines and improve operational efficiency.

## A fully automated Python system that sends:

-Monthly client payment reminders
-Contract expiry alerts
-Daily automated reports
-Emails to: Client, Accountant, Sales Team
-Runs every day at 9 AM automatically via Docker + Cron

## 📌 Features
✔ Fully automated email reminders
✔ Dockerized — runs on any device
✔ Daily cron scheduling
✔ Secure SMTP credentials via .env
✔ Logging system
✔ Easy to deploy anywhere

##Install dependencies:
```bash
pip install -r requirements.txt
```
## Docker Instructions
Build the Docker image:
```bash
docker build -t swag-automation .
```

Run the contracts script:
```bash
docker run --env-file .env -v $(pwd)/contracts.xlsx:/app/contracts.xlsx swag-automation
```

Run the payments script:
```bash
docker run --env-file .env -v $(pwd)/payments.xlsx:/app/payments.xlsx swag-automation
```
## Email Setup with App Password
1.Enable 2-Step Verification on your Gmail account.
2.Go to App Passwords → generate a password for:
   -App: Mail
   -Device: Other (name it ContractAutomation)
3.Store credentials in a .env file
