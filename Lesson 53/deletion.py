class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None
class DLL:
    def __init__(self):
        self.head = None
    def bdelete(self):
        if self.head != None:
            temp = self.head
            self.head = self.head.next
            self.head.prev = None
            temp = None
    def edelete(self):
        if self.head!= None:
            if self.head.next == None:
                self.head = None
            else:
                temp = self.head
                while temp.next.next:
                    temp = temp.next
                temp.next = None
    def display(self):
        if self.head == None:
            print("list is empty")
        else:
            temp = self.head
            while temp:
                print(temp.data,"-->",end=" ")
                temp = temp.next

l = DLL()
n = Node(10)
l.head = n
n1 = Node(20)
n.next = n1
n2 = Node(30)
n1.next = n2
n1.prev = n
l.display()
print("\n")
l.bdelete()
l.display()
print("\n")
l.edelete()
l.display()

    
