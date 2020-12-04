f = open('Day2/AOC2.txt', 'r')
lst = f.readlines()
newLst = []
for element in lst:
    element.replace('\n', '')
count = 0

for element in lst:
    string = element.split(':')
    letter = string[0][-1]
    mini = string[0][:-1].split('-')[0]
    maxi = string[0][:-1].split('-')[1]
    if string[1].count(letter) >= int(mini) and string[1].count(letter) <= int(maxi):
        count += 1
print(count)

# new star:
count2 = 0

for element in lst:
    string = element.split(':')
    letter = string[0][-1]
    index1 = int(string[0][:-1].split('-')[0])
    index2 = int(string[0][:-1].split('-')[1])
    if string[1][index1] == letter and string[1][index2] != letter or string[1][index1] != letter and string[1][index2] == letter:
        count2 += 1

print(count2)
