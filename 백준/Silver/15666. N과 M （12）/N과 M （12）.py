import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(set(map(int, input().split())))
arr.sort()
result = []

def dfs(depth, cur_index, m, stack):
    global result
    if depth == m:
        result.append(list(stack))
        return
    
    for i in range(cur_index, len(arr)):
        stack.append(arr[i])
        dfs(depth+1, i, m, stack)
        stack.pop()
        
def solve():
    for i in range(len(arr)):
        dfs(1, i, m, deque([arr[i]]))

    for row in result:
        print(' '.join(map(str, row)))

solve()