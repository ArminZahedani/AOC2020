import math
f = open('Day13/AOC13.txt', 'r')
lst = f.readlines()
newLst = []
for element in lst:
    buses = element.replace('\n', '').split(',')
    for bus in buses:
        if bus != 'x':
            newLst.append(int(bus))


def silver():
    earliest_time = newLst[0]
    earliest_bus_time = -math.inf
    earliest_bus_id = 0
    for bus in newLst[1:]:
        potential_earliest = (earliest_time % bus) - bus
        if potential_earliest > earliest_bus_time:
            earliest_bus_time = potential_earliest
            earliest_bus_id = bus
    result = earliest_bus_id * abs(earliest_bus_time)
    print(f'Silver star: {result}')


silver()
