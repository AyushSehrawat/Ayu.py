"""The secrets module is used for generating cryptographically strong random numbers suitable for managing data such
as passwords, account authentication, security tokens, and related secrets. """
import string
import secrets
import time
from pathlib import Path


secure_pass_list = []


def secure_password_gen(passlength):
    password = ''.join((secrets.choice(string.ascii_letters) for i in range(passlength)))
    return password


print('Welcome To secure Pass-Gen!\nGenerate unique random password!')

pass_length = int(input('Enter length of password : '))

pass_number = int(input('How many passwords?\n>>> '))

for num in range(pass_number):
    secure_password = secure_password_gen(pass_length)
    secure_pass_list.append(secure_password)
    print(f'Password generated is : {secure_password}')
    time.sleep(1 / 4)

save = input('Do you want to save it?\n(Y)es or (N)o\n>>> ').upper()

if save == 'Y':
    with open("secure-passwords.txt", "a+") as file:
        data = Path('secure-passwords.txt').stat().st_size
        file.write('\nPassword-Generated: ') if data else file.write('Password-Generated: ')
        file.write('\nPassword-Generated: '.join(secure_pass_list))
        print('Check the same directory where this script is saved! ')
else:
    print('Thanks for using!')
