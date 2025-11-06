def linear(a,size,num):
    last = -1

    for i in range(size):
        if a[i] == num:
            last = i
    
    return last

a = [1,6,3,8,4,0,7,2,3,4,8,5]
num = 8
size = len(a)
print(linear(a,size,num))