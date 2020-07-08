"""
A googol (10^100) is a massive number: one followed by one-hundred zeros; 100^100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a^b, where a, b < 100, what is the maximum digital sum?
"""
import math

def show_progress_bar(bar_length, completed, total):
    bar_length_unit_value = (total / bar_length)
    completed_bar_part = math.ceil(completed / bar_length_unit_value)
    progress = "*" * completed_bar_part
    remaining = " " * (bar_length - completed_bar_part)
    percent_done = "%.2f" % ((completed / total) * 100)
    print(f'[{progress}{remaining}] {percent_done}%', end='\r')

bar_length = 30


def digit_sum(a,b):
    while a%10 == 0:
        a = int(a/10)
    p = pow(a,b)
    s = str(p)
    tot = 0
    for letter in s:
        tot += int(letter)
    return tot



max_digit_sum = 1

for a in range(1,100):
    for b in range(1,100):
        show_progress_bar(bar_length,(a-1)*100 + b, 10000)
        s = digit_sum(a,b)
        max_digit_sum = max(max_digit_sum, s)
print('done:', max_digit_sum)

