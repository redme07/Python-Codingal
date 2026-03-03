def swapcase(a):
    result = ""
    
    for i in a:
        if i.islower():
            result += i.upper()
        if i.isupper():
            result += i.lower()
    return result            

inp = input("enter string")
print(swapcase(inp))