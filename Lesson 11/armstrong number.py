n = int(input("Enter a number"))

temp = n

sum = 0

while temp>0:
    digit = temp%10
    sum = sum + digit**3
    temp = temp//10

if(n == sum):
    print("The number is an armstrong number")

else:
    print("The number is not an armstrong number")

