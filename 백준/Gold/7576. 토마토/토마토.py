import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())
ripe_tomatoes = deque()
matrix = []

def bfs(queue):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] == 0:
                matrix[nx][ny] = matrix[x][y] + 1
                queue.append((nx, ny))

def find_days():
    result = 0
    for row in matrix:
        for value in row:
            if value == 0:
                return -1
            result = max(result, value)
    return result - 1 

def solve():
    for i in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)
        for j in range(m):
            if row[j] == 1:
                ripe_tomatoes.append((i, j))

    bfs(ripe_tomatoes)
    print(find_days())

solve()