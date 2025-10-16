def findwater(a,size):
    left = [0]*size
    right = [0]*size

    water = 0
    left[0] = a[0]
    for i in range(1,size):
        left[i] = max(left[i-1],a[i])
    right[size-1] = a[size-1]
    for i in range(size-2,-1,-1):
        right[i] = max(right[i+1],a[i])
    for i in range(0,size):
        water += min(left[i],right[i])-a[i]
    return water

a = [3,0,2]
size = len(a)
print(findwater(a,size))