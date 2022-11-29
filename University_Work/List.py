#Create a list 
my_list = []                               #empty list
my_list = [1,2,3]                        #list of integers
my_list = [1, "Hello", 3.14]          #list with mixed data types
my_list = ["yes", [8,4,6], [' a ']]   #list of list
my_list = ['a', 'e', 'i', 'o' , 'u']
print(my_list[0])
print(my_list[2])
print(my_list[4])
n_list = ["happy", [2, 0, 1, 5]]       #list ซ้อน list เรียกอีกอย่างว่า array 2 มิติ
print(n_list[0][1])
print(n_list[1][3])
#print(my_list[4.0])                        #Error only int!!!!!!!!!!
#access elements from a list 
my_list = ['p', 'r', 'o', 'b', 'e']
print(my_list[-1])
print(my_list[-5])
#list slicing
my_list = ['p', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g']
print(my_list[ : ])       #elements beginning to end
print(my_list[2:5])      #elements 3rd to 5th
print(my_list[:-5])       #elements beginning to 4th
print(my_list[5:])        #elements 6th to end
#change elements to a list
even = [2, 4, 6, 8]
even[0] = 1                 #change the 1st items
print(even)
even[1:4] = [3, 5, 7]     #change 2nd to 4th items
print(even)
#add elements to a list
odd = [1, 3, 5]
odd.append(7)  #เพิ่มไปตำแหน่งท้ายสุดของ list 
print(odd)
odd.extend([9, 11, 13])  #เพิ่มไปตำแหน่งท้ายสุดของ list หลายๆตัว
print(odd)
#add elements to a list
odd = [1,3,5]
print(odd+[9,7,5])
print(["re"]*3)
#add elements to a list
odd = [1,9]
odd.insert(1,3)
print(odd)
odd[2:2] = [5,7]
print(odd)
#delete elements from a list
my_list = ['p','r','o','b','l','e','m']
del my_list[2]                                  #delete one items
print(my_list)
del my_list[1:5]                               #delete multiple items
print(my_list)
del my_list                                      #delete entire list
print(my_list)                                  #error it do not have a list
#delete elements from list
my_list = ['p','r','o','b','l','e','m']
my_list.remove('p')
print(my_list)
print(my_list.pop(1))   # pop = ดึงค่าออกมาโชว์แล้วจะถูกลบออก (1) = ตำแหน่งที่ 1
print(my_list)
print(my_list.pop())
print(my_list)
my_list.clear()            # เครียให้เป็น list ว่าง
print(my_list)
my_list = ['p','r','o','b','l','e','m']
my_list[2:3] = []
my_list
my_list[2:5] = []
my_list
#Python list methods
my_list = [3,8,1,6,0,8,4]
print(my_list.index(8))                 #ให้หาว่าเลข 8 ใน list อยู่ตำแหน่งที่เท่าไหร่ ถ้าเจอตัวไหนก่อนจะนำมาแสดง 
print(my_list.count(8))                 #นับว่าใน list มี 8 กี่ตัว
my_list.sort()                              #เรียงลำดับจากน้อยไปมาก
print(my_list)
my_list.reverse()                          #เรียงจากหลังไปหน้า
print(my_list)
#list comprehemsion
pow2 = []
for x in range(10):
  pow2.appemd(2 ** x)
  pow2 = [2**x for x in range(10)]
print(pow2)
for fruit in ['apple','banana','mango'] :
  print("I like",fruit)
power = [2**x for x in range(21)]
print(power)
for sport in ['football','swim','run'] :
  print("I like",sport)