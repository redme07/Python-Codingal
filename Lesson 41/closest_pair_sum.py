def close(x,n,a):
    diff = 99999999999999999
    i = 0
    j = n-1
    counter = 0
    while i < j:
        if a[i] + a[j] == x:
            continue
        if a[i] +a[j] != x:
            if a[i] + a[j] < x:
                counter = x - a[i] + a[j]
                if counter < diff:
                    diff = counter
                i += 1
            if a[i] + a[j] > x:
                counter = a[i] + a[j] - x
                if counter < diff:
                    diff = counter
                j-=1
            else:
                print("error")
        
    return diff

a = [1,2,3,4,5,6,7,8,9,10]
n = len(a)
x = 10

print(close(x,n,a))