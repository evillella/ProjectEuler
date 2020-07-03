"""
Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
"""


def concat_prod(d,tup):
    ans = ''
    for t in tup:
        ans += str(t*d)
    return int(ans)

print(concat_prod(192,[1,2,3]) == 192384576)
print(concat_prod(9,[1,2,3,4,5]) == 918273645)

largest = 0

for n in range(2,10):
    tup = range(1,n+1)
    d = 1
    prod = concat_prod(d,tup)
    while prod < 1000000000:
        if len(str(prod)) == 9 and len(set(str(prod))-{'0'}) == 9:
               print(prod)
               largest = max(largest, prod)
        d += 1
        prod = concat_prod(d,tup)
print('answer:', largest)
    