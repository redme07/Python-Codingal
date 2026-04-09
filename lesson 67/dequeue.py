class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
class dequeue:
    def __init__(self):
        self.front = self.rear = None
    def isempty(self):
        return self.front == None
    def insertfront(self,data):
        newnode = Node(data)
        if self.front == None:
            self.front = self.rear = newnode
            return
        newnode.next = self.front
        self.front.prev = newnode
        self.front = newnode
    def insertrear(self,data):
        newnode = Node(data)
        if self.rear == None:
            self.front = self.rear = newnode
            return
        self.rear.next = newnode
        newnode.prev = self.rear
        self.rear = newnode
    def deletefront(self):
        if self.isempty():
            print("queue is empty")
            return
        temp = self.front
        self.front = temp.next
        if self.front == None:
            self.rear = None
        else:
            self.front.prev = None
    def deleterear(self):
        if self.isempty():
            print("queue is empty")
            return
        temp = self.rear
        self.rear = temp.prev
        if self.rear == None:
            self.front = None
        else:
            self.rear.next = None
if __name__ == "__main__":
    q = dequeue()
    q.insertrear(10)
    q.insertrear(50)
    q.insertrear(76)
    q.deleterear()
    q.insertfront(20)
    q.insertfront(30)
    q.deletefront()
    print("queue front", q.front.data)
    print("rear element",q.rear.data)