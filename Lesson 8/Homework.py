a = float(input("Enter a number which will be num1 : "))
b = float(input("Enter a number which will be num2 : "))
c = float(input("Enter a number which will be num3 : "))

#num1 = num2, num2 = num3, num3 = num1

temp = a
a = c
c = b
b = temp


print("num1 = ", a)
print("num2 = " , b)
print("num3 = ", c)



