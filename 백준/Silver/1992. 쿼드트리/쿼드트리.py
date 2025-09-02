import sys
input = sys.stdin.readline

def is_uniform(board, r1, c1, r2, c2):
    first = board[r1][c1]
    for i in range(r1, r2):
        for j in range(c1, c2):
            if board[i][j] != first:
                return False, None
    return True, str(first)

def dq(board, r1, c1, r2, c2):
    uniform, val = is_uniform(board, r1, c1, r2, c2)
    if uniform:
        return val

    rm = (r1 + r2) // 2
    cm = (c1 + c2) // 2

    tl = dq(board, r1, c1, rm, cm)
    tr = dq(board, r1, cm, rm, c2)
    bl = dq(board, rm, c1, r2, cm)
    br = dq(board, rm, cm, r2, c2)

    return f"({tl}{tr}{bl}{br})"

def solve():
    n = int(input())
    video = [input().strip() for _ in range(n)]
    print(dq(video, 0, 0, n, n))

solve()