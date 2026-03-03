def reverse(string):
    vowels = ["a","e","i","o","u"]

    result = " "

    for i in range(len(string)):
        if string[i] in vowels:
            result += " "
        else:
            result += string[i]
    return result
string = input("enter string")
print(reverse(string))