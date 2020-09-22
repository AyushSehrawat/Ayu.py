import string
import secrets


def secure_password_gen():
    password = ''.join((secrets.choice(string.ascii_letters) for i in range(10)))
    return password
