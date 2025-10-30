arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

start = 0
end = len(arr) - 1

while start < end:
    # swap elements
    arr[start], arr[end] = arr[end], arr[start]
    start += 1
    end -= 1

print(arr)
