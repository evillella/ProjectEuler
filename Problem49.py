"""
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
"""

primes = {2,3,5,7}
n = 8

def is_prime(n,primes):
    for p in primes:
        if n%p == 0:
            return False
    return True

def get_perms(n):
    """Return list of all permutations of 4-digit number n"""
    s = str(n)
    if len(s) < 4:
        return []
    stack1 = [s[0]+s[1],s[1]+s[0]]
    stack2 = []
    for pair in stack1:
        stack2.append(s[2]+pair)
        stack2.append(pair[0]+s[2]+pair[1])
        stack2.append(pair+s[2])
    stack3 = []
    for trip in stack2:
        stack3.append(s[3]+trip)
        stack3.append(trip[0]+s[3]+trip[1:])
        stack3.append(trip[:2] + s[3] + trip[2])
        stack3.append(trip+s[3])
    return [int(s) for s in stack3]



def get_triple(perms):
    """If found, returns triple which make up arithmetic sequence"""
    perms.sort()
    for i, n1 in enumerate(perms[:-1]):
        for n2 in perms[i+1:]:
            if n2 > n1 and n2 + n2 - n1 in perms:
                return str(n1)+str(n2)+str(2*n2-n1)


while n < 10000:
    if is_prime(n,primes):
        primes.add(n)
    n += 1
    
# remove primes below 1000, for valid primes check whether perms are in group
sets = []
for p in primes:
    if p > 999:
        perms = get_perms(p)
        perms = [q for q in perms if q in primes and q > 999]
        if len(perms) >2:
            print(get_triple(perms))
#            print(perms)
            
