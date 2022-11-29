class Stack:
  def init(self):
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
  def score(self):
    return self.data


laystack = Stack()
tempdata=1
roundofdata=0
while tempdata >0:
  print("Enter an int value(<0 to end)")
  tempdata = int(input())
  laystack.push(tempdata)
  print('Stack size =' ,laystack.length())
  print('Stack data = ',laystack.score())
#for  roundofdata in range(laystack.langth())
#print('result of pop = ', laystack.pop())