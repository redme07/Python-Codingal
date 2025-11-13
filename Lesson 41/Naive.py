def naive(x,n,a):
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if a[j] + a[i] == x:
                return a[i],a[j]
            if a[i] + a[j] > x:
                break
    return 0

a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
x = 25
n = len(a)
print(naive(x,n,a))
