"""
Problem 28
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""

#look at it as a sum of boxes of increasing sizes,
#1,3x3,5x5,etc until 1001x1001

diag_sum = 1
counter = 2

for i in range(3,1002,2):
    perim = 4*(i-1)
    counter = counter + perim
    diag_sum = diag_sum + 4*counter-6*i+2

print(diag_sum)