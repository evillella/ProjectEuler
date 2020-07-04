"""
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property.
"""

# generate list of 3-digit numbers divisible by 17
# iterate through remaining smaller primes to add preceding digits with properties

    
divs = [2,3,5,7,11,13]


def gen1():
    """
    Returns a list of "abc"s such that abc is divisible by 17
    """
    ans = []
    for n in range(12,988):
        if (n%17==0):
            if n < 100 and len(set(str(n))-{"0"}) == 2:
                ans.append('0'+str(n))
            elif n > 100 and len(set(str(n))) == 3:
                ans.append(str(n))
    return ans

stack = gen1()
print(stack[:10])
print(len(stack))

def gen_rest(stack):
    primes = [2, 3, 5, 7, 11, 13]
    while len(primes) > 0:
        p = primes.pop()
        new_stack = []
        for s in stack:
            poss = set([str(i) for i in range(10)]) - set(s)
            for d in poss:
                if int(d+s[:2])%p == 0:
                    new_stack.append(d+s)
        stack = new_stack
    return stack
                    
stack = gen_rest(stack)
print(len(stack), stack[0])

total = 0
for s in stack:
    d = (set([str(i) for i in range(10)]) - set(s)).pop()
    total += int(d+s)
print(total)


