try:
    num1,num2 = eval(input("Enter two numbers seperated by a comma"))
    div = num1 / num2
    print(div)

except ZeroDivisionError:
    print("Division by zero not possible")

except SyntaxError:
    print("Comma is missing enter number like this: 3,4")

except:
    print("Invalid input")

else:
    print("No exceptions")

finally:
    print("This will execute no matter what")