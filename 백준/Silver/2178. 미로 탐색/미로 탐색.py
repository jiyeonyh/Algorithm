from collections import deque
import copy

def read_input():
    n, m = map(int, input().split())
    board = []

    for _ in range(n):
        line = input().strip()
        board.append([int(char) for char in line])

    return n, m, board

def is_valid_position(x, y, n, m):
    return 0 < x <= n and 0 < y <= m

def get_neighbors(x, y, n, m):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    neighbors = []

    for dx, dy in directions:
        next_x, next_y = x + dx, y + dy
        if is_valid_position(next_x, next_y, n, m):
            neighbors.append((next_x, next_y))

    return neighbors

def bfs_shortest_path(board, start_x, start_y, end_x, end_y):
    copy_board = copy.deepcopy(board)

    queue = deque()
    queue.append((start_x, start_y))

    while queue:
        cur_x, cur_y = queue.popleft()

        if cur_x == end_x and cur_y == end_y:
            return copy_board[cur_x-1][cur_y-1]

        for next_x, next_y in get_neighbors(cur_x, cur_y, end_x, end_y):
            if  copy_board[next_x-1][next_y-1] == 1:
                copy_board[next_x-1][next_y-1] = copy_board[cur_x-1][cur_y-1] + 1

                queue.append((next_x, next_y))

def solve():
    n, m, board = read_input()

    result = bfs_shortest_path(board, 1, 1, n, m)

    print(result)


solve()
