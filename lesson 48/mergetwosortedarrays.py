def mergesort(a1,a2,m,n):
    a3 = [None] * (m+n)
    i = 0
    j = 0 
    k = 0

    while i < m and j < n:
        if a1[i] < a2[j]:
            a3[k] = a1[i]
            k+=1
            i+=1
        else:
            a3[k] = a2[j]
            k+=1
            j+=1
    while i<m:
        a3[k] = a1[i]
        k+=1
        i+=1
    while j<n:
        a3[k] = a2[j]
        k+=1
        j+=1
    print("merged arrays")
    for i in range(m+n):
        print(a3[i],end = " ")

a1 = [1,3,5,7,9]
a2 = [2,4,6,8,10]
m = len(a1)
n = len(a2)
mergesort(a1,a2,m,n)