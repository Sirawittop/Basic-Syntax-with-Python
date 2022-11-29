import math
Yu = [18,22,24,17,19,20,25,15,14]
Ume = [19,19,21,21,20,18,13,13,20,]
listA = []
listB = []
listApow2 = []
listBpow2 = []
Nm = len(Yu)
Mn = len(Ume)
A = 0
B = 0
C = 0
D = 0
for i in range(Nm): 
    A += Yu[i]
for i in range(Mn):
    B += Ume[i]
XbarA =A/Nm
XbarB =B/Mn
for i in range(Nm):
   Ss =  Yu[i] - XbarA
   listA.append(Ss)
for i in range(Mn):
    Tt = Ume[i] - XbarB
    listB.append(Tt)
for i in range(Nm):
    Pop = listA[i]*listA[i]
    listApow2.append(Pop)
for i in range(Mn):
    Tot = listB[i]*listB[i]
    listBpow2.append(Pop)
for i in range(Nm):
    C += listApow2[i]
for i in range(Nm):
    D += listBpow2[i]
Spow2A = C/(Nm-1)
Spow2B = D/(Mn-1)
Com = XbarA - XbarB
Pu = Spow2A/Nm
Ter = Spow2B/Mn
Computer = Pu + Ter
Note = math.sqrt(Computer)
Book = Com/Note
print(Book)
if Book <= 1.746 :
    print("accepth0")
else:
    print("accepth1")
#64020822 สิรวิชญ์ คำชุ่ม
#64020721 ภัทรดนัย ใจเต็ม
#64020811 สพลดนัย พรหมศรี
#64024309 จิรศักดิ์ อุ่นบ้าน