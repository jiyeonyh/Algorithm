import sys
from collections import deque
input = sys.stdin.readline

def dfs(node):
    visited[node] = True
    count = 1
    for next_node in graph[node]:
        if not visited[next_node]:
            count += dfs(next_node)
    return count
    

n = int(input())
c = int(input())
graph = [[] for _ in range(n+1)]
visited = [False] * (n + 1)

for _ in range(c):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

result = dfs(1) - 1
print(result)