import math
def divisors_count_number(current):
    count = 0
    for divisor in range(1, math.ceil(current**0.5)+1):
        if current % divisor == 0:
            count = count + 2
    return count

def highly_divisible_triangular_number(divisors_number=5):
    current = 1
    next = 2
    divisors_count = 1
    while divisors_count < divisors_number:
        current = current + next
        next = next + 1
        divisors_count = divisors_count_number(current)
        print(current, divisors_count)
    return current

print(highly_divisible_triangular_number())

print(highly_divisible_triangular_number(500))
