word = input("Enter a sentence")

total = 1

for i in range(len(word)):
    if(word[i] == ' '):
        total = total + 1
print("The number of words in the sentance is equal to ",total)