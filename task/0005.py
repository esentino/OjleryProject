from functools import reduce
from operator import mul


def smallest_multiple(min, max):

    number_range = range(min, max + 1)
    max_number = reduce(mul, number_range, 1)
    for n in range(max, max_number):
        if is_divided_by_numbers(n, number_range):
            return n
    return max_number


def is_divided_by_numbers(n, number_range):
    for m in number_range:
        if n % m != 0:
            return False
    return True

print(smallest_multiple(1, 10))

print(smallest_multiple(1, 20))
