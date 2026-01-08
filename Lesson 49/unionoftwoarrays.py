def unionoftwoarrays(a1,a2,m,n):
    i = 0
    j = 0
    while i < m and j < n:
        if a1[i] < a2[j]:
            print(a1[i],end=" ")
            i +=1
        elif a1[i] > a2[j]:
            print(a2[j],end=" ")
            j+=1
        else:
            print(a2[j],end=" ")
            i+=1 
            j+=1
    while i<m:
        print(a1[i], end=" ")
        i+=1
    while j < n:
        print(a2[j], end=" ")
        j+=1
    
a1 = [1,3,8,9]
a2 = [2,4,7,10]
m = len(a1)
n = len(a2)
unionoftwoarrays(a1,a2,m,n)