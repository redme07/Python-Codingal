def substraight(str1, str2):
    if str1 in str2:
        return str2.index(str1)
    else:
        return -1
    
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

print(substraight(str1, str2))
    