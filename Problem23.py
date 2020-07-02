"""
Problem 23
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""


def is_abundant(n):
    divisors = {1}
    d1 = 2
    d2 = int(n/2)
    while d1 <= d2:
        if d1*d2 == n:
            divisors.add(d1)
            divisors.add(d2)
        d1 += 1
        d2 = int(n/d1)
    tot = 0
    for d in divisors:
        tot += d
    return tot > n

def fill_abundants():
    abundant = set()
    for i in range(1,28123):
        if is_abundant(i):
            abundant.add(i)
    return abundant


abundant = fill_abundants()
abundant = list(abundant)
abundant.sort()

def is_sum_of_abundants(n, abundant = abundant):
    ind1 = 0
    ind2 = len(abundant)-1
    while ind1 <= ind2:
        if abundant[ind1] + abundant[ind2] == n:
            return True
        elif abundant[ind1] + abundant[ind2] < n:
            ind1 += 1
        else:
            ind2 -= 1
    return False



answer = 0
for i in range(28294):
    if not is_sum_of_abundants(i):
        answer += i
print(answer)
