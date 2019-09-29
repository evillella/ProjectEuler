"""
Problem 15
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there
are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20×20 grid?
"""

#for 2x2 grid, need two rights (R) and two downs (D), R,R,D,D, in any order. There are choose(4,2) options.

#for 20x20 it's 20 R's and 20 D's, so we have choose(40,20)

def factorial(n):
    if n==1:
        return n
    else: return n*factorial(n-1)
    
print(factorial(40)/(factorial(20))**2)