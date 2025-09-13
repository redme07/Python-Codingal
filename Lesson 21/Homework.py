start = int(input("Enter a number: "))
end = int(input("Enter a another number larger than the first one: "))

def squares(start, end):
    for i in range(start, end+1):
        square = i * i
        
        if square % 2 == 0:
            print(f"The sqaure of {i} is {square} its even")
        else:
            print(f"The square of {i} is odd; its sqaure is {square}")
        i += 1 
        

print(squares(start, end))


    

