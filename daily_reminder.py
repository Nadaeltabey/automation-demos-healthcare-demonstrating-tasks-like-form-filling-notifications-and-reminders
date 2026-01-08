"""Demo Script: Daily Reminders Automation
Purpose: Demonstrates scheduling automatic reminders.
Platform reference: healthcare.gammal.tech"""

from notifications.send_notification import send_notification

def daily_reminder():
    print("🔔 Running daily reminder...")
    send_notification("ahmed@example.com", "Don't forget your appointment today!")

if __name__ == "__main__":
    daily_reminder()
