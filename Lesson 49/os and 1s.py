def zeroandone(a,leng):
    count = 0
    count1 = 0
    for i in range(leng):
        if a[i] == 0:
            count +=1
    for i in range(count):
        a[i] = 0
    for i in range(count,leng):
        a[i] = 1
    return a

a = [1,0,1,0,1,1,1,0,0,1,1,0,0,0,0]
leng = len(a)
print(zeroandone(a,leng))

            
        