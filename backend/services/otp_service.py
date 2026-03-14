import random

otp_store = {}


def generate_otp(email: str):

    otp = random.randint(100000, 999999)

    otp_store[email] = otp

    return otp


def verify_otp(email: str, otp: int):

    if email not in otp_store:
        return False

    if otp_store[email] != otp:
        return False

    return True