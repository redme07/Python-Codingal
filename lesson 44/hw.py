arr = list(map(int, input().split()))
n = len(arr)

max_product = arr[0] * arr[1]
pair = (arr[0], arr[1])

for i in range(n):
    for j in range(i + 1, n):
        if arr[i] * arr[j] > max_product:
            max_product = arr[i] * arr[j]
            pair = (arr[i], arr[j])

print(pair[0], pair[1])