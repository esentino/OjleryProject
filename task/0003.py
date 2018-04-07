import math

first_prime_number = 2
def is_prime(param):
    for n in range(first_prime_number, math.ceil(param**0.5)):
        if param % n == 0:
            return False
    return True


def large_prime_factor(number):

    for n in range(first_prime_number, number):
        if number % n == 0:
            if is_prime(number/n):
                return number/n

print(large_prime_factor(13195))

print(large_prime_factor(600851475143))