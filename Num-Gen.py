import random
import time

num_list = []
area_code = [555, 205, 251, 256, 334, 938, 907, 480, 480, 520, 602, 623, 928, 479, 209, 213, 279, 530, 562, 925, 303,
             203, 302, 305, 808, 208, 217, 319, 316, 270, 225, 781, 810, 763, 406, 308]
print('Welcome to Num gen\nProud to present Num gen')
val = int(input('How many number do you want to generate\n>> '))
print('Can only generate USA and Indian Numbers')
country = input('Type Us for USA and In for Indian number\n>>: ').lower()
print(f'Generating {country.upper()} numbers')
if country == 'us':
    for num in range(val):
        number = f'({random.choice(area_code)})-{random.randint(600, 800)}-{random.randint(4000, 9999)}'
        print(f'Number generated: {number}')
        time.sleep(2)
        num_list.append(number)
elif country == 'in':
    for num in range(val):
        number = f' +91 -{random.randint(7000000000, 9999999999)}'
        print(f'Number generated: {number}')
        num_list.append(number)

print('_' * 40)

while True:
    total = input('Press 1 to show all generated numbers\nPress 2 to show total generated numbers\nPress anything to '
                  'exit\n>>>  ')
    if total == '1':
        print(f'Numbers generated are -\n{num_list}')
        continue
    elif total == '2':
        print(f'Numbers generated are {len(num_list)}')
        continue
    else:
        break
