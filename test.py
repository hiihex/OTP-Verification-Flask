from twilio.rest import Client
from random import randint

ACCOUNT_SID = "twilio sid"
AUTH_TOKEN = "twilio auth token"

twilio_client = Client(ACCOUNT_SID, AUTH_TOKEN)


def generate_send_verification_code(number_to):
    code = (randint(1000, 9999))
    message = twilio_client.messages.create(
        to=number_to,
        from_="+18448310464",
        body=f"Your verification code is: {code}"
    )
    return code


number = input("Input your phone number: ")
check = generate_send_verification_code(number)
check_code = int(input("Input your verification code: "))
if check_code == check:
    print("Verified")
else:
    print("noopee")
