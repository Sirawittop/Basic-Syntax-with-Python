def odd_number():
  a1 = int(input("กรุณากรอกจำนวนเต็มบวกจำนวนแรก    :   "))
  a2 = int(input("กรุณากรอกจำนวนเต็มบวกจำนวนที่สอง    :   "))
  print("_________________________________________________________")
  sum = 1
  print("จำนวนคี่ระหว่าง",a1,"และ", a2 ,"คือ :",end = ' ')
  if a1 > 0 and a2 > 0 :
    for x in range( a1, (a2+1) ):
        if( x % 2 != 0 ):
          sum = sum * x
          print(x , end = " ")
          
  print("\nผลคูณจำนวนคี่ทั้งหมดคือ  : ",sum)
  print("_________________________________________________________")



def prime_number():
  b1 = int(input("กรุณากรอกจำนวนเต็มบวกจำนวนแรก    :   "))
  b2 = int(input("กรุณากรอกจำนวนเต็มบวกจำนวนที่สอง    :   "))
  print("_________________________________________________________")
  print("จำนวนเฉพาะระหว่าง",b1,"และ", b2 ,"คือ :",end = ' ')
  sum2 = 1
  for j in range (b1, b2 + 1):  
    if j > 1:  
        for i in range (2, j):
            if (j % i) == 0:  
              break  
        else: 
          sum2 = sum2 * j 
          print (j,end = " ")  
  print("\nผลคูณจำนวนเฉพาะทั้งหมดคือ  : ",sum2)
  print("_________________________________________________________")


while True:
  first_loop = input('''คุณต้องการใช้โปรแกรมใด
                    กรอกเลข 1 เพื่อ หาเลขคี่ทั้งหมดระหว่างจำนวนเต็มบวกจากนั้นนำมาคูณกัน
                    กรอกเลข 2 เพื่อ หาจำนวนเฉพาะระหว่างจำนวนเต็มบวกจากนั้นนำมาคูณกัน
                    
                    ''')
  if first_loop == "1":
        odd_number()
  if first_loop == "2":
        prime_number()
  
  a3 = input("คุณต้องการดำเนินการต่อหรือไม่ (Y/N)  : ")
  if a3.upper() =="N":
    break

print("Good Bye <_>")
  
