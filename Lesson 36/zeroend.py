def zero(a,size):
    count = 0

    for i in range(len(a)-1,-1,-1):
        if a[i] == 0:
            count +=1
            a.pop(i)
    a.extend([0]*count)
    return a

a = [0,1,3,5,0,2,0,4,5,0,4,5,0,2]
size = len(a)
print(zero(a,size))