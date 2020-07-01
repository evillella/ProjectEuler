"""
Problem 10
The sum of primes below 10 is 2+3+5+7 = 17.
Find the sum of primes below two million.
"""

primes = []
def find_primes(n):
    #computes list of primes, returns sum
    all_nums = set(range(2,n))
    primes = set()
    while len(all_nums) > 0:
        print('length',len(all_nums))
        i = min(all_nums)
#        print(i,len(all_nums))
        # i is prime, remove i and its multiples
        mults = set([i*n for n in range(1,int(n/i)+1)])
        all_nums = all_nums - mults
        primes.add(i)
    
    #return sum
    sum = 0
    for p in primes:
        sum+= p
    return sum

print(find_primes(10))
print(find_primes(2000000))
            
