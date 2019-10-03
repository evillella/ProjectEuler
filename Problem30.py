"""
Problem 30
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their
digits
1634 = 1**4 + 6**4 + 3**4 + 4**4
8208 = 8**4 + 2**4 + 0**4 + 8**4
9474 = 9**4 + 4**4 + 7**4 + 4**4
The sum of these numbers is 1634 + 8208 + 9474 = 19316.
Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""

sums_of_powers = 0
for n in range(2,400000):
    n_str = str(n)
    temp_sum = 0
    for l in n_str:
        temp_sum += int(l)**5
    if n == temp_sum:
        sums_of_powers += n
print(sums_of_powers)
        
    