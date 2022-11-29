class Node:
    def __init__(self,item):
        self.data = item
        self.next = None
    def getData(self):
        return self.data
    def setData(self,newitem):
        self.data = newitem
    def getNext(self):
        return self.next
    def setNext(self,newnext):
        self.next = newnext

class Unorderedlist: 
    def __init__(self):
        self.head = None
        #self.count = 0
    def inEmpty(self):
        return self.hand == None
    def add(self,item):
        temp = Node(item)
        temp = Node.setNext(self.head)
        self.head = temp
        #self.count += 1
    def remove(self,item):
        current = self.head
        previous = None
        found = False #Flag
        while not found :
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
            if previous == None:
                self.head ==current.getNext()
            else:
                previous.setNext(current.getNext())
    def size(self):
        current = self.head
        count = 0
        while current != None :
            count += 1
            current = current.getNext()
            return count
    def search(self,item):
        current = self.head
        found = False #flag
        while current.getData() != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found
    def remove(self,item):
        current = self.head
        previous = None
        found = False #flag
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None :
            self.head = current.getNext()
        else :
            previous.setNext(current.getNext())
    def append (self,item):
        temp = Node(item)
        if self.head == None:
            self.head = temp
        else:
            current = self.head
            while current.getNext() != None:
                current = current.getNext()
            current.setNext(temp)
    def index(self,item):
        current = self.head
        found = False
        pos = 0
        while not found :
            if current.getData() == item :
                found = True
            else:
                pos += 1
            current = current.getNext()
        return pos