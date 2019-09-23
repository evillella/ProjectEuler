"""
Problem 8
The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.
Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?
"""

file = open('p8data.txt')
rows_str = [line.strip('\n') for line in file]
str = ''
for r in rows_str:
    str += r
#str is string version of the 1000 digit number    

string_list = [str[i:]+str[:i] for i in range(13)]

#str_1 = str[1:]+str[:1]
#str_2 = str[2:]+str[:2]
#str_3 = str[3:]+str[:3]

# for testing, multiply these four strings pointwise into list; max should be the answer
#test_answer = [int(str[i])*int(str_1[i])*int(str_2[i])*int(str_3[i]) for i in range(1000)]

answer_list = []
for i in range(1000):
    a = 1
    for num in string_list:
        a = a*int(num[i])
    answer_list.append(a)
print(max(answer_list))