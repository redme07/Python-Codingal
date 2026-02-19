x = [[1,2,3],[4,5,6],[7,8,9]]
ans = 0

for i in range(len(x)):
    for j in range(len(x[0])):
        ans += x[i][j]
    print(ans,end=" ")
    ans = 0