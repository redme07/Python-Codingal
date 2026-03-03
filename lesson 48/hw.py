n = int(input())
arr = list(map(int, input().split()))

def mergesort(a):
    if len(a) <= 1:
        return a
    
    mid = len(a) // 2
    left = mergesort(a[:mid])
    right = mergesort(a[mid:])
    
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

sorted_arr = mergesort(arr)
print(*sorted_arr)