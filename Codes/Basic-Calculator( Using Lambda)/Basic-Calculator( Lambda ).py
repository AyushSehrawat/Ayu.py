import time
#  Basic calculator using lambda

print('Welcome to Basic Calculator')


def error():
    print('Something went wrong! ')         # Just 1 def,for showing error,rest using lambda


while True:

    print('-'*40)
    choice = input('Please Select One Of The Feature\n1 For basic calculation(+,-,*,/)\n'
                   '2 for Square and square root\n3 for exit\n>>> ')
    time.sleep(1)
    print('-'*40)

    if choice == '1':

        int_1 = float(input('Please Tell Your First Number: '))
        int_2 = float(input('Please Tell Your Second Number: '))
        i1 = int_1
        i2 = int_2

        print('-'*40)
        time.sleep(0.5)

        choice2 = input('Please Select any one\n1 for addition\n2 for subtraction\n'
                        '3 for multiplication\n4 for division\n>>> ')
        time.sleep(0.5)

        if choice2 == '1':
            i4 = (lambda x, y: x + y)(i1, i2)
            print(f'\nYour answer is: {i4}')

        elif choice2 == '2':
            i4 = (lambda x, y: x - y)(i1, i2)
            print(f'\nYour answer is: {i4}')


        elif choice2 == '3':
            i4 = (lambda x, y: x * y)(i1, i2)
            print(f'\nYour answer is: {i4}')


        elif choice2 == '4':
            i4 = (lambda x, y: x / y)(i1, i2)
            print(f'\nYour answer is: {i4}')

        else:
            error()

    elif choice == '2':
        print('-'*40)

        int_3 = float(input('Input your number here: '))
        i3 = int_3
        time.sleep(1)

        print('-'*40)

        choice3 = input('Select any one\n1 for squaring\n2 for square root\n>>> ')
        time.sleep(0.5)

        if choice3 == '2':
            i5 = (lambda x: x ** (1/2))(i3)
            print(f'\nYour answer is: {i5}')


        elif choice3 == '1':
            i5 = (lambda x: x ** 2)(i3)
            print(f'\nYour answer is: {i5}')
        else:
            error()

    elif choice == '3':
        print('Thanks for using ')
        print('-'*40)
        break

    else:
        error()
