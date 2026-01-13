a = [5,7,8,9,1,2,3,4,6]
a_size = len(a)
count = 0

for i in range(1,a_size):
    if a[i] < a[i-1]:
        count += 1
if a[a_size-1] > a[0]:
    count+=1
print(count<=1)