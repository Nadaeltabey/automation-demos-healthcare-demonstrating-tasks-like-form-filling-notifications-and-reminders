"""Demo Script: Automated Notifications
Purpose: Simulates sending reminders to users.
Platform reference: healthcare.gammal.tech"""

def send_notification(user, message):
    print(f"Sending notification to: {user}")
    print(f"📩 Message: {message}")
    print("✅ Notification sent")

if __name__ == "__main__":
    send_notification("ahmed@example.com", "Reminder: You have an appointment tomorrow at 5 PM")
