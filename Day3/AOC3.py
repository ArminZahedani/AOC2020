import math
f = open('Day3/AOC3.txt', 'r')
lst = f.readlines()
newLst = []
for element in lst:
    newLst.append(element.replace('\n', ''))
print(newLst)

for i in range(0, len(lst)):
    element = lst[i].replace('\n', '')
    newLst[i] = element * math.ceil(323/3)

pos = 0
index = 0
count = 0
overallProd = count
while pos <= 321:
    pos += 1
    index += 3

    if newLst[pos][index] == '#':
        count += 1
print(count)
count = 0
pos = 0
index = 0
while pos <= 321:
    pos += 1
    index += 1

    if newLst[pos][index] == '#':
        count += 1
overallProd *= count
print(count)
count = 0

pos = 0
index = 0
while pos <= 321:
    pos += 1
    index += 5

    if newLst[pos][index] == '#':
        count += 1
overallProd *= count
print(count)
count = 0

pos = 0
index = 0
while pos <= 321:
    pos += 1
    index += 7
    if newLst[pos][index] == '#':
        count += 1
overallProd *= count
print(count)
count = 0

pos = 0
index = 0
while pos <= 321:
    pos += 2
    index += 1

    if newLst[pos][index] == '#':
        count += 1
overallProd *= count
print(count)
