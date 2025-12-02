a = [9,8,3,6,7,1,4,2,5]
n = len(a)
inter = n//2

while inter > 0:
    for i in range(inter,n):
        j = i
        temp = a[i]
        while j>=inter and a[j-inter]>temp:
            a[j] = a[j-inter]
            j-=inter
        a[j] = temp

    inter //= 2
print(a)