def evod(a,size):
    cmax = 0
    max = 0

    for i in range(0,size):
        if i % 2 == 0 and i+1 % 2 == 1:
            cmax += 1
        if max < cmax:
            max = cmax
    return max

a = [1,2,3,4,5,6,7,8,9]

size = len(a)
print(evod(a,size))