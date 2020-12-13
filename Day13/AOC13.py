import math
from sympy.ntheory.modular import crt
f = open('Day13/AOC13.txt', 'r')
lst = f.readlines()
newLst = []
for element in lst:
    buses = element.replace('\n', '').split(',')
    for bus in buses:
        newLst.append(bus)


def silver():
    earliest_time = int(newLst[0])
    earliest_bus_time = -math.inf
    earliest_bus_id = 0
    for bus in newLst[1:]:
        if bus != 'x':
            int_bus = int(bus)
            potential_earliest = (earliest_time % int_bus) - int_bus
            if potential_earliest > earliest_bus_time:
                earliest_bus_time = potential_earliest
                earliest_bus_id = int_bus
    result = earliest_bus_id * abs(earliest_bus_time)
    print(f'Silver star: {result}')


silver()


def gold():
    global newLst
    newLst = newLst[1:]
    nums = [-i for i in range(0, len(newLst)) if newLst[i] != 'x']
    lst_m = [int(element) for element in newLst if element != 'x']
    print(crt(lst_m, nums))


gold()
