f = open('Day8/AOC8.txt', 'r')
lst = f.readlines()
newLst = []
for element in lst:
    newLst.append(element.replace('\n', ''))
print(newLst)
accumulator = 0
seenInstructions = [False]*len(newLst)
index = 0
while True:
    print(index)
    instruction = newLst[index]
    if seenInstructions[index] == True:
        break
    seenInstructions[index] = True
    if instruction[:3] == 'jmp':
        if '+' in instruction:
            index += int(instruction.split('+')[1])
        if '-' in instruction:
            index -= int(instruction.split('-')[1])
    if instruction[:3] == 'acc':
        if '+' in instruction:
            accumulator += int(instruction.split('+')[1])
        if '-' in instruction:
            accumulator -= int(instruction.split('-')[1])
        index += 1
    if instruction[:3] == 'nop':
        index += 1
print(accumulator)
