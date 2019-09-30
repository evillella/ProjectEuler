"""
Problem 16
2^{15} = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 2^{1000}?
"""

n= 2**1000
tot = 0
s = str(n)
for d in s:
    tot += int(d)
    
print(tot)