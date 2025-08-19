list = [2, 4, 3, 5, 6, 1, 8, 9, 7]

sum = 0

for i in list:
    sum = sum + i

avg = sum/len(list)

print("The sum of the list is", sum)
print("The average of the list is", avg)

list.sort()

print("The smallest number is", list[0])
print("The largest number is", list[-1])