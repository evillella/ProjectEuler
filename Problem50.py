"""
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
"""

import math

def show_progress_bar(bar_length, completed, total):
    bar_length_unit_value = (total / bar_length)
    completed_bar_part = math.ceil(completed / bar_length_unit_value)
    progress = "*" * completed_bar_part
    remaining = " " * (bar_length - completed_bar_part)
    percent_done = "%.2f" % ((completed / total) * 100)
    print(f'[{progress}{remaining}] {percent_done}%', end='\r')

bar_length = 30


def is_prime(n,primes):
    for p in primes:
        if n%p == 0:
            return False
    return True

def gen_primes(n):
    primes = {2}
    primesums = [2]
    p = 3
    while p < n:
        show_progress_bar(bar_length, p, n)
        if is_prime(p,primes):
            primes.add(p)
            primesums.append(primesums[-1]+p)
        p+=1
    return primes, primesums

primes, primesums = gen_primes(1000000)
print('primes generated')

def valid_sum_len(n,primesums,primes):
    if primesums[n-1] in primes:
        return True
    l = len(primesums)
    for i in range(l-n):
        if primesums[n+i] - primesums[i] in primes:
            print('n',n,'sum',primesums[n+i]-primesums[i])
            return True
    return False

def binsearch(primesums,primes):
    below = 539
    above = len(primesums)
    for m in range(below,above):
        show_progress_bar(bar_length,below-539,above-539)
        valid = valid_sum_len(m,primesums,primes)
        if valid:
            print('found len:',m)

binsearch(primesums,primes)
        