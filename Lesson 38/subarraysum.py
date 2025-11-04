def subarray(a,sum,n):
    n = len(a)
    for i in range(n):
        cmax = a[i]

        j = i+1

        while j<=n:
            if cmax == sum:
                print("sum found")
                print(i, j-1)
                return 1
            if cmax > sum or j == n:
                break
            cmax += a[j]

            j+=1
    print("no subarray found")
    return 0

a = [1,5,3,9,5,2,8,0,2,1]
sum = 17
n = len(a)
print(subarray(a,sum,n))
