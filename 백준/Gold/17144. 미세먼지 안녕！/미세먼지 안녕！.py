import sys
input = sys.stdin.readline

def find_cleaner():
    for i in range(r):
        for j in range(c):
            if board[i][j] == -1:
                cleaner.append(i)
                cleaner.append((i + 1))
                return

def spread():
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    new_board = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if board[i][j] > 0:
                amount = board[i][j] // 5
                spread_count = 0
                for dx, dy in directions:
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < r and 0 <= ny < c and board[nx][ny] != -1:
                        new_board[nx][ny] += amount
                        spread_count += 1
                new_board[i][j] += board[i][j] - (amount * spread_count)
            elif board[i][j] == -1:
                new_board[i][j] = -1
    return new_board

def clean():
    upper_x = cleaner[0]
    lower_x = cleaner[1]

    for i in range(upper_x - 1, 0, -1):
        board[i][0] = board[i-1][0]
    
    for i in range(c-1):
        board[0][i] = board[0][i+1]

    for i in range(upper_x):
        board[i][c-1] = board[i+1][c-1]

    for i in range(c-1, 1, -1):
        board[upper_x][i] = board[upper_x][i-1]
    board[upper_x][1] = 0

    for i in range(lower_x+1, r-1):
        board[i][0] = board[i+1][0]
    
    for i in range(c-1):
        board[r-1][i] = board[r-1][i+1]
    
    for i in range(r-1, lower_x, -1):
        board[i][c-1] = board[i-1][c-1]
    
    for i in range(c-1, 1, -1):
        board[lower_x][i] = board[lower_x][i-1]
    board[lower_x][1] = 0 

r, c, t = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(r)]
cleaner = []

find_cleaner()
for _ in range(t):
    board = spread()
    clean()
result = sum(sum(row) for row in board)
print(result + 2)