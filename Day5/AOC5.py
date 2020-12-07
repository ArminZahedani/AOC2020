f = open('Day5/AOC5.txt', 'r')
lst = f.readlines()
newLst = []
for element in lst:
    newLst.append(element.replace('\n', ''))
print(newLst)
seats = set()

# silver
for element in newLst:
    string = element.replace('F', '0').replace('B', '1')
    print(string)
    row = int(string[:-3], base=2)
    columnStr = string[-3:].replace('L', '0').replace('R', '1')
    column = int(columnStr, base=2)
    seatID = row * 8 + column
    seats.add(seatID)
print(max(seats))

# gold:
allSeats = set([i for i in range(9, 126*8 + 8)])
seatNextTo = set()
for element in allSeats:
    if element - 1 in seats and element + 1 in seats and element not in seats:
        seatNextTo.add(element)
print(allSeats.difference(seatNextTo))
print(seatNextTo)
