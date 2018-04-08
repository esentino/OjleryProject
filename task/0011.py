from functools import reduce
from operator import mul

def find_solution(col_length=20, row_length=20):
    table = [[0 for y in range(row_length)] for x in range(col_length)]

    with open('0011.txt') as file:
        row_counter = 0
        for line in file.readlines():
            row = line.split(' ')
            col_counter = 0
            for cell in row:
                table[row_counter][col_counter] = int(cell)
                col_counter = col_counter + 1
            row_counter = row_counter + 1
    max_row = check_row(table)
    max_col = check_col(table)
    max_diagon = check_diagonal(table)
    return max(max_row,max_col, max_diagon)


def check_row(table, col_length=20, row_lenght=20):
    max = 0
    for col in range(col_length):
        numbers = [0 for x in range(4)]
        for row in range(row_lenght):
            numbers[row % 4] = table[row][col]
            result = reduce(mul, numbers, 1)
            if max < result:
                max = result
    return max


def check_col(table, col_length=20, row_length=20):
    max = 0
    for row in range(row_length):
        numbers = [0 for x in range(4)]
        for col in range(col_length):
            numbers[col%4] = table[row][col]
            result = reduce(mul,numbers, 1)
            if max < result:
                max = result
    return max

def check_diagonal(table, col_length=20, row_length=20):
    max = 0
    #check \ way
    for x in range(row_length-3):
        for y in range(col_length-3):
            numbers = [table[x][y], table[x+1][y+1], table[x+2][y+2], table[x+3][y+3]]
            result = reduce(mul, numbers, 1)
            if max < result:
                max = result
    #check / way
    for x in range(row_length-3):
        for y in range(3, col_length):
            numbers = [table[x][y], table[x + 1][y - 1], table[x + 2][y - 2], table[x + 3][y - 3]]
            result = reduce(mul, numbers, 1)
            if max < result:
                max = result

    return max

print(find_solution())
