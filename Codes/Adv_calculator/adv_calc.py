import math
from math import sin, cos, tan, pi, asin, acos, atan, log10, sqrt
from statistics import mean, median, mode

# Help Site - https://problemsolvingwithpython.com/03-The-Python-REPL/03.01-Python-as-a-Calculator/
# Help Site - Math module docs - python offcial

print('Welcome to Advanced Calculator\nCopyright - AyushSehrawat (Github)')
print('...................................................................')
# ------------------------------------------------------------------------

# Entry to Maths World
# ____________________________________________________________________________

simple_command = 'Press 1 for Addition\nPress 2 for Subtraction\nPress 3 for Multiplication\nPress 4 for Division'
adv_simple_command = 'Press 5 for Remainder\nPress 6 for Square\nPress 7 for Square root\nPress 8 for specific power(x^y)'
trigo_command = 'Press 9 for Trigonometry commands'
rel_trigo = 'Press 10 for Radian to degree\nPress 11 for Degree to Radian\nPress 12 for Radian to Gradian'
trigo_options = '\nPress 21 for Sin\nPress 22 for Cos\nPress 23 for Tan\nPress 24 for Asin\nPress 25 for Acos\nPress 26 for Atan\n\n'
log_options = 'Press 13 for log of base 10\nPress 14 for log of custom base\nPress 15 for number with base 2'
statsoption = 'Press 16 for mean\nPress 17 for median\nPress 18 for mode'
fact = 'Press 19 for factorial'
exp = 'Press 20 for Exponent'
lcm_hcf = 'Press 30 for lcm\nPress 31 for hcf\nPress 32 for both HCF and LCM\nPress 33 for HCF of decimals'
vctor = 'Press 34 for Vector Length'

# -------------------------------------
main_phy = 'Press 100 to enter physcis world....'
# Under process :)
# --------------------------------------


simple_list = [1,2,3,4]
adv_simple_list = [5,6,7,8]
rel_trigo_list = [10,11,12]
stat_list = [16,17,18]

print(f'\n\n{simple_command}\n\n{adv_simple_command}\n\n{trigo_command}\n\n{rel_trigo}\n\n{log_options}\n\n{statsoption}\n\n{fact}\n\n{exp}\n\n')
print(f'{lcm_hcf}\n\n{vctor}')


def add(x,y):
    print(x+y)


def sub(x,y):
    print(x-y)


def multi(x,y):
    print(x*y)


def divi(x,y):
    print(x/y)


