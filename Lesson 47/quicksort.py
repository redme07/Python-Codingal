def partition(a,low,high):
    i = low-1
    pivot = a[high]

    for j in range(low,high):
        if a[j] <= pivot:
            i += 1
            a[j],a[i] = a[i],a[j]
        
    a[i+1],a[high] = a[high],a[i+1]

    return i+1
def quicksort(a,low,high):
    if low<high:
        pivot = partition(a,low,high)
        quicksort(a,low,pivot-1)
        quicksort(a,pivot+1,high)

a = [18,22,3,11,96,45,23]
print(a)
n = len(a)-1
quicksort(a,0,n)
print(a)
