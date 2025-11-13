def pointer(x,n,a):

    i = 0
    j = n-1

    while i < j:
        if a[i] + a[j] == x:
            return a[i],a[j]
        elif a[i] + a[j] < x:
            i += 1
        else:
            j -= 1
    return 0

a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
n = len(a)
x = 25
print(pointer(x,n,a))