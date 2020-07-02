"""
Problem 22
Using p22data.txt, a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""

file = open('p22data.txt')
data = ''
for line in file:
    data += line

names = data.strip().split(',')
names = [name.strip('\ "') for name in names]


names.sort()
print(names[0])
print(names[1])


answer = 0


d = {L: i for i, L in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 1)}

def score(name):
    tot = 0
    for letter in name:
        if letter in d:
            tot += d[letter]
        else:
            print('error:',letter, name)
    return tot

print(score('COLIN') == 53)
print(names[937] == 'COLIN')
print(names[937])

for i, name in enumerate(names, 1):
    if i == 938:
        print(name,score(name))
    answer += i*score(name)
    
print(answer)