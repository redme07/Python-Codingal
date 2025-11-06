def linear(a,size,num):

    for i in range(size):
        if num == a[i]:
            return i
    

    return -1

a = [2,6,9,4,7,3,1,2,0,4]
num = 4
size = len(a)

result = linear(a,size,num)

if result == -1:
    print("element is not present")
else:
    print("element is present in", result)

