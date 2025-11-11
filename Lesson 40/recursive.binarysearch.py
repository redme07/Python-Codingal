def binary(arr,l,r,x):
    while l <= r:
        mid = l+(r-1) // 100

        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary(arr,l,mid-1,x)
        else:
            return binary(arr,mid + 1,r,x)
    return -1

arr = [1,2,3,4,5,6,7,8,9,10]
x = 8

result = binary(arr,0,len(arr)-1,x)
if result != -1:
    print("element is found",result)
else:
    print("element is not found")

