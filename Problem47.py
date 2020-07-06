"""
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?
"""

primes = {2,3,5,7}
p = 8

def num_factors(n, primes):
    count = 0
    for p in primes:
        if n%p == 0:
            count += 1
    return count

consec = []

while len(consec) < 4:
    n = num_factors(p, primes)
    if n == 0:
        primes.add(p)
        consec = []
    elif n < 4:
        consec = []
    else:
        consec.append(p)
    p += 1

print(consec)
