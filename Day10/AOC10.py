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
print(one_jolts * three_jolts)
