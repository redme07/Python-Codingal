n = int(input())
arr = list(map(int, input().split()))

def quicksort(a):
    if len(a) <= 1:
        return a
    pivot = a[len(a) // 2]
    left = [x for x in a if x < pivot]
    middle = [x for x in a if x == pivot]
    right = [x for x in a if x > pivot]
    return quicksort(left) + middle + quicksort(right)

sorted_arr = quicksort(arr)
print(*sorted_arr)