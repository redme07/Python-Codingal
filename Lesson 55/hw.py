x = [[1,2],[3,4],[4,5],[7,8]]
y = [[5,4],[6,7],[7,8],[9,7]]
answer = [[0,0],[0,0],[0,0],[0,0]]

for i in range(len(x)):
    for j in range(len(x[0])):
        answer[i][j] = y[i][j] - x[i][j]

for i in answer:
    print(i)        