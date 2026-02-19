x = [[1,8,9],[4,2,1],[6,5,4]]
ans = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(x)):
    for j in range(len(x[0])):
        ans[i][j] = x[j][i]
for i in ans:
    print(i)