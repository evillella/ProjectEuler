"""
There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, (53)=10.

In general, (nr)=n!r!(n−r)!, where r≤n, n!=n×(n−1)×...×3×2×1, and 0!=1.

It is not until n=23, that a value exceeds one-million: (2310)=1144066.

How many, not necessarily distinct, values of (nr) for 1≤n≤100, are greater than one-million?
"""
from math import log10


def is_choose_greater(n,r):
    """Returns whether (nr) is greater than 1000000"""
    top = set(range(n-r+1,n+1))
    bot = set(range(1,r+1))
    #check whether log(top) - log(bot) > 6
    logtot = 0
    for i in range(1,r+1):
        logtot = logtot + log10(n-r+i) - log10(i)
    return logtot > 6

print(is_choose_greater(23,10))
print(is_choose_greater(22,10))

answer = 0
for n in range(1,101):
    top = int(n/2)
    if 2*top == n:
        if is_choose_greater(n,top):
            answer += 1
        top = top -1
    for i in range(1,top+1):
        if is_choose_greater(n,i):
            answer += 2 #one for i, one for n-i
print('done:',answer)
        