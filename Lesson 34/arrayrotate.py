def rotation(a,a_size,n):
    for i in range(n):
        rotate(a,a_size)

def rotate(a,a_size):
    temp = a[0]
    for i in range(a_size-1):
        a[i] = a[i+1]
    a[a_size-1] = temp
def printarray(a,a_size):
    for i in range(a_size):
        print(a[i],end=" ")
    print("\n")

a = [12,23,34,4,56,67,78,89]
printarray(a,len(a))
rotation(a,len(a),3)
printarray(a,len(a))
