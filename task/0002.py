def sum_of_even_fibb_number(lower_of: int)->int:
    sum = 0
    a = 1
    b = 1
    next_a = False
    while a + b < lower_of:
        if next_a:
            a = a + b
            if a % 2 == 0:
                sum = sum + a
        else :
            b = a + b
            if b % 2 == 0:
                sum = sum + b
        next_a = not next_a
    return sum

print(sum_of_even_fibb_number(12))

print(sum_of_even_fibb_number(4000000))
