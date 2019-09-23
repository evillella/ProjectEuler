"""
Problem 10
The sum of primes below 10 is 2+3+5+7 = 17.
Find the sum of primes below two million.
"""

primes = []
def find_primes(n):
    #computes list of primes, returns sum
    for i in range(2,n+1):
        #check whether it's prime
        is_prime = True
        for p in primes:
            if int(i/p)*p == i:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    #return sum
    sum = 0
    for p in primes:
        sum+= p
    return sum

print(find_primes(10))
print(find_primes(2000000))
            
