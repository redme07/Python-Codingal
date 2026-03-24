rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []

for i in range(rows):
    row = list(map(int, input(f"Enter elements of row {i+1} separated by space: ").split()))
    matrix.append(row)

for i in range(rows):
    row_sum = sum(matrix[i])
    print(f"Sum of row {i+1} = {row_sum}")