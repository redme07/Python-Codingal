def equal(a):
    left = 0
    right = 0
    n = len(a)
    for i in range(n):
        left = 0
        right = 0 

        for j in range(i):
            left += a[i]
        
        for j in range(i+1,n):
            right += a[i]
        
        if left == right:
            return i
    return -1

a = [1,5,7,4,8,2,3]

print(equal(a))        