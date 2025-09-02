import sys
input = sys.stdin.readline

def draw_star(arr, x, y, n):
    if n == 1:
        arr[x][y] = '*'
        return
    
    div = n // 3
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            draw_star(arr, x + i * div, y + j * div, div)

def solve():
    n = int(input())
    result = [[' ' for _ in range(n)] for _ in range(n)]

    draw_star(result, 0, 0, n)

    print('\n'.join(''.join(row) for row in result))

solve()