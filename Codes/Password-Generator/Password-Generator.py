import random
# To generate random password

import time

# To give it some looks

print('Welcome to Pass-Gen\nA basic password generator')
print('-' * 30)

person = input('Your name: ')

print(f'Welcome {person}')
time.sleep(0.25)

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+}{`~"
# all possible characters used in password

print(f"{person} your password can't be lower than 8 and higher than 16")
# Good passwords are between 8 to 16
time.sleep(0.25)

total = int(input('How many passwords do you want to generate?\n>>> '))
time.sleep(0.2)

print(f'You want to generate {total}!')
print('Loading Pass-gen')
time.sleep(2)

pass_list = []

# It stores the passwords generated and later on in the code can be used to make a .txt file of passwords

for num in range(total):
    password = ""
    # Created an empty password variable which resets when the loop  run again

    print('-' * 40)

    pass_len = int(input("Enter your password length\n>>> "))

    if pass_len > 16 or pass_len < 8:
        print("Your pass can't be less than 8 or larger than 16")
        continue

    elif pass_len > 8 or pass_len < 16:
        print('-' * 30)
        print('Generating\nHold on...')

        for i in range(pass_len):
            password += random.choice(characters)
        pass_list.append(password)

        # Added/Appended the password to the empty list created
        time.sleep(0.5)

    else:
        print('You wrote something else!\nRetry')
        continue

save = input('Do you want to save this file as a .txt ?\n(Y)es or (N)o\n>>> ').lower()

if save == 'y':

    with open("passwords.txt", "a+") as file_object:

        # Append creates a new file if not or add the data if already exists

        file_object.seek(0)
        data = file_object.read(100)

        # We did this because in case if you run this again the data would be added but not from new line

        if len(data) > 0:
            file_object.write("\n")
        file_object.write('\n'.join(pass_list))

        # Joined pass_list to convert list -> string

    print('File has been saved in the same directory in which this codd is saved!')

else:
    print(f'Passwords are below-\n{pass_list}')

# Find the passwords.txt file atatched to it!
