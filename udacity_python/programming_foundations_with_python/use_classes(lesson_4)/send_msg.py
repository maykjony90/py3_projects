from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = ""
# Your Auth Token from twilio.com/console
auth_token  = ""

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+905066129402", 
    from_="+",
    body="BIRAK LAN BERK'I PIC!")

print(message.sid)
