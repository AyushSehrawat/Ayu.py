import random

print('\nWelcome to Hangman :)\nAuthor - AyushSehrawat(Github)')
print('-------------------------------\n')

# ------------------------------------------------------------------------------------------------------------
word_list = {'windows':'A big project by microsoft', 'linux':'Free operating system', 'apple':'Unix based os'}
g_list = ['windows','linux','apple']

g_word = random.choice(g_list)
# -------------------------------------------------------------------------------------------------------------

print('\nHere is your hint to find the word :)')
print(f'\n -------> \n | {word_list[g_word]} |\n')
print('You got max 10 guesses!')

guesses = 10
rights = 1

while guesses > 0:
    t_len = len(g_word)
    print(f'\nThe word is of {t_len} letters.\n')
    u_word = input('\nWord: ').lower()
    if u_word == g_word:
        print('\nYou won!\n')
        print(f'\nYou guessed it in {rights} turns\n')
        break
    else:
        print('Wrong :(')
        guesses = guesses -1
        rights = rights + 1
        
        
    