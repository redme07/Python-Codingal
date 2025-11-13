arr = [1, 3, 4, 7, 10]
target = 15
arr.sort()

left = 0
right = len(arr) - 1
closest_sum = float('inf')
pair = (0, 0)

while left < right:
    curr_sum = arr[left] + arr[right]
    if abs(target - curr_sum) < abs(target - closest_sum):
        closest_sum = curr_sum
        pair = (arr[left], arr[right])
    if curr_sum < target:
        left += 1
    else:
        right -= 1

print("The pair with sum closest to", target, "is", pair, "with sum", closest_sum)






