"""Demo Script: Automated Form Filling
Purpose: Simulates a patient booking an appointment.
Platform reference: healthcare.gammal.tech"""

def fill_appointment_form(name, email, date):
    print("Opening appointment form page...")
    print(f"Entering Name: {name}")
    print(f"Entering Email: {email}")
    print(f"Selecting Appointment Date: {date}")
    print("Clicking Confirm button...")
    print("✅ Form submitted successfully")

if __name__ == "__main__":
    fill_appointment_form("Ahmed Ali", "ahmed@example.com", "2026-01-10")
