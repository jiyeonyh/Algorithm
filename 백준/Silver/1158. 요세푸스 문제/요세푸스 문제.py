from collections import deque
import sys
input = sys.stdin.readline

def remove(q, k):
    q.rotate(-(k-1))
    return q.popleft()

def solve():
    n, k = map(int, input().split())
    q = deque([i for i in range(1, n+1)])
    
    result = []
    while q:
        result.append(remove(q, k))
    
    print("<" + ", ".join(map(str, result)) + ">")


solve()