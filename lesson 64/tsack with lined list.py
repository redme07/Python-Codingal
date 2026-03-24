class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class stack:
    def __init__(self):
        self.head = None
    def isempty(self):
        return True if self.head == None else False
    def push(self,data):
        if self.head == None:
            self.head = Node(data)
        else:
            new = Node(data)
            new.next = self.head
            self.head = new
    def topelement(self):
        if self.isempty():
            return None
        else:
            return self.head.data
    def pop(self):
        if self.isempty():
            return None
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            return temp.data
obj = stack()
obj.push(5)
obj.push(7)
obj.push(9)
obj.push(11)
print(obj.topelement())
print(obj.pop())