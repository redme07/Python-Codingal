x= [[8,2],[4,2]]
y = [[4,2],[3,1]]
answer= [[0,0],[0,0]]
for i in range(len(x)):
    for j in range(len(x[0])):
        answer[i][j] = x[i][j] + y[i][j]
for i in answer:
    print(i)