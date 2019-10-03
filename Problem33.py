"""
Problem 33
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
"""

specials = []

def special_fraction(num,denom):
    n1=int(str(num)[0])
    n2=int(str(num)[1])
    d1=int(str(denom)[0])
    d2=int(str(denom)[1])
    if n2+d2==0:
        pass
    elif num*d2 == denom*n1 and n2==d1:
        print(num)
        print(denom)
        specials.append((n1,d2))
    else:
        pass
        
for denom in range(11,100):
    for num in range(11,denom):
        special_fraction(num,denom)
        
print(specials)

#by inspection, solution is 100