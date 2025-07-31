import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
max_heap = []
min_heap = []
solved = defaultdict(bool)
for _ in range(n):
    p, l = map(int, input().split())
    heapq.heappush(max_heap, (-l, -p))
    heapq.heappush(min_heap, (l, p))

m = int(input())
for _ in range(m):
    command = input().split()
    if command[0] == "add":
        l = int(command[2])
        p = int(command[1])
        heapq.heappush(max_heap, (-l, -p))
        heapq.heappush(min_heap,  (l, p))
    elif command[0] == "recommend":
        if command[1] == '1':
            while solved[-max_heap[0][1]]:
                solved[-max_heap[0][1]] = False
                heapq.heappop(max_heap)
            print(-max_heap[0][1])
        else:
            while solved[min_heap[0][1]]:
                solved[min_heap[0][1]] = False
                heapq.heappop(min_heap)
            print(min_heap[0][1])
    elif command[0] == "solved":
        solved[int(command[1])] = True
    

