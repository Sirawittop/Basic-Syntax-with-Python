print("  -------------------------------------------------------")
print("             ยินดีต้อนรับเข้าสู่ The Cloud Fruit Shop")
print("  -------------------------------------------------------")
print("            ท่านสามารถเลือกหมวดหมู่ประเภทสินค้าของทางร้านได้ดังนี้")
print("  -------------------------------------------------------")
fresh_fruit = ["อะโวคาโด","มังคุด","แก้วมังกร","สับปะรด","มะพร้าว","กล้วย","เสาวรส","กระท้อน","แอปเปิ้ล","ส้ม","ฝรั่ง","แตงโม","ทุเรียน","มะม่วง"]
price_fresh_fruit = [85, 60, 35, 35, 30, 30, 30, 40, 40, 30, 35, 40, 200, 25]
peeled_fruit = ["แตงโม","ฝรั่ง","เมล่อน","แอปเปิ่ล","สตอเบอร์รี่","แก้วมังกร","มะม่วง","มะละกอ","สาลี่","กี่วี่","ชมพู่","กระท้อน"]
price_peeled_fruit = [20, 20, 20, 25, 30, 20, 20, 20, 20, 30, 20, 25]
processed_fruit = ["แยมสับปะรด","แยมสตอเบอร์รี่","เงาะลอยแก้ว","มะม่วงกวน","ทุเรียนกวน","ทุเรียนทอด","ทุเรียนเชื่อม","วุ้นมะพร้าว","กล้วยเชื่อม","ลำไยอบแห้ง","กี่วี่อบแห้ง"]
price_processed_fruit = [85, 85, 40, 50, 65, 70, 60, 40, 35, 50, 70]
fruit_basket = ["S","M","L","XL"]
price_fruit_basket = [400, 750, 900, 1250]
bath = ('บาท')
price_fresh_fruit_all = 0
price_peeled_fruit_all = 0
price_processed_fruit_all = 0
price_fruit_basket_all = 0
y1 = 0
y2 = 0
y3 = 0
y4 = 0

def fresh_fruit_funtion():
  print("\nผลไม้สดมีทั้งหมด 14 รายการ")
  print("\n  รายการ","\t\t\t\t\t","ราคา / กิโลกรัม")
  for i in range(0,14):
      print("{:2}.{}{}{}".format(i+1,fresh_fruit[i],"            \t\t\t ",price_fresh_fruit[i])+" \t"+bath)
  global price1
  fresh_fruit_1 = input("\nกรอกหมายเลขสินค้าที่ต้องการ  :  ")
  global price1
  if fresh_fruit_1 == '1' :
          price1 = 85
          price_fresh_fruit_how_much()
  elif fresh_fruit_1 == '2' :
          price1 = 60
          price_fresh_fruit_how_much()
  elif fresh_fruit_1 == '3' :
          price1 = 35
          price_fresh_fruit_how_much()
  elif fresh_fruit_1 == '4' :
          price1 = 35
          price_fresh_fruit_how_much()
  elif fresh_fruit_1 == '5' :
          price1 = 30
          price_fresh_fruit_how_much()
  elif fresh_fruit_1 == '6' :
          price1 = 30
          price_fresh_fruit_how_much()
  elif fresh_fruit_1 == '7' :
          price1 = 30
          price_fresh_fruit_how_much()
  elif fresh_fruit_1 == '8' :
          price1 = 40
          price_fresh_fruit_how_much()
  elif fresh_fruit_1 == '9' :
          price1 = 40
          price_fresh_fruit_how_much()
  elif fresh_fruit_1 == '10' :
          price1 = 30
          price_fresh_fruit_how_much()
  elif fresh_fruit_1 == '11' :
          price1 = 35
          price_fresh_fruit_how_much()
  elif fresh_fruit_1 == '12' :
          price1 = 40
          price_fresh_fruit_how_much()
  elif fresh_fruit_1 == '13' :
          price1 = 200
          price_fresh_fruit_how_much()
  elif fresh_fruit_1 == '14' :
          price1 = 25
          price_fresh_fruit_how_much()
  else:
      print("\n------------------ไม่มีคำสั่งนี้ กรุณากรอกใหม่-----------------")
      fresh_fruit_funtion()

