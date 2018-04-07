def sum_of_number(number_below: int):
    return sum([x for x in range(number_below) if x % 5 == 0 or x % 3 == 0])


print(sum_of_number(10))

print(sum_of_number(1000))