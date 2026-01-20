class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class singyll:
    def __init__(self):
        self.head = None
    def insertbeg(self,data):
        nb = Node(data)
        nb.next = self.head
        self.head = nb
    def inserend(self,data):
        ne = Node(data)
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = ne
    def display(self):
        if self.head == None:
            print("list is empty")
        else:
            temp = self.head
            while temp:
                print(temp.data)