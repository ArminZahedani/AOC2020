f = open('Day9/AOC9.txt', 'r')
lst = f.readlines()
newLst = []
for element in lst:
    newLst.append(int(element.replace('\n', '')))

runningIndex = 0
for number in newLst[25:]:
    sentinel = False
    for candidate1 in newLst[runningIndex: runningIndex+25]:
        for candidate2 in newLst[runningIndex: runningIndex+25]:
            if number == candidate1 + candidate2:
                sentinel = True
    if not sentinel:
        print(number)
        break
    runningIndex += 1

target = 507622668

for index in range(0, len(newLst)):
    for index2 in range(index, len(newLst)):
        potentialSet = newLst[index:index2]
        if sum(potentialSet) == target:
            print('min + max of the set is {}'.format(
                min(potentialSet) + max(potentialSet)))
