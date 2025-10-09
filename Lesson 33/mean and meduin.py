def arrmean(arrsize, arr):
    sum = 0

    for i in range(0,arrsize):
        sum = sum + arr[i]
    return sum/arrsize

def arrmedian(arrsize, arr):
    
    sorted(arr)

    if arrsize % 2 !=0:
        return arr[int(arrsize/2)]

    return (arr[int(arrsize-1)/2]+arr[int(arrsize)/2])/2

arr = [2,5,3,8,5,0,13]
arrsize = len(arr)

print(arrmean(arrsize,arr), arrmedian(arrsize,arr))
