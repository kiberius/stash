def Input():
    global limit
    try:
        limit = int(input('\nPrime numbers limit: '))
        Main()
    except ValueError:
        print('\nYou must enter an interger.')
        Input()
    except:
        Input()

def Main():
    primes_sum = 0
    primes_count = 0
    for num in range(limit):
        if num > 1:
            for i in range(2,num):
                if (num % i) == 0:
                    break
            else:
                print(num)
                primes_sum += num
                primes_count += 1
    print(f'\nThe number of primes is {primes_count}.\n')
    print(f'The sum of all listed primes is {primes_sum}.\n')
    print(f'The average of all listed primes is {primes_sum/primes_count}.\n')
Input()
