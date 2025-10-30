def caden(a,size):
    max = -9999999999999
    cmax = 0

    for i in range(0,size):
        cmax = cmax + a[i]

        if max < cmax:
            max = cmax
        if cmax < 0:
            cmax = 0
        
    return max

a = [1,2,7,4,9,-1,-8,6,3,-4]
size = len(a)
print(caden(a,size))