# Contract-Payment-Automation
A Python automation system that monitors contract expirations and client payments. It automatically sends email alerts for upcoming contract renewals, upcoming payments, due payments, and overdue payments, helping the team stay on top of critical deadlines and improve operational efficiency.

## A fully automated Python system that sends:

-client payment reminders

-Contract expiry alerts

-Emails to: Client, Accountant

-Runs every day at 9 AM automatically via Docker + Cron

## 📌 Features
✔ Fully automated email reminders

✔ Dockerized — runs on any device

✔ Daily cron scheduling

✔ Secure SMTP credentials via .env

✔ Logging system

✔ Easy to deploy anywhere

## Install dependencies:
```bash
pip install -r requirements.txt
```
## Docker Instructions
Using Docker Compose:
```bash
version: "3.9"
services:
  contracts:
    build: .
    command: python contracts.py
    env_file:
      - .env
    volumes:
      - ./contracts.xlsx:/app/contracts.xlsx

  payments:
    build: .
    command: python payments.py
    env_file:
      - .env
    volumes:
      - ./payments.xlsx:/app/payments.xlsx
```
Run everything together:
```bash
docker-compose up --build
```
## Email Setup with App Password
1.Enable 2-Step Verification on your Gmail account.

2.Go to App Passwords → generate a password for:
   -App: Mail
   -Device: Other (name it anythingyouwant)
   
3.Store credentials in a .env file
