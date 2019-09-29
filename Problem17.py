"""
Problem 17
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""

word_dict = dict(zip(['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','30','40','50','60','70','80','90'],
['','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']))

def get_letters(n):
    str_n = str(n)
    if len(str_n)>3:
        #one thousand
        return 11
    elif len(str_n) > 2:
        hund = len(word_dict[str_n[0]])+10 #len(hundred = 7, and = 3)
#        print(word_dict[str_n[0]]+' hundred and ')
        if str_n[-2:] == '00':
            hund = hund-3
    else:
        hund = 0
    #didn't consider case len(str_n) = 1
    if len(str_n)==1:
#        print(word_dict[str_n])
        return len(word_dict[str_n])
    if int(str_n[-2])>1: #tens and ones are standard
#        print(word_dict[str_n[-2]+'0'])
#        print(word_dict[str_n[-1]])
        return hund+len(word_dict[str_n[-2]+'0']) + len(word_dict[str_n[-1]])
    elif int(str_n[-2])<1: #just return ones
#        print(word_dict[str_n[-1]])
        return hund+len(word_dict[str_n[-1]])
    else:#a teen number
#        print(word_dict[str_n[-2:]])
        return hund+len(word_dict[str_n[-2:]])
    
def get_sum(n):
    #returns sum of numbers of letters for all numbers up to n
    tot = 0
    for i in range(1,n+1):
#        print(i)
#        print(get_letters(i))
        tot += get_letters(i)
    return tot

print(get_letters(342)==23)
print(get_letters(115)==20)
print(get_sum(5))