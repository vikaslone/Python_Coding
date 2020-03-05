# COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number
# count_primes(100) --> 25


def count_primes(num1):
    lst = []
    for i in range(2, num1+1):
        cnt = 0
        for j in range(1, i):
            if i % j == 0:
                cnt += 1
        if cnt < 2:
            lst.append(i)
    print(lst)
    return len(lst)


print(count_primes(int(input('Enter Number: '))))


# Alternate code

def count_primes2(num):
    primes = [2]
    x = 3
    if num < 2:
        return 0
    while x <= num:
        for y in primes:  # use the primes list!
            if x % y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)


print(count_primes2(100))
