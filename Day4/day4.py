import json
f = open('Day4/input', 'r')
lst = f.readlines()
newLst = []
print(lst)
for element in lst:
    newLst.append(element.replace('\n', ''))
count = 0
se = set()
lastN = 0
new1Lst = []
for i in range(0, len(lst)):
    if lst[i] == '\n':
        new1Lst.append(''.join(lst[lastN: i]))
        lastN = i
    if i == len(lst) - 1:
        new1Lst.append(''.join(lst[lastN:]))
print(new1Lst)

count2 = 0
for element in new1Lst:
    found = []
    for field in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']:
        if element.find(field) != -1:
            found.append(True)
        if element.find(field) == -1:
            found.append(False)
    if (all(found)):
        count += 1
        nearlyDict = element.replace('\n', ' ')
        elements = nearlyDict.strip().split(' ')
        found2 = []
        for element2 in elements:
            for field in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']:
                if element2.find(field) != -1:
                    val = element2.split(':')[1]
                    if element2.split(':')[0] == 'byr':
                        if int(val) <= 2002 and int(val) >= 1920:
                            found2.append(True)
                        else:
                            found2.append(False)
                    if element2.split(':')[0] == 'iyr':
                        if int(val) <= 2020 and int(val) >= 2010:
                            found2.append(True)
                        else:
                            found2.append(False)
                    if element2.split(':')[0] == 'eyr':
                        if int(val) <= 2030 and int(val) >= 2020:
                            found2.append(True)
                        else:
                            found2.append(False)
                    if element2.split(':')[0] == 'hgt':
                        if val[-2:] == 'cm' and int(val[:-2]) >= 150 and int(val[:2]) <= 193:
                            found2.append(True)
                        elif val[-2:] == 'in' and int(val[:-2]) >= 59 and int(val[:2]) <= 76:
                            found2.append(True)
                        else:
                            found2.append(False)
                    if element2.split(':')[0] == 'hcl':
                        if val[0] == '#':
                            try:
                                newVal = int(val[1:], base=16)
                                found2.append(True)
                            except ValueError:
                                found2.append(False)
                    if element2.split(':')[0] == 'ecl':
                        if val in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                            found2.append(True)
                        else:
                            found2.append(False)
                    if element2.split(':')[0] == 'pid':
                        if len(val) == 9:
                            found2.append(True)
                        else:
                            found2.append(False)

            if found2 == [] or len(found2) != 7:
                continue
            elif(all(found2)):
                count2 += 1
                se.add(str(elements))


print(count2)
print(len(se))
