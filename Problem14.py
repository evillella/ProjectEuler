"""
Problem 14
The following iterative sequence is defined for the set of positive integers:
n → n/2 (n is even)
n → 3n + 1 (n is odd)
Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has
not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
Which starting number, under one million, produces the longest chain?
NOTE: Once the chain starts the terms are allowed to go above one million.
"""

def next_term(n):
    if n%2==0:
        return n/2
    else:
        return 3*n+1
    
length_dict = {1:1}    
    
def get_length(n):
    if n==1:
        return 1
    else:
        next = next_term(n)
        if next in length_dict.keys():
            return length_dict[next]+1
        else:
            return 1+get_length(next)
    
longest_chain_start = 1
chain_length = 1
for i in range(1,1000000):
    len = get_length(i)
    length_dict[i] = len
    if len > chain_length:
        chain_length = len
        longest_chain_start = i
        
print(longest_chain_start)
    