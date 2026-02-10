class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None
class DLL:
    def __init__(self):
        self.head = None
    def search(self,data):
        t = 0
        temp = self.head
        while temp:
            if temp.data == data:
                t = 1
                break
            temp = temp.next
        if t == 1:
            print("element found")
        else:
            print("elemnt is not found")
    def display(self):
        if self.head == None:
            print("list is empty")
        else:
            temp = self.head
            while temp:
                print(temp.data,"-->",end=" ")
                temp = temp.next

obj = DLL()
n1 = Node(10)
obj.head = n1
n2 = Node(20)
n1.next = n2
n3 = Node(30)
n2.next = n3
n3.prev = n2
obj.display()
print(end="\n")
obj.search(20)