import time
from twilio.rest import Client

# To find these visit https://www.twilio.com/user/account
ACCOUNT_SID             = "XXXXX"
AUTH_TOKEN              = "XXXXX"
twilio_phone_numer      = "XXXXX"
brother_phone_number    = "XXXXX"

client = Client(ACCOUNT_SID, AUTH_TOKEN)
for i in range(10):
    try:
        client.messages.create(
            to=alex,
            body="Ciao!, Hows it goin?",  # Message body, if any
            from_=twilio_phone_numer,
        )
        print('send message')
    except Exception as e:
        print('error:'+str(e))
        pass
    time.sleep(1)
