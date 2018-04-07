def largest_palindrome_product():
    max = 0
    for first_number in range(100,1000):
        for second_number in range(100, 1000):
            product = first_number * second_number
            if (max < product
                    and product // 100000 == product % 10
                    and (product // 10000) % 10 == product % 100//10
                    and (product // 1000) % 10 == product % 1000//100
            ):
                max = product
    return max

print(largest_palindrome_product())
