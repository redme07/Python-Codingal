def bubble(a):
    n = len(a)

    for i in range(n):
        swap = False
        for j in range(0,n-i-1):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
                swap = True
        if swap == False:
            break
a = [2,5,3,4,1,8,6,7,9]
bubble(a)
for i in range(len(a)):
    print(a[i])