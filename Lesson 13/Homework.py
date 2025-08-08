def mirrored_right_angled_triangle(n):
    for i in range(1, n + 1):
        # print spaces
        print(' ' * (n - i), end='')
        # print stars
        print('*' * i)

# Example usage
rows = int(input("Enter the number of rows: "))
mirrored_right_angled_triangle(rows)