class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class singyLLy:
    def __init__(self):
        self.head = None
    def swap(self,n1,n2):
        prevnode = None
        prevnode2 = None
        node1 = self.head
        node2 = self.head
        if self.head == None:
            return 
        if n1 == n2:
            return 
        while node1 != None and node1.data != n1:
            prevnode = node1
            node1 = node1.next
        while node2!= None and node2.data != n2:
            prevnode2 = node2
            node2 = node2.next
        if node2 != None and node1 != None:
            if prevnode != None:
                prevnode.next = node2
            else:
                self.head = node2 
            if prevnode2 != None:
                prevnode2.next = node1
            else:
                self.head = node1
            temp = node1.next
            node1.next = node2.next
            node2.next = temp
        else:
            print("swapping not possible")

    def display(self):
        if self.head == None:
            print("empty")
        else:
            temp = self.head
            while temp:
                print(temp.data, "-->", end=" ")
                temp = temp.next

l = singyLLy()
n = Node(10)
l.head = n
n1 = Node(20)
n.next = n1
n2 = Node(30)
n1.next = n2
n3 = Node(40)
n2.next = n3
l.display()
print(end="\n")
l.swap(10,30)
l.display()


            
 


