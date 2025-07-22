import sys
from  collections import deque
input = sys.stdin.readline

n = int(input())
q = deque(enumerate(map(int, input().split())))
result = []

while q:
    index, value = q.popleft()
    result.append(index+1)

    if value > 0:
        q.rotate(-(value-1))
    else:
        q.rotate(-value)

print(' '.join(map(str, result)))