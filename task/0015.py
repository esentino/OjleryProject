
def path(left, down, length, memory=None):
    sum = 0
    if left < length:
        if memory[left+1][down]==0:
            memory[left+1][down] = path(left + 1, down, length, memory)
        sum = sum + memory[left + 1][down]
    if down < length:
        if memory[left][down + 1] == 0:
            memory[left][down + 1] = path(left, down + 1, length, memory)
        sum = sum + memory[left][down + 1]
    if left == length and down == length:
        return 1
    return sum


def lattice_paths(length=2):
    """1100 1010 1001 0110 0101 0011 for 2x2"""
    """  12   10    9    6    5    3"""
    memory = [[0 for y in range(length+1)] for x in range(length+1)]
    return path(0, 0, length, memory)


print(lattice_paths())

print(lattice_paths(20))
