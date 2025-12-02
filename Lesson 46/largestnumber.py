a = [1,2,4,6,8,9]
b = [1,3,4,5,7,10]

c = len(a)
d = len(b)

i = 0
j = 0

while i < c and j<d:
    if a[i]>b[j]:
        j+=1
    elif a[i]<b[j]:
        i+=1
    else:
        print(b[j])
        i+=1
        j+=1
