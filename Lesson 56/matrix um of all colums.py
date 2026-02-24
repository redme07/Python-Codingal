x = [[1,3,3],[4,5,6],[5,6,7]]
ans = 0

for i in range(len(x)):
    for j in range(len(x[0])):
        ans += x[j][i]
    print(ans,end=" ")
    ans = 0
