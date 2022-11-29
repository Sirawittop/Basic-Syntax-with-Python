num = int(input())
reversed_num = 0
sumofnumber = 0
while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10
    sumofnumber += digit

print(sumofnumber)