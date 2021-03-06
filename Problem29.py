"""
Problem 29
Consider all integer combinations of a**b for 2 ≤ a ≤ 5 and 2 ≤ b ≤ 5:

2**2=4,  2**3=8,   2**4=16,  2**5=32
3**2=9,  3**3=27,  3**4=81,  3**5=243
4**2=16, 4**3=64,  4**4=256, 4**5=1024
5**2=25, 5**3=125, 5**4=625, 5**5=3125
If they are then placed in numerical order, with any repeats removed, we get the following sequence of 15 distinct terms:

4, 8, 9, 16, 25, 27, 32, 64, 81, 125, 243, 256, 625, 1024, 3125

How many distinct terms are in the sequence generated by ab for 2 ≤ a ≤ 100 and 2 ≤ b ≤ 100?
"""

#all_terms = [[a**b for a in range(2,6)] for b in range(2,6)]

import math

def show_progress_bar(bar_length, completed, total):
    bar_length_unit_value = (total / bar_length)
    completed_bar_part = math.ceil(completed / bar_length_unit_value)
    progress = "*" * completed_bar_part
    remaining = " " * (bar_length - completed_bar_part)
    percent_done = "%.2f" % ((completed / total) * 100)
    print(f'[{progress}{remaining}] {percent_done}%', end='\r')

bar_length = 30
total = 99
#sample use:
#for i in range(0, total + 1):
#    show_progress_bar(bar_length, i, total)

visited = set()

for a in range(2,101):
    for b in range(2,101):
        show_progress_bar(bar_length, a-1, total)
        n = a**b
        visited.add(n)

print(len(visited))

