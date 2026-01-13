def rotation(a,n,a_size):
    for i in range(n):
        rotate(a,a_size)
def rotate(a,a_size):
    temp = a[0]
    for i in range(a_size-1):
        a[i] = a[i+1]
    a[a_size-1] = temp
def printa(a, a_size):
    for i in range(a_size):
        print("%d" %a[i],end=" ")
    print("\n")

a = [1,2,3,4,5,6,7,8,9,10]
a_size = len(a)
rotation(a,2,a_size)
printa(a,a_size)
