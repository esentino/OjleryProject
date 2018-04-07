import math
first_prime_number = 2
def is_prime(param):
    if param == first_prime_number:
        return True
    for n in range(first_prime_number, math.ceil(param**0.5)+1):
        if param % n == 0:
            return False
    return True

def sum_prime(below=2000000):
    sum = 0
    for number in range(2, below):
        if is_prime(number):
            sum = sum + number

    return sum


print(sum_prime(10))

print(sum_prime())