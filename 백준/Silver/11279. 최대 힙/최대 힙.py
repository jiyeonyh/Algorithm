import heapq
import sys
input = sys.stdin.readline

def heap_push(max_heap, x):
    heapq.heappush(max_heap, -x)

def heap_pop(max_heap, x):
    if x == 0:
        if len(max_heap) == 0:
            return 0
        else:
            return -heapq.heappop(max_heap)

def solve():
    n = int(input())
    max_heap = []

    for _ in range(n):
        x = int(input())
        if x == 0:
            print(heap_pop(max_heap, x))
        else:
            heap_push(max_heap, x)
        
solve()