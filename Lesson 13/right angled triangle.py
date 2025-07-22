print("Right angled triangle")

n = int(input("Enter number of rows"))

for i in range(n):

    for a in range(i+1):
        print("*", end=" ")

    print()