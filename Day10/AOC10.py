f = open('Day10/AOC10.txt', 'r')
lst = f.readlines()
newLst = []
for element in lst:
    newLst.append(int(element.replace('\n', '')))
print(newLst)
newLst = sorted(newLst)
one_jolts, three_jolts = 0, 0
previousElement = 0
for element in newLst:
    if element - previousElement == 1:
        one_jolts += 1
    if element - previousElement == 3:
        three_jolts += 1
    previousElement = element
    print(one_jolts, three_jolts)
three_jolts += 1
print("Silver star: {}".format(one_jolts * three_jolts))  # silver

jumps = []
previousElement = 0
for element in newLst:
    jumps.append(element - previousElement)
    previousElement = element
subLst = []
leftPointer, rightPointer = 0, 0
lastseenElement = 3
for i in range(0, len(jumps)):
    element = jumps[i]
    if element == lastseenElement:
        subLst.append(jumps[leftPointer: i])
        leftPointer = i
        lastseenElement = jumps[i-1]
subLst.append(jumps[leftPointer:])

count = 1
for subJmp in subLst:
    if 3 in subJmp:
        continue
    if len(subJmp) == 2:
        count *= 2
    if len(subJmp) == 3:
        count *= 2 ** (len(subJmp) - 1)
    if len(subJmp) == 4:
        count *= 7
print("Gold star: {}".format(count))
