"""
The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
"""

def fast_pow(a,b):
    """ More quickly computes a^b mod 10000000000 """
    s = bin(b)[2:]
    ans = 1
    tmp = a
#    print(s)
    for i in range(len(s)):
        if s[-1-i] == '1':
            ans = ans * tmp 
        tmp = tmp*tmp
    return ans
        
    


n = 1
ans = 0
while n < 1001:
    ans = (ans + fast_pow(n,n) % 10000000000)
    n += 1
print(ans)