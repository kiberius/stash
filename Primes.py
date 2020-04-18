def Main():
    limit = int(input('\nPrime numbers limit:\n'))
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
    print('\nThe sum of all listed primes is {}.\n'.format(primes_sum))
    print('The average of all listed primes is {}.\n'.format(primes_sum/primes_count))
    
Main()
