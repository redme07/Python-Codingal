def getone(a,size):
    counter = 0
    one = 0

    for i in range(0,size):
        if a[i] == 1:
            counter+=1
            one = max(counter,one)
            
        else:
            counter = 0
    return one
a = [0,1,1,0,1,1,1,0,0,0,1,1,1,1,1,0]
size = len(a)
print(getone(a,size))