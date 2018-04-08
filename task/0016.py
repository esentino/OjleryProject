bank_size = 400
def power_digit_sum(power=15):
    number = [0 for i in range(bank_size)]
    number[0] = 1
    for p in range(power):
        for z in range(bank_size-1):
            number[z+1] = number[z+1] + (number[z]//10)
            number[z] = number[z]%10
            number[z] = number[z]*2

    for z in range(bank_size - 1):
        number[z + 1] = number[z+1] + (number[z] // 10)
        number[z] = number[z] % 10
    print(number)
    print(any([x > 9 for x in number]))
    return sum(number)

print(power_digit_sum())
for i in range(10):
    print(power_digit_sum(i))

print(power_digit_sum(1000))

