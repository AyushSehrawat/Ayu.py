import random
# For shuffling
from time import sleep

# Just to make it a bit good

print('Welcome to Mad Libs Generator!')

story_words = []
# Empty list which stores the words for making story

name = input('Your name: ')

print(f'Welcome {name}')
sleep(0.2)

while True:
    words = input('Need words for your story\n Type 00 for exit\n>>> ')

    if words == '00':
        print('Making a useless story...\nWait')
        sleep(3)
        break

    else:
        print('-' * 30)
        print('Word added!')
        story_words.append(words)
        continue

random.shuffle(story_words)
random.shuffle(story_words)
random.shuffle(story_words)

# Shuffled the list so no word is left
# Shuffled it thrice ( so the way user input the words is less matchable with the story)

print(f'Just complete...')

for i in range(5, 0, -1):
    sleep(1)
    print(f'{i}..')
sleep(2)
# Just some animations

print(*story_words)

# Used * in print function
# As it is used for unpacking a tuple or list
# For more informating find the readme.md attached to it
