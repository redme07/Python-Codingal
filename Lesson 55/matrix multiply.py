x = [[8,5],[6,4]]
y = [[7,1],[9,2]]
answer = [[0,0],[0,0]]

for i in range(len(x)):
    for j in range(len(y[0])):
        for k in range(len(y)):
            answer[i][j] += x[i][k] * y[k][j]

for i in answer:
    print(i)