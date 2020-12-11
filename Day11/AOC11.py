import copy
f = open('Day11/AOC11.txt', 'r')
lst = f.readlines()
newLst = []
for element in lst:
    newLst.append(element.replace('\n', ''))


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


def silver():
    matrix = []
    for element in newLst:
        matrix.append(list(element))
    initial_matrix = copy.deepcopy(matrix)
    while True:
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                if initial_matrix[i][j] == 'L' and adjacent_occupied(initial_matrix, i, j) == 0:
                    matrix[i][j] = '#'
                elif initial_matrix[i][j] == '#' and adjacent_occupied(initial_matrix, i, j) >= 4:
                    matrix[i][j] = 'L'
        if initial_matrix == matrix:
            break
        initial_matrix = copy.deepcopy(matrix)
    print(
        f'Silver star: Number of occupied seats is {count_total_occupied(matrix)}')


def count_total_occupied(matrix):
    count = 0
    for row in matrix:
        for seat in row:
            if seat == '#':
                count += 1
    return count


def count_right(matrix, i, j):
    count = 0
    for a in range(j + 1, len(matrix[0])):
        if matrix[i][a] == 'L':
            break
        if matrix[i][a] == '#':
            count += 1
            break
    return count


def count_down(matrix, i, j):
    count = 0
    for b in range(i + 1, len(matrix)):
        if matrix[b][j] == 'L':
            break
        if matrix[b][j] == '#':
            count += 1
            break
    return count


def count_up(matrix, i, j):
    count = 0
    for b in range(i - 1, -1, -1):
        if matrix[b][j] == 'L':
            break
        if matrix[b][j] == '#':
            count += 1
            break
    return count


def count_left(matrix, i, j):
    count = 0
    for a in range(j - 1, -1, -1):
        if matrix[i][a] == 'L':
            break
        if matrix[i][a] == '#':
            count += 1
            break
    return count


def loop_diagonally_down_right(matrix, a, b):
    count = 0
    a, b = a + 1, b + 1
    while a < len(matrix) and b < len(matrix[0]):
        if matrix[a][b] == 'L':
            break
        if matrix[a][b] == '#':
            count += 1
            break
        a, b = a + 1, b + 1
    return count


def loop_diagonally_down_left(matrix, a, b):
    count = 0
    a, b = a + 1, b - 1
    while a < len(matrix) and b > - 1:
        if matrix[a][b] == 'L':
            break
        if matrix[a][b] == '#':
            count += 1
            break
        a, b = a + 1, b - 1
    return count


def loop_diagonally_up_right(matrix, a, b):
    count = 0
    a, b = a - 1, b + 1
    while a > - 1 and b < len(matrix[0]):
        if matrix[a][b] == 'L':
            break
        if matrix[a][b] == '#':
            count += 1
            break
        a, b = a - 1, b + 1
    return count


def loop_diagonally_up_left(matrix, a, b):
    count = 0
    a, b = a - 1, b - 1
    while a > -1 and b > -1:
        if matrix[a][b] == 'L':
            break
        if matrix[a][b] == '#':
            count += 1
            break
        a, b = a - 1, b - 1
    return count


def adjacent_occupied_direction(matrix, i, j):
    adjacent_occupied = 0
    if i == 0 and j == 0:
        adjacent_occupied += count_right(matrix, i, j) + count_down(
            matrix, i, j) + loop_diagonally_down_right(matrix, i, j)

    elif i == 0 and j == len(matrix[0]) - 1:
        adjacent_occupied += count_left(matrix, i, j) + count_down(
            matrix, i, j) + loop_diagonally_down_left(matrix, i, j)
    elif i == len(matrix) - 1 and j == 0:
        adjacent_occupied += count_up(matrix, i, j) + count_right(
            matrix, i, j) + loop_diagonally_up_right(matrix, i, j)
    elif j == len(matrix[0]) - 1 and i == len(matrix) - 1:
        adjacent_occupied += count_up(matrix, i, j) + count_left(
            matrix, i, j) + loop_diagonally_up_left(matrix, i, j)
    elif i == 0:
        adjacent_occupied += count_left(matrix, i, j) + count_right(matrix, i, j) + count_down(
            matrix, i, j) + loop_diagonally_down_left(matrix, i, j) + loop_diagonally_down_right(matrix, i, j)
    elif j == 0:
        adjacent_occupied += count_right(matrix, i, j) + count_up(matrix, i, j) + count_down(
            matrix, i, j) + loop_diagonally_up_right(matrix, i, j) + loop_diagonally_down_right(matrix, i, j)
    elif i == len(matrix) - 1:
        adjacent_occupied += count_right(matrix, i, j) + count_left(matrix, i, j) + count_up(
            matrix, i, j) + loop_diagonally_up_left(matrix, i, j) + loop_diagonally_up_right(matrix, i, j)
    elif j == len(matrix[0]) - 1:
        adjacent_occupied += count_down(matrix, i, j) + count_up(matrix, i, j) + count_left(
            matrix, i, j) + loop_diagonally_up_left(matrix, i, j) + loop_diagonally_down_left(matrix, i, j)
    else:
        adjacent_occupied += count_down(matrix, i, j) + count_up(matrix, i, j) + count_left(
            matrix, i, j) + + count_right(matrix, i, j) + loop_diagonally_up_left(matrix, i, j) + loop_diagonally_down_left(matrix, i, j) + loop_diagonally_down_right(matrix, i, j) + loop_diagonally_up_right(matrix, i, j)
    return adjacent_occupied

# gold:


def gold():
    matrix = []
    for element in newLst:
        matrix.append(list(element))
    initial_matrix = copy.deepcopy(matrix)
    while True:
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                if initial_matrix[i][j] == 'L' and adjacent_occupied_direction(initial_matrix, i, j) == 0:
                    matrix[i][j] = '#'
                elif initial_matrix[i][j] == '#' and adjacent_occupied_direction(initial_matrix, i, j) >= 5:
                    matrix[i][j] = 'L'
        if initial_matrix == matrix:
            break
        initial_matrix = copy.deepcopy(matrix)
    print(
        f'Gold star: Number of occupied seats is {count_total_occupied(matrix)}')


silver()
gold()
