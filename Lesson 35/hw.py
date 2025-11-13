arr = [2, 4, 7, 4, 9, 4, 5]
target = 4
last_index = -1

for i in range(len(arr)):
    if arr[i] == target:
        last_index = i

if last_index != -1:
    print("The last occurrence of", target, "is at index", last_index)
else:
    print("Element not found in the array.")






