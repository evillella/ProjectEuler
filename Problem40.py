"""
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
"""

answer = 1
next_list = [1e6, 1e5, 1e4, 1e3, 1e2, 10]
#next_list = [1e4]
position = 1
int_ctr = 1

while len(next_list) > 0:
#    print(position, int_ctr)
    if position + len(str(int_ctr)) <= next_list[-1]:
        position += len(str(int_ctr))
        int_ctr += 1
    else:
        n = next_list.pop()
        assert position <= n
        n = int(n - position)
#        print('n',n,'num',int_ctr)
        d = int(str(int_ctr)[n])
        print(d)
        answer = answer*d
print(answer)
