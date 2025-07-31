num = int(input("Enter a number: "))


if num == 0:
    print("Binary representation: 0")
else:
    binary = ""
    n = num 
    while n > 0:
        remainder = n % 2
        binary = str(remainder) + binary
        n = n // 2

    print("Binary representation:", binary)