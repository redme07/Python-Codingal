num = int(input("Enter a number"))

def fac(number):

    if number == 1 or number == 0:
        return 1
    else:
        return number * fac(number - 1)
    
print(fac(num))