"""
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
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


def get_primes(n):
    nums = set(range(2,n))
    primes = set()
    while len(nums) > 0:
        p = min(nums) #is prime
#        print(p, nums, primes)
        show_progress_bar(bar_length, p, n)
        primes.add(p)
        nums = nums - set([p*i for i in range(1,int(n/p)+1)])
    return primes

print(get_primes(10))
print(get_primes(50))

def get_shifts(num):
    s = str(num)
    l = len(s)
    answer = []
    while l > 1:
        s = s[1:] + s[0]
        answer.append(int(s))
        l -= 1
    return answer

print(get_shifts(32))
print(get_shifts(2362))

primes = get_primes(1000000)
print('primes initialized')

count = 0

for p in primes:
    shifts = get_shifts(p)
    all_prime = True
    for n in shifts:
        if n not in primes:
            all_prime = False
    if all_prime:
        count += 1
print(count)


