f = open('AOC1.txt', 'r')
lst = f.readlines()
for element in lst:
    element.replace('\n', '')

for element in lst:
    for element2 in lst:
        if int(element) + int(element2) == 2020:
            print(int(element) * int(element2))

for element in lst:
    for element2 in lst:
        for element3 in lst:
            if int(element) + int(element2) + int(element3) == 2020:
                print(int(element) * int(element2) * int(element3))
