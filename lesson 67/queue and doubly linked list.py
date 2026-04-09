class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class queue:
    def __init__(self):
        self.front = self.rear = None
    def isempty(self):
        return self.front == None
    def enqueue(self,data):
        newnode = Node(data)
        if self.rear == None:
            self.front = self.rear = newnode
            return
        self.rear.next = newnode
        self.rear = newnode
    def dequeue(self):
        if self.isempty():
            print("queue is empty")
            return
        temp = self.front
        self.front = temp.next
        if self.front == None:
            self.rear = None

if __name__ == "__main__":
    q = queue()
    q.enqueue(10)
    q.enqueue(20)
    q.dequeue()
    q.enqueue(30)
    q.enqueue(40)
    q.dequeue()
    print("queue front", q.front.data)
    print("rear element", q.rear.data)