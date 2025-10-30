def caden(a,size):
    max = -99999999999
    cmax = 0

    for i in range(0,size):
        cmax += a[i]

        if cmax > max:
            max = cmax
        if cmax < 0:
            cmax = 0
    return max

def maxcircularsum(a):
    n = len(a)
    max_kaden = caden(a,n)
    max_wrap = 0

    for i in range(n):
        max_wrap += a[i]
        a[i] = -a[i]

    max_wrap += caden(a,n)
    if max_wrap > max_kaden:
        return max_wrap
    else:
        return max_kaden

a = [0,2,6,-4,8,-7,-4,3,5,8]
print(maxcircularsum(a))
