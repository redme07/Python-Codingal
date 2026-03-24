class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

def create_dll(arr):
    head = Node(arr[0])
    temp = head
    for i in range(1, len(arr)):
        new = Node(arr[i])
        temp.next = new
        new.prev = temp
        temp = new
    return head

def insert_after(head, pos, val):
    temp = head
    for _ in range(pos):
        temp = temp.next
    
    new = Node(val)
    new.next = temp.next
    new.prev = temp
    
    if temp.next:
        temp.next.prev = new
    
    temp.next = new
    return head

def display(head):
    temp = head
    while temp:
        print(temp.data, end=" ")
        temp = temp.next

n = int(input())
arr = list(map(int, input().split()))
pos = int(input())
val = int(input())

head = create_dll(arr)
head = insert_after(head, pos, val)
display(head)