def remain(x,y):
    print(x//y)


def sq(x):
    print(x**2)


def sqroot(x):
    print(math.sqrt(x))


def spec_power(x,y):
    print(x**y)


def rad_to_degree(x):
    print(x*57.2958)


def degree_to_rad(x):
    print(x*0.0174533)


def rad_to_grad(x):
    print(x*63.662)


def _lcm(x, y):
   if x > y:
       greater = x
   else:
       greater = y

   while True:
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   print(lcm)


def _hcf(x, y):
   while(y):
       x, y = y, x % y
   print(x)


def __gcd(a,b) : 
    if (a < b) : 
        return __gcd(b, a) 
      
    if (abs(b) < 0.001) : 
        return a 
    else : 
        return (__gcd(b, a - math.floor(a / b) * b))


def length_vector():
  print("Enter the length of the x coordinate and the length of the y coodinate.")
  x = float(input('X: '))
  y = float(input('Y: '))
  print(f'Your vector is {x},{y}')
  length = sqrt((x**2)+(y**2))
  print(f'Length of vector is {length}')


main_choice = float(input('\nYour Choice: '))

if main_choice in simple_list:
    num1 = float(input('First Number: '))
    num2 = float(input('Second Number: '))

    if main_choice == 1:
        print('_____Answer_____')
        add(num1,num2)
        print('_____Answer_____')

    elif main_choice == 2:
        print('_____Answer_____')
        sub(num1,num2)
        print('_____Answer_____')

    elif main_choice == 3:
        print('_____Answer_____')
        multi(num1,num2)
        print('_____Answer_____')

    elif main_choice == 4:
        print('_____Answer_____')
        divi(num1,num2)
        print('_____Answer_____')

elif main_choice in adv_simple_list:

    if main_choice == 5:
        rem_num = float(input('Number 1: '))
        rem_num2 = float(input('NUmber 2: '))

        print('_____Answer_____')
        remain(rem_num,rem_num2)
        print('_____Answer_____')
    
    elif main_choice == 6 or main_choice == 7:
        sq_num = float(input('Number: '))
        if main_choice == 6:
            print('_____Answer_____')
            sq(sq_num)
            print('_____Answer_____')

        elif main_choice == 7:
            print('_____Answer_____')
            sqroot(sq_num)
            print('_____Answer_____')

    elif main_choice == 8:

        power_num = float(input('Number: '))
        power_power = float(input('Power: '))

        spec_power(power_num,power_power)

elif main_choice in rel_trigo_list:

    if main_choice == 10:

        rad_num = float(input('Radian: '))
        print('_____Answer_____')
        rad_to_degree(rad_num)
        print('_____Answer_____')

    elif main_choice == 11:
        deg_num = float(input('Degree: '))
        print('_____Answer_____')
        degree_to_rad(deg_num)
        print('_____Answer_____')

    elif main_choice == 12:
        rad_to_grad_num = float(input('Radian: '))
        print('_____Answer_____')
        rad_to_grad(rad_to_grad_num)
        print('_____Answer_____')

elif main_choice == 13 or main_choice == 14 or main_choice == 15:

    if main_choice == 13:
        n_log = int(input('Number: '))
        print('____Answer____')
        print(math.log(10,n_log))
        print('____Answer____')

    elif main_choice == 14:
        c_log = int(input('Number: '))
        c_num = int(input('Base: '))
        print('____Answer____')
        print(math.log(c_log,c_num))
        print('____Answer____')

    elif main_choice == 15:
        two_log_num = int(input('Number: '))
        print('____Answer____')
        print(math.log2(two_log_num))
        print('____Answer____')

elif main_choice == 9:

    print(trigo_options)

    trigo_choice = float(input('Your Choice: '))
    val_radian = float(input('Value(In Degree): '))
    val_radia = math.radians(val_radian)

    if trigo_choice == 21:
        print('____Answer____')
        print(sin(val_radia))
        print('____Answer____')

    elif trigo_choice == 22:
        print('____Answer____')
        print(cos(val_radia))
        print('____Answer____')

    elif trigo_choice == 23:
        print('____Answer____')
        print(tan(val_radia))
        print('____Answer____')

    elif trigo_choice == 24:
        print('____Answer____')
        print(asin(val_radia))
        print('____Answer____')

    elif trigo_choice == 25:
        print('____Answer____')
        print(acos(val_radia))
        print('____Answer____')

    elif trigo_choice == 26:
        print('____Answer____')
        print(atan(val_radia))
        print('____Answer____')


elif main_choice in stat_list:
    stat_table = []

    while True:

        stat_nums = float(input('\nPress 000 for exit\nValues:  '))
        if stat_nums == 000:
            break
        else:
            stat_table.append(stat_nums)


    try:
        #
        if main_choice == 16:
            #
            print('____Answer____')
            print(mean(stat_table))
            print('____Answer____')

        elif main_choice == 17:
            #
            print('____Answer____')
            print(median(stat_table))
            print('____Answer____')

        elif main_choice == 18:
            #
            print('____Answer____')
            print(mode(stat_table))
            print('____Answer____')

    except:
        print('Something went wrong :( Terminating...')
    
elif main_choice == 19:
    f_num = int(input('Only natural number\nInput: '))
    if f_num == 0:
        print('____Answer____')
        print('0')
        print('____Answer____')
    elif f_num > 0:
        f_init = 1
        for i in range(1,f_num+1):
            f_init = f_init * i

        print('____Answer____')
        print(f_init)
        print('____Answer____')


elif main_choice == 20:
    exp_num = int(input('Power: '))
    print('____Answer____')
    print(math.exp(exp_num))
    print('____Answer___-')


elif main_choice == 30 or main_choice == 31 or main_choice == 32 or main_choice == 33:
    hl_num1 = float(input('Number 1: '))
    hl_num2 = float(input('Number 2: '))

    if main_choice == 30:
        _lcm(hl_num1,hl_num2)
    elif main_choice == 31:
        _hcf(hl_num1,hl_num2)
    elif main_choice == 32:
        print('\nLCM')
        _lcm(hl_num1,hl_num2)
        print('\n')
        print('HCF/GCD')
        _hcf(hl_num1,hl_num2)
        print('\n')
    elif main_choice == 33:
        temp1 = __gcd(hl_num1,hl_num2)
        print(temp1)
    
elif main_choice == 34:
    length_vector()