def peeled_fruit_funtion():
  print("\nผลไม้ปอกพร้อมทานมีทั้งหมด 12 รายการ")
  print("\n  รายการ","\t\t\t\t\t","ราคา /  ชิ้น")
  for i in range(0,12):
      print("{:2}.{}{}{}".format(i+1,peeled_fruit[i],"            \t\t\t ",price_peeled_fruit[i])+" \t"+bath)
  peeled_fruit_1 = input("\nกรอกหมายเลขสินค้าที่ต้องการ  :  ")
  global price2
  if peeled_fruit_1 == '1' :
        price2 = 20
        price_peeled_fruit_how_much()
  elif peeled_fruit_1 == '2' :
        price2 = 20
        price_peeled_fruit_how_much()
  elif peeled_fruit_1 == '3' :
        price2 = 20
        price_peeled_fruit_how_much()
  elif peeled_fruit_1 == '4' :
        price2 = 25
        price_peeled_fruit_how_much()
  elif peeled_fruit_1 == '5' :
        price2 = 30
        price_peeled_fruit_how_much()
  elif peeled_fruit_1 == '6' :
        price2 = 20
        price_peeled_fruit_how_much()
  elif peeled_fruit_1 == '7' :
        price2 = 20
        price_peeled_fruit_how_much()
  elif peeled_fruit_1 == '8' :
        price2 = 20
        price_peeled_fruit_how_much()
  elif peeled_fruit_1 == '9' :
        price2 = 20
        price_peeled_fruit_how_much()
  elif peeled_fruit_1 == '10' :
        price2 = 30
        price_peeled_fruit_how_much()
  elif peeled_fruit_1 == '11' :
        price2 = 20
        price_peeled_fruit_how_much()
  elif peeled_fruit_1 == '12' :
        price2 = 25
        price_peeled_fruit_how_much()
  else:
      print("\n------------------ไม่มีคำสั่งนี้ กรุณากรอกใหม่-----------------")
      peeled_fruit_funtion()

def processed_fruit_funtion():
  print("\nผลไม้สดมีทั้งหมด 11 รายการ")
  print("\n  รายการ","\t\t\t\t\t","ราคา /  ชิ้น")
  for i in range(0,11):
      print("{:2}.{}{}{}".format(i+1,processed_fruit[i],"            \t\t\t ",price_processed_fruit[i])+" \t"+bath)
  processed_fruit_1 = input("\nกรอกหมายเลขสินค้าที่ต้องการ  :  ")
  global price3
  if processed_fruit_1 == '1' :
          price3 = 85
          processed_fruit_how_much()
  elif processed_fruit_1 == '2' :
          price3 = 85
          processed_fruit_how_much()
  elif processed_fruit_1 == '3' :
          price3 = 40
          processed_fruit_how_much()
  elif processed_fruit_1 == '4' :
          price3 = 50
          processed_fruit_how_much()
  elif processed_fruit_1 == '5' :
          price3 = 65
          processed_fruit_how_much()
  elif processed_fruit_1 == '6' :
          price3 = 70
          processed_fruit_how_much()
  elif processed_fruit_1 == '7' :
          price3 = 60
          processed_fruit_how_much()
  elif processed_fruit_1 == '8' :
          price3 = 40
          processed_fruit_how_much()
  elif processed_fruit_1 == '9' :
          price3 = 35
          processed_fruit_how_much()
  elif processed_fruit_1 == '10' :
          price3 = 50
          processed_fruit_how_much()
  elif processed_fruit_1 == '11' :
          price3 = 70
          processed_fruit_how_much()
  else:
      print("\n------------------ไม่มีคำสั่งนี้ กรุณากรอกใหม่-----------------")
      processed_fruit_funtion()
  
