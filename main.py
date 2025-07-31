from firebase_config import db
from twilio_alert import send_alert
import time

def detect_trigger():
    # Simulated trigger (tap or voice)
    input_value = input("Tap pattern or voice cue detected (y/n)? ")
    return input_value.lower() == 'y'

def handle_emergency():
    print("⚠️ Emergency trigger detected!")
    send_alert("Emergency! SentinelShield activated. Please respond immediately.")
    db.child("alerts").push({"message": "Emergency Alert Triggered"})

if __name__ == "__main__":
    while True:
        if detect_trigger():
            handle_emergency()
            break
        time.sleep(2)
