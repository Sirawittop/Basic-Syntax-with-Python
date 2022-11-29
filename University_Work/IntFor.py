#การใช้งาน [int (e) for e in]
dd, mm, yy = [int (e) for e in input().split('/')]
Date = dd + 30*mm + 30*12*yy
print(Date)
num = [float(e) for e in input("กรอกทศนิยม :  ").split()]
print(num)
total = 0
for e in num:
  total += e
print(total)