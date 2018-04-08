

def longest_chain(below = 1000000):
    n = 0
    longest_number = 1
    longest_counter = 1
    for i in range(2, below):
        n = i
        counter = 0
        while n != 1:
            if n % 2 == 0:
                n = n / 2
            else:
                n = 3 * n + 1
            counter = counter+1

        if counter > longest_counter:
            print(counter, i)
            longest_counter = counter
            longest_number = i

    return longest_number

print(longest_chain(1000000))