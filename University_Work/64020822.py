class Stack:
  def __init__(self): 
    self.data = []
  def push(self,dat): 
    self.data.append(dat)
  def pop(self):
    return self.data.pop()
  def isEmpyt(self):
    return self.data == []
  def length(self): 
    return len(self.data)
  def peek(self): 
    return self.data[-1]
  def memberofdata(self): 
    return self.data

HoangStack = Stack()
inputdata = 1
roundofdata = 0 
print("_______________________________________________")
while inputdata > 0:
    inputdata = int(input('Enter an int value (If enter < 1 = end) : '))
    if inputdata >= 1:
        HoangStack.push(inputdata)
        print('Stack size =' , HoangStack.length())
        print('Stack member data = ', HoangStack.memberofdata())
if inputdata <= 0:
  print("____________________________________________________\n")
  print('Stack member data = ', HoangStack.memberofdata())
  print("The last member of list = ", HoangStack.peek())
print("Is list Empty ? = ", HoangStack.isEmpyt())
for roundofdata in range(HoangStack.length()):
  print('Result of pop = ', HoangStack.pop())
