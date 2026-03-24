class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def create_list(arr):
    head = Node(arr[0])
    temp = head
    for i in range(1, len(arr)):
        temp.next = Node(arr[i])
        temp = temp.next
    return head

def reverse(head):
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev

def print_list(head):
    temp = head
    while temp:
        print(temp.data, end=" ")
        temp = temp.next

n = int(input())
arr = list(map(int, input().split()))

head = create_list(arr)
head = reverse(head)
print_list(head)