class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None
class DLL:
    def __init__(self):
        self.head = None
    def insertbeg(self,data):
        nb = Node(data)
        nb.next = self.head
        self.head = nb
    def insertend(self,data):
        ne = Node(data)
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = ne
        ne.prev = temp
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
l.insertbeg(50)
l.display()
print("\n")
l.insertend(40)
l.display()
