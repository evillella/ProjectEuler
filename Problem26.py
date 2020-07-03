"""
Problem 26
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""

def step(num,div):
    """ Computes num/div to one place, returns answer, remainder."""
    ans = int(num/div)
    r = num - ans*div
    return ans, r

def get_decimal(a,b):
    """Returns list of decimals in a/b, whether repeats."""
    ans = []
    ans_set = set()
    num, r = step(a,b)
    repeat = False
    while (r != 0) and (not repeat):
        num, r = step(10*r,b)
        ans.append((num,r))
        if (num, r) in ans_set:
            repeat = True
        ans_set.add((num,r))
    return ans, repeat

def get_cycle_length(decimal):
    # decimal[-1] appears somewhere else
    r = decimal[-1]
    for i in range(1,len(decimal)):
        if decimal[-1-i] == r:
            return i
    return -1

print(get_decimal(1,2))
print(get_decimal(1,6))
print(get_cycle_length([3, 3]) == 1)
print(get_cycle_length([1, 6, 1]) == 2)

cycle_len = 0
best_d = 0

for d in range(1,1000):
    dec, repeat = get_decimal(1,d)
    if repeat:
        #get cycle length
        l = get_cycle_length(dec)
        if l > cycle_len:
            cycle_len = l
            best_d = d
            print(d,l)
print("done")
    
        