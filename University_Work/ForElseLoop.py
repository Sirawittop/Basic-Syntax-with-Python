#For-else loop
for i in range(1,4):
  print(i)
else:       #Executed because no break in for 
  print("No break\n")
for i in range(1,4):
  print(i)
  break
else:       #Not executed as there is a beark
  print("No break")
  #while loop
count = 0 
while (count < 3):
  count = count+1
  print("hello")
print()
a = [1,2,3,4]
while a:
  print(a.pop())
count = 0
while (count <3 ): count += 1 ; print("hello")
i = 0
a = "computer science"
while i < len(a):
  if a[i] == 'c' or a[i] =='s'  or a[i] == 'e' :
    i += 1
    continue
  print('current Letter  :',a[i])
  i += 1
  i = 0
a = "computer science"
while i < len(a) :
  if a[i] =='o' or a[i] == 's':
    i += 1
    break
  print("Current Letter  :",a[i])
  i += 1
  i = 0
a = "computer science"
while i < len(a) :
  i +=1
  pass
print('Value of i :',i)
i = 0 
while i< 4:
  i += 1
  print(i)
else:
  print("not break\n")
  i = 0
while i < 4:
    i  += 1
    print(i)
    break
else :
   print("no break")