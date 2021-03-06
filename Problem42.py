"""
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?
"""

file = open('p42.txt')
rows_str = [line.strip('\n') for line in file]
words = rows_str[0].split(',')
words = [word.strip('"') for word in words]

triangles = {1,3,6}
n = 3
Tn = 6

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
let_dict = {alphabet[i-1]:i for i in range(1,27)}

num_triangle_words = 0

for word in words:
    score = sum([let_dict[l] for l in word])
    while score > Tn:
        n += 1
        Tn = int(n*(n+1)/2)
        triangles.add(Tn)
    if score in triangles:
        num_triangle_words += 1
print('answer:', num_triangle_words)
        