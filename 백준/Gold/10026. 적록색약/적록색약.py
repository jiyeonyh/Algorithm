from collections import deque
import sys
input = sys.stdin.readline

def same_color(a, b, colorblined):
    if not colorblined:
        return a == b
    
    return (a == b) or (a in ("R", "G") and b in ("R", "G"))

def bfs(board, colorblined):
    n = len(board)
    q = deque()
    visited = [[False] * n for _ in range(n)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    cnt = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == True:
                continue

            q.append((i, j))
            visited[i][j] = True
            cnt += 1

            while q:
                x, y = q.popleft()
                for dx, dy in directions:
                    nx, ny = dx + x, dy + y
                    if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                        if same_color(board[nx][ny], board[x][y], colorblined):
                            visited[nx][ny] = True
                            q.append((nx, ny))
                
    return cnt

def solve():
    n = int(input())
    board = [input().strip() for _ in range(n)]
    print(bfs(board, False), bfs(board, True))

solve()
