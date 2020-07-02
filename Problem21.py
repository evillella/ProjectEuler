"""
Problem 21
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
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
total = 1999

def d(n):
    divisors = {1}
    d1 = 2
    d2 = int(n/2)
    while d1 < d2:
        if d1*d2 == n:
            divisors.add(d1)
            divisors.add(d2)
        d1 += 1
        d2 = int(n/d1)
    s = 0
    for d in divisors:
        s += d
    return s

print(d(220) == 284)
print(d(284) == 220)

amicable = set()
for a in range(1,10000):
    show_progress_bar(bar_length, a, 10000)
    if a not in amicable:
        b = d(a)
        c = d(b)
        if (a != b) and (c == a) and (b < 10000):
            amicable.add(a)
            amicable.add(b)
tot = 0
for a in amicable:
    tot += a
print(tot)
        