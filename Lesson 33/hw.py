arr = [1, 2, 3, 4, 5, 6, 8, 9, 10]  # missing 7

n = 10
expected_sum = n * (n + 1) // 2
actual_sum = sum(arr)

missing_number = expected_sum - actual_sum
print(missing_number)