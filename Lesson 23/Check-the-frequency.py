student = {'Codingal' : 2, 'is' : 2, 'best' : 2, 'for' : 2, 'Coding' :1}

checkval = int(input("Enter a number you want to check that is present in the dictionary: "))

count = 0

for key in student:
    if student[key] == checkval:
        #this will give the value of the key in the dictionary
        count += 1

print(count)