"""
Problem 27
Euler discovered the remarkable quadratic formula:

n**2+n+41
It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39. However, when n=40,402+40+41=40(40+1)+41 is divisible by 41, and certainly when n=41,412+41+41 is clearly divisible by 41.

The incredible formula n**2−79n+1601 was discovered, which produces 80 primes for the consecutive values 0≤n≤79. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n2+an+b, where |a|<1000 and |b|≤1000

where |n| is the modulus/absolute value of n
e.g. |11|=11 and |−4|=4
Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0.
"""

primes = {2,3,5,7}
max_checked = 7

def is_prime(n):
    global max_checked
    if n <= max_checked:
        return n in primes
    else:
        while n > max_checked:
            max_checked += 1
            # figure out whether max_prime
            is_prime = True
            for p in primes:
                d = int(max_checked/p)
                if d*p == max_checked:
                    is_prime = False
            if is_prime:
                primes.add(max_checked)
        return n in primes
    
def num_primes(a,b):
    n = 0
    while is_prime(n*(n+a)+b):
        n+=1
    return n-1

import math

def show_progress_bar(bar_length, completed, total):
    bar_length_unit_value = (total / bar_length)
    completed_bar_part = math.ceil(completed / bar_length_unit_value)
    progress = "*" * completed_bar_part
    remaining = " " * (bar_length - completed_bar_part)
    percent_done = "%.2f" % ((completed / total) * 100)
    print(f'[{progress}{remaining}] {percent_done}%', end='\r')

bar_length = 30
total = 1999
#sample use:
#for i in range(0, total + 1):
#    show_progress_bar(bar_length, i, total)

def solution():
    max_n = 0
    prod_ab = 0
    for a in range(-999,1000,1):
        for b in range(-1000,1001,1):
            show_progress_bar(bar_length, a+999, total)
            n = num_primes(a,b)
            if n > max_n:
                print(n,a,b)
                max_n = n
                prod_ab = a*b
    return prod_ab
            
            
if __name__ == "__main__":
    print(is_prime(25))
    print(is_prime(37))
    print(primes)
    
    print(solution())
            