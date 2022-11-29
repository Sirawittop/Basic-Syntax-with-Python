listofnumber = ["0","1","2","3","4","5"]


def calculatorlistofnumber():
    i = 0
    for i in range(len(listofnumber)):
        if listofnumber[i] != "0":
            print(listofnumber[i],end = "\n")
            for i in range(len(listofnumber)):
                print(listofnumber[i], end="")
        


calculatorlistofnumber()