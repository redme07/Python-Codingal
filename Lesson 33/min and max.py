def minimum(a,size):
    temp = a[0]

    for i in range(1,size):
        temp = min(temp, a[i])
    return temp
def maximum(a,size):
    temp2 = a[0]

    for i in range(1,size):
        temp2 = max(temp2, a[i])
    return temp2

a = [1,4,2,6,8,4,9]
size = len(a)

print(minimum(a,size),maximum(a,size))