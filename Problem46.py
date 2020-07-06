"""
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2×1^2
15 = 7 + 2×2^2
21 = 3 + 2×3^2
25 = 7 + 2×3^2
27 = 19 + 2×2^2
33 = 31 + 2×1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
"""

OCs = [9, 15]
primes = [2, 3, 5, 7, 11, 13, 17]
p = 17
dbl_squares = [2, 8, 18]
sn = 4



def is_prime(n,primes):
    for p in primes:
        if n%p == 0:
            return False
    return True

def update1(p, OCs = OCs, primes = primes):
    """ Add to primes, update OCs, return next p """
    next_int = p+2
    while not is_prime(next_int, primes):
        OCs.append(next_int)
        next_int = next_int + 2
    primes.append(next_int)
    return next_int
    
    
def check(oc, primes, dbl_squares, sn):
    """ Returns whether oc is sum of a in primes and b in dbl_squares, sn
    If necessary, updates dbl_squares """
    
    while oc > dbl_squares[-1]:
        dbl_squares.append(2*sn*sn)
        sn += 1
    
    sq_set = set(dbl_squares)
    for p in primes:
        if oc-p in sq_set:
            return False, sn
    return True, sn
        
    



done = False
while not done:
    while len(OCs) == 0:
        p = update1(p)
    
    oc = OCs.pop(0)
    done, sn = check(oc,primes,dbl_squares, sn)
    
print('done:',oc)

