"""
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

primes = {2,3,5,7}
p = 8
tot = 0
num_found = 0


def truncatable(p, primes):
    s = str(p)
    ans = True
    left = s[1:]
    right = s[:-1]
    while len(left) > 0:
        if int(left) not in primes or int(right) not in primes:
            ans = False
        left = left[1:]
        right = right[:-1]
    return ans

def is_prime(n, primes):
    for p in primes:
        if n % p == 0:
            return False
    return True



while num_found < 11:
    if is_prime(p, primes):
        primes.add(p)
        if truncatable(p, primes):
            num_found += 1
            tot += p
            print(p)
    p += 1
print('answer:', tot)
    
    