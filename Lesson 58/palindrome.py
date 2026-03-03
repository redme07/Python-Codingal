string = "malayalam"

mid = len(string)//2

for i in range(0,mid):
    for j in range(-1,mid,-1):
        if string[i] == string[j]:
            print("palindrome")
            break