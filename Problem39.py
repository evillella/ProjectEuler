"""
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
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
#sample use:
#for i in range(0, total + 1):
#    show_progress_bar(bar_length, i, total)

def get_pairs(p, hyp):
    pairs = set()
    for i in range(1,int((p-hyp)/2)+1):
        j = p - hyp - i
        if i*i + j*j == hyp*hyp:
            pairs.add((i,j))
    return pairs
            


def get_num_solutions(p):
    """ Returns the number of distinct triples which are sides of right triangle with perimeter p"""
    solns = set()
    for hyp in range(int(p/3),p-1):
        pairs = get_pairs(p,hyp)
        for pair in pairs:
            M = max(pair)
            m = min(pair)
            if hyp >= M:
                solns.add((hyp,M,m))
    return len(solns)
        


num_solutions = 0
best_p = 0
for p in range(3,1001):
    show_progress_bar(bar_length, p-2, 999)
    solns = get_num_solutions(p)
    if solns > num_solutions:
        num_solutions = solns
        best_p = p
print(best_p)