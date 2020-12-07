import json
from string import ascii_lowercase
f = open('Day6/AOC6.txt', 'r')
lst = f.readlines()
newLst = []
print(lst)
for element in lst:
    newLst.append(element.replace('\n', ''))
count = 0
se = set()
lastN = 0
new1Lst = []
for i in range(0, len(lst)):
    if lst[i] == '\n':
        new1Lst.append(''.join(lst[lastN: i]).replace('\n', ''))
        lastN = i
    if i == len(lst) - 1:
        new1Lst.append(''.join(lst[lastN:]).replace('\n', ''))
print(new1Lst)

count = 0
for element in new1Lst:
    seen = set()
    for char in element:
        if char not in seen:
            seen.add(char)
            count += 1
print(count)

lastN = 0
new2Lst = []
for i in range(0, len(lst)):
    if lst[i] == '\n':
        new2Lst.append(','.join(lst[lastN: i]).replace('\n', ''))
        lastN = i
    if i == len(lst) - 1:
        new2Lst.append(','.join(lst[lastN:]).replace('\n', ''))
# print(new2Lst)
count2 = 0
for element in new2Lst:
    people = element.split(',')
    people = [x for x in people if x != '']
    print(people)
    countLetters = {}
    for string in people:
        seen = set()
        for char in string:
            if char not in countLetters:
                countLetters[char] = 0
            if char not in seen:
                countLetters[char] += 1
                seen.add(char)
    for char in countLetters:
        print('number of times letter', char, 'occured', countLetters[char])
        if countLetters[char] == len(people):
            count2 += 1
            print('counted', people)

print(count2)

# not 26
