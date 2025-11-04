def evod(a,size):
    cmax = 0
    max = 0

    for i in range(0,size):
        if a[i] % 2 == 0 and a[i] % 2 == 1:
            cmax += 1
        if max < cmax:
            max = cmax
    return max

a = [0,1,4,8,5,9,6,7,8,3,6,1,8,6]

size = len(a)
print(evod(a,size))