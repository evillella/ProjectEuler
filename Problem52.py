"""
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
"""

def is_answer(n):
    s = str(n)
    l = len(s)
    collection = set(str(n))
    for i in range(2,7):
        mult = i*n
        if len(str(mult)) != l or collection != set(str(mult)):
            return False
    return True


n = 1
while not is_answer(n):
    n += 1
print(n)