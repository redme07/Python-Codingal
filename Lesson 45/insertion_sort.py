def insertion(a):
    for i in range(1,len(a)):
        value = a[i]
        j = i-1

        while j >= 0 and value < a[j]:
            a[j+1] = a[j]
            j-=1
            a[j+1] = value
    return a

a = [10,4,3,15,8]
print(insertion(a))
