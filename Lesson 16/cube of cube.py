number = int(input("Enter a number: "))

def cube(number):
    return number ** 3

def three(number):
    if number % 3 == 0:
        return cube(number)
    
    else:
        return False
    

print(three(number))
