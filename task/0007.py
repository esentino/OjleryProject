import math
first_prime_number = 2
def is_prime(param):
    for n in range(first_prime_number, math.ceil(param**0.5)+1):
        if param % n == 0:
            return False
    return True

def prime(nth):
    counter = 1
    current_number = 2
    while counter < nth:
        current_number = current_number + 1
        if is_prime(current_number):
            print(current_number)
            counter = counter + 1

    return current_number

print(prime(6))

print(prime(10001))
