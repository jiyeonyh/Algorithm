from collections import deque

n, m = map(int, input().split())
board = []
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for _ in range(n):
    board.append(list(map(int, input())))
    
    
def bfs(y, x):
    queue = deque()
    queue.append((1, y, x))
    
    board[y][x] = 0
    
    while queue:
        cnt, y, x = queue.popleft()

        if y == n-1 and x == m-1:
            print(cnt)
            break
            
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if ny < 0 or ny >= n or nx < 0 or nx >= m:
                continue

            if board[ny][nx] == 1:
                queue.append((cnt+1, ny, nx))
                board[ny][nx] = 0
                
bfs(0, 0)