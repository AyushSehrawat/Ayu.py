import time
# To make it look a bit good

import sys
# For the animation

import collections

# Used to find the repeated characters

a = ['Welcome to the Rep-Finder!']
# Created a list so each work is printed
# If it is made as string than each letter will be printed in a new line (which we don't want)

for chars in a:

    for letters in chars:
        print(letters, end='')
        sys.stdout.flush()
        time.sleep(0.05)
    print('')

name = input('Your name: ')
print(f'Welcome {name}')
time.sleep(0.5)

print('Loading...')
time.sleep(2)

string = input('Please input the line/lines\n>>>  ')
print('\nWait Analyzing...')
time.sleep(5)

frequencies = collections.Counter(string)
repeated_chars = {}
# This empty dictionary stores the word with their frequency


for key, value in frequencies.items():

    if value > 1:
        repeated_chars[key] = value

print(repeated_chars)
print('\n\nIf there is an empty string, it is due to the spaces between words...')

# If you add the lines without spaces you won't see this issue
