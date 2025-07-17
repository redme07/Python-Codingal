String = input("Enter a word: ")
character = input("Enter the character you want to check")

i = 0
count = 0

while i < len(String):

    if (String[i] == character):
        count += 1

    i += 1

print("The number of occurences is ",count)