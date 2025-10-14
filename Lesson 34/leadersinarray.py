def leaders(a,a_size):
    currentmax= a[a_size-1]
    print(currentmax)
    for i in range(a_size-2,-1,-1):
        if currentmax < a[i]:
            print(a[i])
            currentmax = a[i]
a = [13,67,48,56,90,76,43,67]
a_size = len(a)
leaders(a,a_size)