def reverse(string):
    return string[::-1]

def reverse1(string):
    string = string.lower()
    result = reverse(string)

    if string == result:
        return True
    else:
        return False
    
inp = input("enter string")
print(reverse1(inp))