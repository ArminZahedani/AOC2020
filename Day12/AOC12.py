import math
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


def gold():
    ship_north_south, ship_east_west = 0, 0
    relative_pos_x, relative_pos_y = 10, 1
    for element in newLst:
        magnitude = int(element[1:])
        if element[0] == 'N':
            relative_pos_y += magnitude
        if element[0] == 'S':
            relative_pos_y -= magnitude
        if element[0] == 'E':
            relative_pos_x += magnitude
        if element[0] == 'W':
            relative_pos_x -= magnitude
        if element[0] == 'F':
            ship_east_west += (relative_pos_x * magnitude)
            ship_north_south += (relative_pos_y * magnitude)

        if element[0] == 'L':
            angle = math.radians(magnitude)
            pos_x = relative_pos_x
            relative_pos_x = round(math.cos(
                angle)) * pos_x - round(math.sin(angle)) * relative_pos_y
            relative_pos_y = round(math.cos(
                angle)) * relative_pos_y + round(math.sin(angle)) * pos_x

        if element[0] == 'R':
            angle = math.radians(magnitude)
            pos_x = relative_pos_x
            relative_pos_x = round(math.cos(angle)) * \
                pos_x + round(math.sin(angle)) * relative_pos_y
            relative_pos_y = -pos_x * \
                round(math.sin(angle)) + relative_pos_y * \
                round(math.cos(angle))
    return ship_north_south, ship_east_west


goldStar = gold()
print(f'Gold star: {abs(goldStar[0]) + abs(goldStar[1])}')
