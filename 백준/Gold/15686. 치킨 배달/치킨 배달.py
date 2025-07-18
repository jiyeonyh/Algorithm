from itertools import combinations
import sys
input = sys.stdin.readline

def get_locations(board):
    houses = []
    restaurants = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 1:
                houses.append((i, j))
            elif board[i][j] == 2:
                restaurants.append((i, j))
    return houses, restaurants

def solve():
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    houses, restaurants = get_locations(board)

    result = 9999
    for comb in combinations(restaurants, m):
        sum_dist = 0
        for h in houses:
            min_dist = 9999
            for i in range(m):
                min_dist = min(min_dist, abs(comb[i][0] - h[0]) + abs(comb[i][1] - h[1]))
            sum_dist += min_dist
        result = min(result, sum_dist)

    print(result)


solve()
