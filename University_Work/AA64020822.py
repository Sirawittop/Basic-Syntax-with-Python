import math                                                                                                                                   # import math เพื่อเรียกใช้ Function ในการถอดรากที่สอง
setone = [4.5, 4.9, 6.2, 4.0, 4.3, 6.1, 4.8, 5.3, 6.7, 6.3, 7.8, 6.4, 4.8, 5.4, 5.1, 5.6, 6.3, 6.9, 5.8, 5.1, 5.8, 5.9, 5.6, 5.7, 3.8, 7.6,4.9,5.8,3.5,4.7,7.4]       # Data
listput = []                                                                                                                                      # สร้าง list ชื่อว่า listput ว่างไว้สำหรับเก็บข้อมูลหลังจากการแปลงหน่วบจากหลักหน่วยเป็นหลักพัน
listxi = []                                                                                                                                       # สร้าง list ชื่อว่า listxi ว่างไว้สำหรับเก็บข้อมูล xi - xbar
listpowertwo = []                                                                                                                                 # สร้าง list ชื่อว่า listpowertwo ว่างไว้สำหรับเก็บข้อมูล xi ยกกำลังสอง
xxbar = 6000                                                                                                                                      # สร้างตัวแปรที่มีชื่อว่า xxbar (ค่าเฉลี่ยของการซ่อม) กำหนดค่าให้ตัวแปรมีค่าเท่ากับ 6000
tcal0_95v25 = 1.708                                                                                                                               # สร้างตัวแปรที่มีชื่อว่า tcal0_95v25 (Tcal ที่ 0.97 df = 25) กำหนดค่าให้ตัวแปรมีค่าเท่ากับ 1.708 
# cal float to int 1000
for i in range(len(setone)):
    convertpun = int((setone[i])*1000)
    listput.append(convertpun)
# cal x bar
suminput = 0
for i in range(len(listput)):
    suminput += listput[i]
xbar = suminput/len(listput)
# cal SD xi - xbar
for i in range(len(listput)):
    calxixbar = listput[i] - xbar
    listxi.append(calxixbar)
#cal SD xi power two
for i in range(len(listput)):
    powerxi = listxi[i]*listxi[i]
    listpowertwo.append(powerxi)
#cal sum of S power 2
sumsd = 0
for i in range(len(listput)):
    sumsd += listpowertwo[i]
spower2 = sumsd / 25
sd = math.sqrt(spower2)

#cal T-cal
topofsuilt = xbar - xxbar
rootn = math.sqrt(len(listput))
buttonsuilt = sd/rootn
Tcal = topofsuilt / buttonsuilt
deletetcal = tcal0_95v25 * -1
print("\nSD = ",sd)
print("จำนวนสมาชิกของกลุ่มตัวอย่าง = ",len(setone))
print("Xbar = ", xbar)
print("_________________________")
print("\nระดับนัยสำคัญที่ 0.05") 
print("จุดวิกฤต = ",deletetcal)   
print("Tcal ที่คำนวณได้เท่ากับ ",Tcal) 

#calfor answer

if Tcal <= deletetcal:
    print("สรุปผลการทดสอบ : หลังใช้มาตรการลดค่าใช้จ่ายในการซ่อมสินค้ามี ค่าใช้จ่ายเฉลี่ยในการซ่อมสินค้าสูงกว่า 6,000 บาท ที่ระดับนัยสำคัญ 0.05\n")
else :
    print("สรุปผลการทดสอบ : หลังใช้มาตรการลดค่าใช้จ่ายในการซ่อมสินค้ามี ค่าใช้จ่ายเฉลี่ยในการซ่อมสินค้าต่ํากว่า 6,000 บาท ที่ระดับนัยสำคัญ 0.05\n")
