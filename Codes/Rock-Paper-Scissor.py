import random
# Imported random to avoid same choice of computer
import time
# Imported time to make our code look a little good

print('Welcome to Rock,Paper,Scissor game')

name = input('Your name: ')
print(f'Welcome {name}')
turns = int(input('How many turns do you want?\n>>>'))
print(f'{name} choose {turns} turns')

options = ['r', 'p', 's']

marks = []

c_marks = []

total = []

# Created these three empty list to add user , computer's, all choices respectively

# To calculate winner we use marks and c_marks list whereas to show user marks we use marks and total list


# Here we will give user 10 turns
for num in range(turns):
    print('-'*40)
    choice = input('(R)ock,(P)aper or (S)cissor\n1 for exit and 2 for help\n>>>').lower()
    computer = random.choice(options)
    print('-'*40)

# Now we will write all possible conditions and add user & computer decisions
    if choice == computer:
        print('Computer choosing...')
        time.sleep(1)
        print('Tie!')
        marks.append(choice)
        c_marks.append(computer)
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
            c_marks.append(computer)

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
            c_marks.append(computer)

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
            c_marks.append(computer)

    elif choice == '1':
        print(f':( {name} left the game in between')
        break

    elif choice == '2':
        print(f'Hey {name}\n | There are 3 choices for you |\n| (R)ock, (P)aper and (S)cissor |\n| Rock smashes scissor '
              f'but is captured by paper |\n| Paper captures Rock but looses in front of Scissor |\n| Scissor kills '
              f'Paper but '
              f'Rock smashes Scissor |')

    else:
        print('Computer choosing...')
        time.sleep(1)
        print('oops something went wrong')
        total.append(computer)
        c_marks.append(computer)


# Now in the below code we will tell user the marks/his choices/computer choices/exit depending on the input

while True:
    print("~"*30)

    score = input(f'1 - {name} marks\n2 - Show computer wins\n3 - Show {name} wins\n4- Exit\n>>>')

    if score == '1':
        time.sleep(1)
        print(f'You got {len(marks)}/{len(total)}')

        if len(marks) > len(c_marks):
            time.sleep(0.5)
            print(f'{name} won!')

        elif len(marks) == len(c_marks):
            time.sleep(0.5)
            print("It's a tie!")

        else:
            time.sleep(0.5)
            print(f'Computer won! {name} loose!')

    elif score == '2':
        time.sleep(1)
        print(f'Computer got {len(c_marks)} correct \n {c_marks}')
        print('\nIncluding the tie')

    elif score == '3':
        time.sleep(0.5)
        print(f'Your got {len(marks)} correct \n {marks}')
        print('\nIncluding the tie')

    elif score == '4':
        time.sleep(0.5)
        print(f'Bye! Waiting for you {name}')
        break

    else:
        time.sleep(0.5)
        print('Wrong input! Retry')


# Used len(length of list) to find the marks of the user and used the list to show all choices
# The end
