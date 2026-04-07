ar = [0 for _ in range(10)]
n = 10

rear = -1
front = -1

def enqueue(x):
    global n
    global rear
    global front

    if rear == n-1:
        print("overflow \n")
        return ""
    else:
        if front == -1 and rear == -1:
            front = 0
            rear = 0
        else:
            rear += 1
        ar[rear] = x
        print("element inserted")
def dequeue():
    global n
    global rear
    global front
    if front == -1 and rear == -1:
        print("undeflow \n")
       
        return 
    else:
        x = ar[front]
        print("element delted from queue is", x)
        if front == rear:
            front = -1
            rear = -1
        else:
            front += 1

def display():
    global n
    global rear
    global front
    if front == -1:
        print("queue is empty \n",end =" ")
    else:
        print("elements are" )
        i = front
        while i <= rear:
            print(ar[i],end=" ")
            i += 1
        print("\n")
def fronte():
    global n
    global rear 
    global front
    if front == -1:
        print("queue is empty \n")
    else:
        print("front element is", ar[front])
    
ch = None
print("1.inserting element in queue")
print("2.delteing elmement from the queue")
print("3.displaying the queue")
print("4.front element of the queue")
print("5.exit fromt the program")
while ch != 0:
    ch = int(input("enter your choice"))
    if ch == 1:
        x = int(input("enter the element to be inserted"))
        enqueue(x)
    elif ch == 2:
        dequeue()
    elif ch == 3:
        display()
    elif ch == 4:
        fronte()
    elif ch == 5:
        print('exiting from the program')
    else:
        print("invalid choice")