str = input("enter a sentence:")

def sentence(str):
    count = 0
    str = str.strip()
    for i in range(len(str)):
        if str[i] == " ":
            count+=1
    return count+1    

print(sentence(str))