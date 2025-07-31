num = int(input("Enter the number you want as a base: "))
power = int(input("Enter the number you want to use as the exponent: "))

count = 1

for i in range(1, power + 1):
    count = count * num

print(count)
