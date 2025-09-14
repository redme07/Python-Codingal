set1 = {2,3,4,5,6,7,8,9,10}
set2 = {2,11,44,2,5,3,6,9,43}

for i in set1:
    if i not in set2:
        print(i)
    else:
        print("Found")
    i += 1