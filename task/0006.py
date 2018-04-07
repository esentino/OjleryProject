def sum_square_difference(max):
    sum_square = sum([i**2 for i in range(max +1)])
    square_sum = sum([i for i in range(max+1)]) ** 2
    return square_sum - sum_square

print(sum_square_difference(10))

print(sum_square_difference(100))
