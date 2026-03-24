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

def display(head):
    temp = head
    while temp:
        print(temp.data, end=" ")
        temp = temp.next

n = int(input())
arr = list(map(int, input().split()))

head = create_dll(arr)
display(head)