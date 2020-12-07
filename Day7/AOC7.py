import json
from string import ascii_lowercase
f = open('Day7/AOC7.txt', 'r')
lst = f.readlines()
newLst = []
for element in lst:
    newLst.append(element.replace('\n', '').replace('.', ''))
dic = {}
for element in newLst:
    key = element.split('contain')
    lst = [x.lstrip() for x in key[1].split(',')]
    dic[key[0].rstrip()] = lst

count = 0
seen = set()
print(newLst)
print(dic)
# silver


def recursive(bag):
    global count
    print(bag)
    for key in dic.keys():
        if bag[:-1] in ''.join(dic[key]):
            if key not in seen:
                seen.add(key)
                count += 1
                recursive(key)


#recursive('shiny gold')
# print(count)
# print(len(seen))

# gold
count = 0


def recursive(bag):
    lineCounter = 0
    bag = bag.lstrip()
    result = 0
    for key in dic.keys():
        if bag in key:
            for bags in dic[key]:
                print(bags)
                if bags == 'no other bags':
                    return 1
                lineCounter += 1
                rs = recursive(bags[1:])
                result += int(bags[0]) * rs
                print(result)
    return result + 1


print(recursive('shiny gold') - 1)
