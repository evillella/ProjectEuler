"""
The number 145 is well known for the property that the sum of the factorial of its digits is equal to 145:

1! + 4! + 5! = 1 + 24 + 120 = 145

Perhaps less well known is 169, in that it produces the longest chain of numbers that link back to 169; it turns out that there are only three such loops that exist:

169 → 363601 → 1454 → 169
871 → 45361 → 871
872 → 45362 → 872

It is not difficult to prove that EVERY starting number will eventually get stuck in a loop. For example,

69 → 363600 → 1454 → 169 → 363601 (→ 1454)
78 → 45360 → 871 → 45361 (→ 871)
540 → 145 (→ 145)

Starting with 69 produces a chain of five non-repeating terms, but the longest non-repeating chain with a starting number below one million is sixty terms.

How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?
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
total = 1000000
#sample use:
#for i in range(0, total + 1):
#    show_progress_bar(bar_length, i, total)

factorial = {}
factorial[0] = 1
for i in range(1,10):
    factorial[i] = i*factorial[i-1]
    
def get_chain(n):
    """ Returns a set containing all values seen by the chain starting at n"""
    chain = set()
    node = n
    while node not in chain:
        chain.add(node)
        s = str(node)
        node = 0
        for letter in s:
            node += factorial[int(letter)]
    return chain

below = set()
equals_60 = set()

def count_chains(below, equals_60):
    for i in range(1000000):
        show_progress_bar(bar_length, i, total)
        if i in below or i in equals_60:
            pass
        else:
            #look at chain starting with i
            chain = get_chain(i)
            if len(chain) == 60:
                equals_60.add(i)
                below = below.union(chain)
                below = below - {i}
            else:
                below = below.union(chain)
    return len(equals_60)


if __name__ == "__main__":
    print(count_chains(below, equals_60))