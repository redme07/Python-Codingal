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

def search(head, key):
    temp = head
    while temp:
        if temp.data == key:
            return True
        temp = temp.next
    return False

n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements: ").split()))
key = int(input("Enter element to search: "))

head = create_list(arr)

if search(head, key):
    print("Found")
else:
    print("Not Found")