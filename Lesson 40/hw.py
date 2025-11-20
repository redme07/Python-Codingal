arr = [1, 3, 5, 7, 9, 11, 13, 15]
target = 9

low = 0
high = len(arr) - 1
found = -1

while low <= high:
    mid = (low + high) // 2
    if arr[mid] == target:
        found = mid
        break
    elif arr[mid] < target:
        low = mid + 1
    else:
        high = mid - 1

if found != -1:
    print("Element found at index", found)
else:
    print("Element not found in the array.")