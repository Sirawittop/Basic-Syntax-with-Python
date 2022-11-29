#dd/mm/yy
DD,MM,YY = input().split('/')
DD = int(DD)
MM = int(MM)
YY = int(YY)
Date = DD + 30*MM + 30*12*YY
print(Date)