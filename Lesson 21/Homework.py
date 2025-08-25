start = int(input("Enter a number: "))
end = int(input("Enter a another number larger than the first one: "))

def squares(start, end):
    for i in range(start, end+1):
        square = i * i
        print(square)
    
    
print(squares(start, end))

