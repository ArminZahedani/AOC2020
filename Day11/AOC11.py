import copy
f = open('Day11/AOC11.txt', 'r')
lst = f.readlines()
newLst = []
for element in lst:
    newLst.append(element.replace('\n', ''))
matrix = []
for element in newLst:
    matrix.append(list(element))
initial_matrix = copy.deepcopy(matrix)


def adjacent_occupied(matrix, i, j):
    adjacent_occupied = 0
    if i == 0 and j == 0:
        for a in [i, i+1]:
            for b in [j, j+1]:
                if a == i and b == j:
                    continue
                adjacent_occupied += count_occupied(matrix, a, b)

    elif i == 0 and j == len(matrix[0]) - 1:
        for a in [i, i+1]:
            for b in [j-1, j]:
                if a == i and b == j:
                    continue
                adjacent_occupied += count_occupied(matrix, a, b)
    elif i == len(matrix) - 1 and j == 0:
        for a in [i-1, i]:
            for b in [j, j+1]:
                if a == i and b == j:
                    continue
                adjacent_occupied += count_occupied(matrix, a, b)
    elif j == len(matrix[0]) - 1 and i == len(matrix) - 1:
        for a in [i-1, i]:
            for b in [j-1, j]:
                if a == i and b == j:
                    continue
                adjacent_occupied += count_occupied(matrix, a, b)

    elif i == 0:
        for a in [i, i+1]:
            for b in [j-1, j, j+1]:
                if a == i and b == j:
                    continue
                adjacent_occupied += count_occupied(matrix, a, b)
    elif j == 0:
        for a in [i-1, i, i+1]:
            for b in [j, j+1]:
                if a == i and b == j:
                    continue
                adjacent_occupied += count_occupied(matrix, a, b)
    elif i == len(matrix) - 1:
        for a in [i-1, i]:
            for b in [j-1, j, j+1]:
                if a == i and b == j:
                    continue
                adjacent_occupied += count_occupied(matrix, a, b)
    elif j == len(matrix[0]) - 1:
        for a in [i-1, i, i+1]:
            for b in [j-1, j]:
                if a == i and b == j:
                    continue
                adjacent_occupied += count_occupied(matrix, a, b)
    else:
        for a in [i-1, i, i+1]:
            for b in [j-1, j, j+1]:
                if a == i and b == j:
                    continue
                adjacent_occupied += count_occupied(matrix, a, b)
    return adjacent_occupied


def count_occupied(matrix, a, b):
    if matrix[a][b] == '#':
        return 1
    return 0


iteration = 0
while True:
    iteration += 1
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            if initial_matrix[i][j] == 'L' and adjacent_occupied(initial_matrix, i, j) == 0:
                matrix[i][j] = '#'
            elif initial_matrix[i][j] == '#' and adjacent_occupied(initial_matrix, i, j) >= 4:
                matrix[i][j] = 'L'
    if initial_matrix == matrix:
        break
    initial_matrix = copy.deepcopy(matrix)
count = 0
print(iteration)
for row in matrix:
    for seat in row:
        if seat == '#':
            count += 1
print(f'Silver star: Number of occupied seats is {count}')
