from random import randint


def generate_send_verification_code(client,number_to: str):
    code = (randint(1000, 9999))
    message = client.messages.create(
        to=number_to,
        from_="+18448310464",
        body=f"Your verification code is: {code}"
    )
    return code
