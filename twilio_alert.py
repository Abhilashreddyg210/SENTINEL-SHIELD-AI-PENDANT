from twilio.rest import Client

def send_alert(message):
    account_sid = 'YOUR_TWILIO_SID'
    auth_token = 'YOUR_TWILIO_AUTH_TOKEN'
    from_number = 'YOUR_TWILIO_NUMBER'
    to_numbers = ['+91XXXXXXXXXX', '+91XXXXXXXXXX']  5 trusted numbers here

    client = Client(account_sid, auth_token)
    for number in to_numbers:
        client.messages.create(
            body=message,
            from_=from_number,
            to=number
        )
