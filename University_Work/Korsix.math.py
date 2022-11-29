listofnumber  = []
for i in range(100,1100):
    listofnumber.append(i)
#100 <= n <= 999
listofnumberfive = []
for i in range(len(listofnumber)):
    if i > 99:
        if i % 5 == 0:
            listofnumberfive.append(i)
print(listofnumberfive)
print("The number of list = ",len(listofnumberfive),"number")