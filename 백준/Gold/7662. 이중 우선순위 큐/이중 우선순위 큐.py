import heapq
import sys
input = sys.stdin.readline

def solve():
    t = int(input())
    for _ in range(t):
        max_heap = []
        min_heap = []
        k = int(input())
        valid = [False] * k
        for i in range(k):
            operation, n = input().split()
            if operation == 'I':
                heapq.heappush(max_heap, (-int(n), i))
                heapq.heappush(min_heap, (int(n), i))
                valid[i] = True
            else:
                if n == "1":
                    if max_heap:
                        valid[heapq.heappop(max_heap)[1]] = False
                else:
                    if min_heap:
                        valid[heapq.heappop(min_heap)[1]] = False
            
            #가장 앞에 있는 값이 유효한 상태인지 확인 -> 유효한 상태의 값이 나올때까지 반복 제거
            while min_heap and valid[min_heap[0][1]] == False:
                heapq.heappop(min_heap)
            while max_heap and valid[max_heap[0][1]] == False:
                heapq.heappop(max_heap)

        if min_heap and max_heap:
            print(-max_heap[0][0], min_heap[0][0])
        else:
            print("EMPTY")


solve()