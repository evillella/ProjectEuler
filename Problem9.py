"""
Problem 9
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a^2 + b^2 = c^2.
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

triples = []
for a in range(1,500):
    for b in range(1,500):
        c = 1000-a-b
        if c*c == a*a + b*b:
            triples.append((a,b,c))
            
#print(triples)
answer = triples[0]
print(answer[0]*answer[1]*answer[2])