def fruit_basket_funtion():
  print("\nผลไม้สดมีทั้งหมด 4 รายการ")
  print("\n  รายการ","\t\t\t\t\t","ราคา /  ชิ้น")
  for i in range(0,4):
      print("{:2}.{}{}{}".format(i+1,fruit_basket[i],"            \t\t\t ",price_fruit_basket[i])+" \t"+bath)
  fruit_basket_1 = input("\nกรอกหมายเลขสินค้าที่ต้องการ  :  ")
  global price4
  if fruit_basket_1 == '1' :
          price4 = 400
          price_fruit_basket_how_much()
  elif fruit_basket_1 == '2' :
          price4 = 750
          price_fruit_basket_how_much()
  elif fruit_basket_1 == '3' :
          price4 = 900
          price_fruit_basket_how_much()
  elif fruit_basket_1 == '4' :
          price4 = 1250
          price_fruit_basket_how_much()
  else:
      print("\n------------------ไม่มีคำสั่งนี้ กรุณากรอกใหม่-----------------")
      fruit_basket_funtion()

def nextbuy():
    while True:
      buy_next = input('''\nคุณต้องการซื้อสินค้าต่อหรือไม่
    1 . ดำเนินการต่อ
    2 . ชำระเงิน
    
    กรอกหมายเลขคำสั้งที่ต้องการ  :  ''')
      if buy_next == "1":
          print("ท่านสามารถเลือกหมวดหมู่ประเภทสินค้าของทางร้านได้ดังนี้")
          break
      elif buy_next == "2":
          all_price()
          money_rish()
          print("---------------------------------------------------")
          break
      else:
          print("\nไม่มีคำสั่งนี้ กรุณากรอกใหม่")
def all_price():
    all_money = y1 + y2 + y3 + y4
    print("---------------------------------------------------")
    print('''    จำนวนเงินที่ต้องจ่ายคือ   : ''',all_money,bath)
    print("---------------------------------------------------")
def money_rish():
    global sumall
    all_money = y1 + y2 + y3 + y4
    money = int(input('''    กรอกจำนวนเงินที่ผู้ใช้บริการจ่าย  :  ''',))
    print("---------------------------------------------------")
    if money > all_money :
        sumall = (money - all_money)
        print("    จำนวนเงินทอน  :  ",sumall,bath)
        money_type = [1000, 500, 100, 50, 20, 10, 5, 2, 1]
        for t in money_type:
         if sumall  >= t:
          print("    {} บาท  :  {}".format(t, int(sumall / t))," ใบ")
          sumall = sumall % t    
    else:
        print('''------------------- จำนวนเงินไม่เพียงพอ ------------------''')
def price_fresh_fruit_how_much():
  global y1
  kilogram = float(input("กรุณากรอกน้ำหนักผลไม้(หน่วยเป็นกิโลกรัม)  :   "))
  price_fresh_fruit_all = kilogram * price1
  x1 = price_fresh_fruit_all
  y1 += x1
  return y1 
def price_peeled_fruit_how_much():
  global y2
  Quantity = float(input("กรุณากรอกจำนวนสินค้าที่ต้องการ  :   "))
  price_peeled_fruit_all = Quantity * price2
  x2 = price_peeled_fruit_all
  y2 += x2
  return y2
def processed_fruit_how_much():
  global y3
  Quantity3 = float(input("กรุณากรอกจำนวนสินค้าที่ต้องการ  :   "))
  price_processed_fruit_all = Quantity3 * price3
  x3 = price_processed_fruit_all
  y3 += x3
  return y3
def price_fruit_basket_how_much():
  global y4
  Quantity4 = float(input("กรุณากรอกจำนวนสินค้าที่ต้องการ  :   "))
  price_fruit_basket_all = Quantity4 * price4
  x4 = price_fruit_basket_all
  y4 += x4
  return y4
while True:
  Product_type = input(''' 
  1 . ผลไม้สด
  2 . ผลไม้ปอกพร้อมทาน
  3 . ผลไม้แปรรูป
  4 . กระเช้าผลไม้
  5 . ออกจากโปรแกรม

  กรอกหมายเลขหมวดหมู่ที่ต้องการ  :  ''')
  if Product_type == "1":
      fresh_fruit_funtion()
      nextbuy()
  elif Product_type == "2":
      peeled_fruit_funtion()
      nextbuy()
  elif Product_type == "3":
      processed_fruit_funtion()
      nextbuy()
  elif Product_type == "4":
      fruit_basket_funtion()
      nextbuy()
  elif Product_type == "5":
      print("\n----------------ยินดีให้บริการครับ----------------")
      break
  else:
      print("\nไม่มีคำสั่งนี้ กรุณากรอกใหม่")