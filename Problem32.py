"""
Problem 32
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""

def is_pandigital(m,n):
    p = m*n
    string = str(p)+str(m)+str(n)
    if len(string) < 9 or len(string) > 9:
        return False
    else:
        num_dict = {}
        repeated = False
        prod = 1
        for l in string:
            prod = prod * int(l)
            if l in num_dict.keys():
                num_dict[l] += 1
                repeated = True
            else:
                num_dict[l] = 1
        if repeated:
            return False
        elif prod == 0:
            return False
        else:
            return True
        
answer=0
answer_list = []
for m in range(1,10000):
    for n in range(1,10000):
        if is_pandigital(m,n):
            p = m*n
            if p in answer_list:
                pass
            else:
                answer_list.append(p)
                answer+= m*n
            
#for m in range(10,100):
#    for n in range(10,1000):
#        if is_pandigital(m,n):
#            p=m*n
#            if p in answer_list:
#                pass
#            else:
#                answer_list.append(p)
#                answer+=m*n

print(answer) #449061 is wrong