num = int(input("Enter a number"))
print(type(num))
if(type(num) is int):
    print("The number is integer")

elif(type(num)is not float):
    print("The number is not float")

else:
    print("False")

x = 20
y = 20

if(x is y):
    print("X and Y are equal")

y = 56

if(x is not y):
    print("They are not equal")