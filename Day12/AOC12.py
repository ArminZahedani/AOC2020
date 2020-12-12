f = open('Day12/AOC12.txt', 'r')
lst = f.readlines()
newLst = []
for element in lst:
    newLst.append(element.replace('\n', ''))


def silver():
    north_south, east_west = 0, 0
    currentFacing = 90
    for element in newLst:
        magnitude = int(element[1:])
        if element[0] == 'N':
            north_south += magnitude
        if element[0] == 'S':
            north_south -= magnitude
        if element[0] == 'E':
            east_west += magnitude
        if element[0] == 'W':
            east_west -= magnitude
        if element[0] == 'R':
            currentFacing += magnitude
            currentFacing = currentFacing % 360
        if element[0] == 'L':
            currentFacing -= magnitude
            currentFacing = currentFacing % 360
        if element[0] == 'F':
            if currentFacing == 0:
                north_south += magnitude
            if currentFacing == 90:
                east_west += magnitude
            if currentFacing == 180:
                north_south -= magnitude
            if currentFacing == 270:
                east_west -= magnitude
    return north_south, east_west


silverStar = silver()
print(f'Silver star: {abs(silverStar[0]) + abs(silverStar[1])}')
