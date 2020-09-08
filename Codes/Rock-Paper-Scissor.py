import random
# Imported random to avoid same choice of computer
import time
# Imported time to make our code look a little goos

print('Welcome to Rock,Paper,Scissor game')

name = input('Your name: ')
turns = int(input('How many turns do you want?\n>>>'))

options = ['r', 'p', 's']

marks = []

total = []

# Created these two empty list to add user and computer choice respectively and calculate the marks


# Here we will give user 10 turns
for num in range(turns):
    choice = input('(R)ock,(P)aper or (S)cissor\n1 for exit\n>>>').lower()
    computer = random.choice(options)

# Now we will write all possible conditions and add user & computer decisions
    if choice == computer:
        print('Computer choosing...')
        time.sleep(1)
        print('Tie!')
        marks.append(choice)
        total.append(computer)

    elif choice == 'r':

        if computer == 's':
            print('Computer choosing...')
            time.sleep(1)
            print(f'{name} won!')
            marks.append(choice)
            total.append(computer)

        else:
            print('Computer choosing...')
            time.sleep(1)
            print('Oops computer won!')
            total.append(computer)

    elif choice == 'p':

        if computer == 'r':
            print('Computer choosing...')
            time.sleep(1)
            print(f'{name} won!')
            marks.append(choice)
            total.append(computer)

        else:
            print('Computer choosing...')
            time.sleep(1)
            print('Oops computer won!')
            total.append(computer)

    elif choice == 's':

        if computer == 'p':
            print('Computer choosing...')
            time.sleep(1)
            print(f'{name} won')
            marks.append(choice)
            total.append(computer)

        else:
            print('Computer choosing...')
            time.sleep(1)
            print('Oops computer won!')
            total.append(computer)

    elif choice == '1':
        print(f':( {name} left the game in between')
        break

    else:
        print('Computer choosing...')
        time.sleep(1)
        print('oops something went wrong')
        total.append(computer)


# Now in the below code we will tell user the marks/his choices/computer choices/exit depending on the input

while True:
    print('-'*30)

    score = input(f'1 - {name} marks\n2 - Show computer choices\n3 - Show {name} choice\n4- Exit\n>>>')

    if score == '1':
        time.sleep(1)
        print(f'You got {len(marks)}/{len(total)}')

        if len(marks) > len(total):
            time.sleep(0.5)
            print(f'{name} won!')

        elif len(marks) == len(total):
            time.sleep(0.5)
            print("It's a tie!")

        else:
            time.sleep(0.5)
            print(f'Computer won! {name} loose!')

    elif score == '2':
        time.sleep(1)
        print(f'Computer choices are \n {total}')

    elif score == '3':
        time.sleep(0.5)
        print(f'Your choices are \n {marks}')

    elif score == '4':
        time.sleep(0.5)
        print(f'Bye Bye {name}')
        break

    else:
        time.sleep(0.5)
        print('Wrong input! Retry')

# The end
