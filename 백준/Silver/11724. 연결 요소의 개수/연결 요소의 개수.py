import sys
from collections import deque
input = sys.stdin.readline

def bfs(graph):
    visited = [False] * len(graph)
    q = deque()
    cnt = 0
    for i in range(1, len(graph)):
        if visited[i]:
            continue 
        q.append(i)
        visited[i] = True
        while q:
            cur = q.popleft()
            for node in graph[cur]:
                if not visited[node]:
                    q.append(node)
                    visited[node] = True
        cnt += 1
    return cnt

def solve():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]

    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    cnt = bfs(graph)
    print(cnt)

solve()