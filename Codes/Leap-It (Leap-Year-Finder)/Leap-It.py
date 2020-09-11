# Just a simple beginner's script for finding leap year
# Leap-It!

print('Welcome to Leap-It\nMost accurate Leap Year finder! ')

print('-'*30)

name = input('Your name: ')

print('-'*30)


year = int(input("Enter a year: "))
print('-'*30)


if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print("{0} is a leap year".format(year))
        else:
            print("{0} is not a leap year".format(year))
    else:
        print("{0} is a leap year".format(year))
else:
    print("{0} is not a leap year".format(year))


print('-' * 30)

print(f'Thanks for using Leap-It - {name} ')
