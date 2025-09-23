def add(p, q):
    return p + q
def sub(p, q):
    return p - q
def mult(p, q):
    return p * q
def div(p, q):
    return p/q

print("Please select the operation\nChoose option a: add\nChoose option b: subtract\nChoose option c: multiply\nChoose option d: divide")

choice = input("Enter your choice: ")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if choice == "a" or choice == "A":
    print(f"{num1} + {num2} = {add(num1, num2)}")
if choice == "b" or choice == "B":
    print(f"{num1} - {num2} = {sub(num1, num2)}")
if choice == "c" or choice == "C":
    print(f"{num1} * {num2} = {mult(num1, num2)}")
if choice == "d" or choice == "D":
    print(f"{num1} / {num2} = {div(num1, num2)}")
else:
    print("Invalid input")