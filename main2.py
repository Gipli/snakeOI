def printmap():
    for i in range(snakeNum):
        board[snakeX[i]][snakeY[i]] = snakeC[i]
    for row in board:
        print(row)


data = str(input())
data = data.split()
print(data)
m = int(data[0])
p = int(data[1])
n = int(data[2])
board = [['-1' for i in range(m)] for j in range(m)]
for i in range(p):
    data = str(input())
    data = data.split()
    x = int(data[0]) - 1
    y = int(data[1]) - 1
    color = int(data[2])
    board[x][y] = color
snakeX = [0]
snakeY = [0]
snakeC = [0]

snakeNum = 0
for j in range(n):
    data = str(input())
    data = data.split()
    if data[0] == 'Z':
        print(board[int(data[1])][int(data[2])])
    if data[0] == 'P':
        if board[snakeX[snakeNum]][snakeY[snakeNum] + 1] != -1:
            snakeX.append(snakeX[snakeNum])
            snakeY.append(snakeY[snakeNum] + 1)
            snakeC.append(board[snakeX[snakeNum]][snakeY[snakeNum] + 1])
            snakeNum += 1
        else:
            for i in range(snakeNum):
                snakeX[i] = snakeX[i + 1]
                snakeY[i] = snakeY[i + 1]
            snakeY[snakeNum] = snakeY[snakeNum] + 1
    if data[0] == 'G':
        if board[snakeX[snakeNum]][snakeY[snakeNum] + 1] != -1:
            snakeX.append(snakeX[snakeNum] + 1)
            snakeY.append(snakeY[snakeNum])
            snakeC.append(board[snakeX[snakeNum] + 1][snakeY[snakeNum]])
            snakeNum += 1
        else:
            for i in range(snakeNum):
                snakeX[i] = snakeX[i + 1]
                snakeY[i] = snakeY[i + 1]
            snakeX[snakeNum] = snakeX[snakeNum] - 1
    if data[0] == 'D':
        if board[snakeX[snakeNum]][snakeY[snakeNum] + 1] != -1:
            snakeX.append(snakeX[snakeNum] - 1)
            snakeY.append(snakeY[snakeNum])
            snakeC.append(board[snakeX[snakeNum] - 1][snakeY[snakeNum]])
            snakeNum += 1
        else:
            for i in range(snakeNum):
                snakeX[i] = snakeX[i + 1]
                snakeY[i] = snakeY[i + 1]
            snakeX[snakeNum] = snakeX[snakeNum] + 1
    if data[0] == 'L':
        if board[snakeX[snakeNum]][snakeY[snakeNum] + 1] != -1:
            snakeX.append(snakeX[snakeNum])
            snakeY.append(snakeY[snakeNum] - 1)
            snakeC.append(board[snakeX[snakeNum]][snakeY[snakeNum] - 1])
            snakeNum += 1
        else:
            for i in range(snakeNum):
                snakeX[i] = snakeX[i + 1]
                snakeY[i] = snakeY[i + 1]
            snakeY[snakeNum] = snakeY[snakeNum] - 1
        printmap()



