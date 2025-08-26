dictionary = {"codingal":  3,"is":  2,"best": 2,"for": 2,"coding": 1}

print(dictionary)

checkval = int(input("Which value would you like to check"))

count = 0

for key in dictionary:
    if dictionary[key] == checkval:
        count+=1

print(count)