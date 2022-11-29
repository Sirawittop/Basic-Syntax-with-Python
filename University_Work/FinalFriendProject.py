""""
print("ยินดีต้อนรับสู้ ร้านหมูกระทะ อู๊ดอู๊ด")
print("เชิญเลือกโต๊ะที่นั่งได้เลยครับ")
Menu = ["A5"]
price_Menu = ["100"]
Drink = ["cola"]
price_Drink =["10"]
Dessert =["jelly"]
price_Dessert = ["20"]
bath = ('บาท')
def Menus():
  print('\รายการเมนูหลักที่มี')
  print(' รายการ ','\t\t\t\t\t\t\t\\t\t\t\t\t\t', 'ราคา')
  for i in range(1):
    print("{:2}.{}{}{}".format(i+1,Menu[i],'\t\t\t\t\t\t\t\t',price_Menu[i]),bath)
def Drinks() :
  print('\รายการเครื่องเดื่มที่มี')
  print(' รายการ ','\t\t\t\t\t\t\t\\t\t\t\t\t\t', 'ราคา')
  for i in range(10):
    print("{:2}.{}{}{}".format(i+1,Drink[i],'\t\t\t\t\t\t\t\t',price_Drink[i]),bath)
def Desserts() :
  print('\รายการของว่างที่มัที่มี')
  print(' รายการ ','\t\t\t\t\t\t\t\\t\t\t\t\t\t', 'ราคา')
  for i in range(10):
    print("{:2}.{}{}{}".format(i+1,Dessert[i],'\t\t\t\t\t\t\t\t',price_Dessert[i]),bath)
def buy_1(sm):
  selectmenu = sm
  if selectmenu == "1" :
    item01 = "A5"
    menuma.append(item01)
    sinca = 100
    sincas.append(sinca)
  question()
def buy_2(sm):
  selectmenu = sm
  if selectmenu == "1" :
    item01 = "cola"
    menuma.append(item01)
    sinca = 10
    sincas.append(sinca)
  question()
def buy_3(sm):
  selectmenu = sm
  if selectmenu == "1" :
    item01 = "jelly"
    menuma.append(item01)
    sinca = 20
    sincas.append(sinca)
  question()
def next():
  print("กด 1 เพื่อสั่งอาหารเพิ่ม")
  print("กด 2 เพื่อชำระเงิน")
  go = input("รอคำสั่ง")
  if go == "1" :
    start0()
  elif go == "2":
    print("จำนวนเงินทั้งหมดที่ต้องจ่าย : ",sum(sincas),bath)
    pay()
def select_1():
  print("1 เพื่อเลือกสินค้า")
  print("2 เพื่อกับไปดูหมวดหมู่")
  tik = input("รอคำสั่ง")
  if tik == "1" :
    last_1()
  elif tik == "2":
    start0()
def select_2():
  print("1 เพื่อเลือกสินค้า")
  print("2 เพื่อกับไปดูหมวดหมู่")
  tik = input("รอคำสั่ง")
  if tik == "1" :
    last_2()
  elif tik == "2":
    start0()
def select_3():
  print("1 เพื่อเลือกสินค้า")
  print("2 เพื่อกับไปดูหมวดหมู่")
  tik = input("รอคำสั่ง")
  if tik == "1" :
    last_2()
  elif tik == "2":
    start0()
def question():
  print("1 เพื่อยืนยันเมนู")
  print("2 เพื่อยกเลิก ")
  add = input("รอคำสั่ง")
  if add == "1":
    next()
  elif add == "2":
    del sincas[-1]
    del menuma[-1]
    start0()
def last_1():
  sm = input('เลือกเมนูที่ต้องการ')
  if sm in ['1']:
    buy_1(sm)
def last_2():
   sm = input('เลือกเมนูที่ต้องการ')
   if sm in ['1']:
    buy_2(sm)
def last_3():
   sm = input('เลือกเมนูที่ต้องการ')
   if sm in ['1']:
    buy_3(sm)
def start0():
  pin =1
  while pin == 1:
    print()
    print("1 เลือกเมนูหลัก")
    print("2 เลือกเครื่องดื่ม")
    print("3 เลือกของว่าง")
    print("4 ชำระเงิน")
    print()
    choice = input("รอคำสั่ง")
    if choice == "1":
      Menus()
      select_1()
      pin1 = 1
      pin =2
    elif choice == "2":
      Drinks()
      select_2()
      pin1 = 1
      pin =2
    elif choice == "3":
      Desserts()
      select_3()
      pin1 = 1
      pin =2
    elif choice == "4":
      pay()
      pin1 = 1
      pin =2
def system_auto():
  print("จำนวนเงินที่ต้องจ่าย : ",sum(sincas),bath)
  money = (int(input("จำนวนเงินที่คุณจ่ายมาให้ : ")))
  money1 = str(money)
  rubma = money - sum(sincas)
  bank1000 = (rubma//1000)
  trade.append(bank1000)
  bank500 = (rubma%1000//500)
  trade.append(bank500)
  bank100 = (rubma%1000//100)-(bank500*5)
  trade.append(bank100)
  bank50 = (rubma%100//50)
  trade.append(bank50)
  bank20 = ((rubma%100-bank50*50)//20)
  trade.append(bank20)
  bank10 = ((rubma%100-bank50*50-bank20*20)//10)
  trade.append(bank10)
  bank5 = (rubma%10//5)
  trade.append(bank5)
  bank1 = (rubma%10//1)-bank5*5
  trade.append(bank1)
  if money >= sum(sincas):
    print
    print(' รายการ ','\t\t\t\t\t\t\t\\t\t\t\t\t\t', 'ราคา')
    for i in range(len(menuma)):
      print("{:2}.{}{}{}".format(i+1,menuma[i],'\t\t\t\t\t\t\t\t',sincas[i]),bath)
      print()
      print("ขอบคุณที่ใช้บริการ")
  elif money > sum(sincas):
    print("******ชำระเงินใหม่******")
    print("******คุณจะไม่ได้รับเงินทอน******")
    bat()
  elif miney1 == ' ':
    print("******จำนวนเงินไม่เพียงพอต่อการชำระ******")
  elif money < sum(sincas):
    print("******จำนวนเงินไม่เพียงพอต่อการชำระ******")
    bat()
def pay() :
  print("คุณต้องการจ่ายเงินแบบไหน")
  print("1. เงินสด")
  print("2. บัตรเครดิตหรือพ้อมเพล")
  pay_select = input()
  if pay_select == "1" :
    print("ขอบคุณที่ใช้บริการ ของทางร้าน")
    system_auto()
  elif pay_select == "2" :
    bat()
sincas = []
trade = []
menuma = []
start0()  
"""