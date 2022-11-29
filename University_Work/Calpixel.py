""""
import math 
def cal_area_rect():
    w = float(input("ความกว้างของสี่เหลี่ยมผืนผ้า : "))
    l = float(input("ความยาวของสี่เหลี่ยมผืนผ้า : "))
    area_rect = w * l
    print("พื้นที่สี่เหลี่ยมพื้นผ้า : " , area_rect)
def cal_area_tri():
    b = float(input("ความยาวฐานของสามเหลี่ยม : "))
    h = float(input("ความสูงของสามเหลี่ยม : "))
    area_tri = 1/2 * b * h
    print("พื้นที่สามเหลี่ยม : " , area_tri)
def cal_area_circle():
    r = float(input("รัศมี : "))
    area_circle = math.pi * r * r
    print("พื้นที่วงกลม : " , area_circle)
def cal_circum_rect():
    w = float(input("ความกว้างของสี่เหลี่ยมผืนผ้า : "))
    l = float(input("ความยาวของสี่เหลี่ยมผืนผ้า : "))
    print()
def cal_circum_rect():
  w = float(input("ความกว้างสี่เหลี่ยมผืนผ้า  :  "))
  l = float(input("ความยาวสี่เหลี่ยมผืนผ้า  :  "))
  print(2 * (w+l))
def cal_circum_tri():
  b = float(input("ความยาวฐานของสามเหลี่ยม : "))
  h = float(input("ความสูงของสามเหลี่ยม : "))
  c = math.sqrt(b * b + h * h)
  print(b + h + c)
def cal_circum_circle():
  r = float(input("รัศมี  : "))
  print(2 * math.pi * r)
while True :
    ans1 = input('''คุณต้องการคำนวณพื้นที่หรือเส้นรอบวง
                    1. พื้นที่
                    2. เส้นรอบวง
                    หรือกด q เพื่อออกโปรแกรม\n''')
    if ans1 == "1":
      ans2 = input('''คุณต้องการคำนวณหาพื้นที่ของรูปทรงอะไร

                    1.สี่เหลี่ยมผืนผ้า
                    2.สามเหลี่ยมมุมฉาก
                    3.วงกลม\n
                    ''')
      print("_______________________________________________________________________________________________________________________")
      if ans2 == "1" : 
            cal_area_rect()
      if ans2 == "2" : 
            cal_area_tri()
      if ans2 == "3" : 
            cal_area_circle()
    if ans1 == "2":
      ans2 = input('''คุณต้องการคำนวณหาพื้นที่ของรูปทรงอะไร
                    1.สี่เหลี่ยมผืนผ้า
                    2.สามเหลี่ยมมุมฉาก
                    3.วงกลม\n
                    ''')
      if ans2 == "1" : 
          cal_circum_rect()
      if ans2 == "2" : 
          cal_circum_tri()
      if ans2 == "3" : 
          cal_circum_circle()
    print("_______________________________________________________________________________________________________________________")
    else : 
        ans1.upper() == "Q": 
        break
print(" Bye bye <_> ")
"""