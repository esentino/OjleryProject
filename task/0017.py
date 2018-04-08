count=[0 for x in range(1001)]
count[1]  = 3#one
count[2]  = 3#two
count[3]  = 5#three
count[4]  = 4#four
count[5]  = 4#five
count[6]  = 3#six
count[7]  = 5#seven
count[8]  = 5#eight
count[9]  = 4#nine
count[10] = 3#ten
count[11] = 6#eleven
count[12] = 6#twelve
count[13] = 8#thirteen
count[14] = 8#fourteen
count[15] = 7#fifteen
count[16] = 7#sixteen
count[17] = 9#seventeen
count[18] = 8#eighteen
count[19] = 8#nineteen
count[20] = 6#twenty
#count[range(21,30)] = count[20] + count[range(1,10)]
count[30] = 6#thirty
count[40] = 5#forty
count[50] = 5#fifty
count[60] = 5#sixty
count[70] = 7#seventy
count[80] = 6#eighty
count[90] = 6#ninety
count[100] = 7#hundred
count[1000] = 8#thousand
print(count)
def letter_count(min, max):
    sum=0
    for number in range(min, max+1):
        if number%100 < 20:
            sum=sum+count[number%100]
        else:
            sum=sum+count[number%100//10*10]+count[number%10]
        if 100 <= number < 1000:
            sum=sum+count[number//100]+count[100]
            if number % 100 > 0:
                sum = sum+3 #and word
        if number == 1000:
            sum = sum+count[1]+count[1000]
        print(sum, number)
    return sum

print(letter_count(1,5))
print(letter_count(1,1000))