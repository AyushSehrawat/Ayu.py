import random
import time

# User will get 3 inputs and the secret number will be the sum of them.

print('-' * 40)
print('Welcome to SECRET HOUSE')
time.sleep(0.25)
print('You will be given 3 inputs and the secret number is from 3 to 9')
print('If your guess is right then AWESOME or else try again')
time.sleep(0.25)
print('Note your input can be less than 1 and greater than 3')
time.sleep(0.5)
print('-' * 40)

confirm = input("Have you read the instructions?\n(Y)es or (N)o: ")

if confirm == 'Y':
    time.sleep(0.25)
    print('You are good to go')

elif confirm == 'N':

    while True:
        print('-' * 40)
        print('Welcome to SECRET HOUSE')
        print('You will be given 3 inputs and the secret number is between 3 and 9')
        print('If your guess is right then AWESOME or else try again')
        print('Note your input cannot be less than 1 and greater than 3')
        print('-' * 40)

        confirm_2 = input('Have you read the instructions now\n(Y)es or (N)o: ')

        if confirm_2 == 'Y':
            time.sleep(0.25)
            print('You are good to go!')
            break

        elif confirm_2 == 'N':
            continue

secret_number = random.randint(3, 9)

while True:
    print('-' * 40)

    digit_1 = int(input('Guess the first digit from 1 to 3:   '))
    digit_2 = int(input('Guess the second digit from 1 to 3:   '))
    digit_3 = int(input('Guess the third digit from 1 to 3:   '))

    if digit_1 < 1 or digit_1 > 3:
        time.sleep(0.25)
        print('Oops wrong digit chosen')
        break

    elif digit_2 < 1 or digit_2 > 3:
        time.sleep(0.25)
        print('Oops wrong digit chosen')
        break

    elif digit_3 < 1 or digit_3 > 3:
        time.sleep(0.25)
        print('Oops wrong digit chosen')
        break

    elif digit_1 + digit_2 + digit_3 == secret_number:
        time.sleep(0.25)
        print('-' * 40)
        print('Yeah you choose the right number')
        print(f'The secret number was {secret_number}')
        print('Thanks for playing')
        print('Credits - Ayush')
        break

    else:
        print('~' * 40)
        print('Retry!\nRemember sum of these digits should be equal to\nSecret number!')
        time.sleep(0.25)
        print('~' * 40)
        quit_option = (input('Press 2 for continue and anything else for exit:  '))

        if quit_option == '2':
            time.sleep(0.25)
            continue

        else:
            time.sleep(0.25)
            print('Thanks for playing\nCredits-Ayush')
            break
