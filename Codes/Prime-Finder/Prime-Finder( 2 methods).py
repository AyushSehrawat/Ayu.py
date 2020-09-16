import time

# A simple program to find prime numbers


print('Welcome to Prime-Number finder! ')

time.sleep(0.5)

print('-'*30)


def count_primes(num):
    primes = [2]

    x = 3

    if num < 2:
        return 0

    while x <= num:

        for y in primes:

            if x%y == 0:
                x += 2
                break

        else:
            primes.append(x)
            x += 2

    print(primes)

    print(f'There are: {len(primes)} prime numbers')

prime_find = int(input('Till where do you want to find prime number?\n>>> '))

time.sleep(1)

count_primes(prime_find)


# A same way to do the following problem(Indenation might be wrong)

# def count_primes(num):
 #   primes = [2]
  #  x = 3
  #  if num < 2:  # for the case of num = 0 or 1
   #     return 0
    #while x <= num:
    #    for y in range(3,x,2):  # test all odd factors up to x-1
     #       if x%y == 0:
      #          x += 2
      #          break
       # else:
      #      primes.append(x)
     #       x += 2
    #print(primes)
    #return len(primes)
