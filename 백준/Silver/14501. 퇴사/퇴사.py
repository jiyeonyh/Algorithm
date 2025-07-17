import sys
input = sys.stdin.readline

def dfs(graph, v, n, total):
    finish_day = v + graph[v][0]

    if finish_day == n+1:
        return total + graph[v][1]
    elif finish_day > n+1:
        return total
    
    total += graph[v][1]

    max_total = total
    for i in range(finish_day, n+1):
        if i in graph:
            result = dfs(graph, i, n, total)
            max_total = max(max_total, result)

    return max_total



def solve():
    n = int(input())
    schedules = {}
    
    for i in range(n):
        t, p = map(int, input().split())
        
        if i+t <= n:
            schedules[i+1] = (t, p)

    max_result = 0
    for start_day in schedules:
        result = dfs(schedules, start_day, n, 0)
        max_result = max(max_result, result)

    print(max_result)

solve()