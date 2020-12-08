f = open('Day8/AOC8.txt', 'r')
lst = f.readlines()
newLst = []
for element in lst:
    newLst.append(element.replace('\n', ''))
accumulator = 0
seenInstructions = [False]*len(newLst)
index = 0
while True:
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
# print(accumulator)

# Gold:
accumulator = 0


def silver(seenInstructions, index, lst):
    accumulator = 0
    while True:
        if index == len(lst):
            print('success')
            return accumulator
        instruction = lst[index]
        if seenInstructions[index] == True:
            return 0
        seenInstructions[index] = True
        print(instruction)
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
    return accumulator

#silver([False]*len(newLst), 0)


def gold(index, seenInstructions):
    for i in range(0, len(newLst)):
        if element[:3] == 'jmp':
            out = silver([False]*len(newLst), 0, newLst)
            if out != 0:
                print('success')
                print(out)
                break
            lst = newLst.copy()
            lst[i] = 'nop' + element[3:]
            out = silver([False]*len(newLst), 0, lst)
            if out != 0:
                print('success')
                print(out)
                break
        if element[:3] == 'nop':
            silver([False]*len(newLst), 0, newLst)
            if out != 0:
                print('success')
                print(out)
                break
            lst = newLst.copy()
            lst[i] = 'jmp' + element[3:]
            silver([False]*len(newLst), 0, lst)
            if out != 0:
                print('success')
                print(out)
                break


gold(0, [False]*len(newLst))
# 1685 too high
