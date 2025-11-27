def evod(a,size):
    cmax = 0
    max = 0
    a2 = []
    for i in range(0,size):
        if a[i] % 2 == 0 and a[i+1] % 2 == 1:
            cmax += 1
            a2.append(a[i])
            a2.append(a[i+1])
        if max < cmax:
            max = cmax
    return a2

a = [1,2,3,4,5,6,7,8,9]

size = len(a)
print(evod(a,size))