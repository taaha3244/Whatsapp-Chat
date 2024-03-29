import os
from twilio.rest import Client
from dotenv import load_dotenv,find_dotenv

load_dotenv(find_dotenv())

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

def send_twilio_message(message:str,sender_id: str)-> None: 
    message = client.messages.create(
                              body=message,
                              from_="whatsapp:+14155238886",
                              to=sender_id
                          )
    print(message.sid)
    return None

