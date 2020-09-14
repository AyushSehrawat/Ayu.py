import time
#  Basic calculator using def

print('Welcome to Basic Calculator')


def addition(num1, num2):
    a = num1 + num2
    print(a)


def subtraction(num1, num2):
    a = num1 - num2
    print(a)


def multiplication(num1, num2):
    a = num1 * num2
    print(a)


def division(num1, num2):
    a = num1 / num2
    print(a)


def square_root(num1):
    a = num1 * 0.5
    print(a)


def square(num1):
    a = num1 ** 2
    print(a)


def error():
    print('Something went wrong! ')


while True:

    print('-'*40)
    choice = input('Please Select One Of The Feature\n1 For basic calculation(+,-,*,/)\n'
                   '2 for Square and square root\n3 for exit\n>>> ')
    time.sleep(1)
    print('-'*40)

    if choice == '1':

        int_1 = float(input('Please Tell Your First Number: '))
        int_2 = float(input('Please Tell Your Second Number: '))

        print('-'*40)
        time.sleep(0.5)

        choice2 = input('Please Select any one\n1 for addition\n2 for subtraction\n'
                        '3 for multiplication\n4 for division\n>>> ')
        time.sleep(0.5)

        if choice2 == '1':
            print('Result: ')
            addition(int_1, int_2)

        elif choice2 == '2':
            print('Result: ')
            subtraction(int_1, int_2)

        elif choice2 == '3':
            print('Result: ')
            multiplication(int_1, int_2)

        elif choice2 == '4':
            print('Result: ')
            division(int_1, int_2)

        else:
            error()

    elif choice == '2':
        print('-'*40)

        int_3 = float(input('Input your number here: '))
        time.sleep(1)

        print('-'*40)

        choice3 = input('Select any one\n1 for squaring\n2 for square root\n>>> ')
        time.sleep(0.5)

        if choice3 == '2':
            print('Result: ')
            square_root(int_3)

        elif choice3 == '1':
            print('Result: ')
            square(int_3)

        else:
            error()

    elif choice == '3':
        print('Thanks for using ')
        print('-'*40)
        break

    else:
        error()

# Defined all first and now the code is in a sorted way!
# The End
