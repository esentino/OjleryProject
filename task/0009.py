def find_pythagorean(number):
    for i in range(1, number-2):
        for j in range(i,number-1):
            for k in range(j, number):
                if i +j + k == number and i**2 + j**2 == k**2 :
                    return i*j*k

print(find_pythagorean(12))

print(find_pythagorean(1000))