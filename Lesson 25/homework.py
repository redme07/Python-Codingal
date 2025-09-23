inp = int(input("enter a range"))

odd = [i for i in range(inp) if i % 2 != 0]
print(odd)

even = [i for i in range(inp) if i % 2 == 0]
print(even)

fruits = ["mango", "apple", "strawberry", "mango"]

fruit = [i.capitalize() for i in fruits]
print(fruit)