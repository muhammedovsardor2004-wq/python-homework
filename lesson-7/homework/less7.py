
#1
def is_prime(n):

    b = 2

    while b*b <= n:
        if n % b == 0:
            return f'{n} is not prime'
        b += 1

    return f'{n} is prime'

is_prime(15)

#2

def digit_sum(k):

    summ = 0

    for digits in str(k):
        summ += int(digits)

    return summ

digit_sum(502)

#3
def power2 (n):

    k = 1
    result = []

    while 2**k <= n:
        if 2**k <= n:
            result.append(2**k)

        k += 1

    return result

power2 (100)

