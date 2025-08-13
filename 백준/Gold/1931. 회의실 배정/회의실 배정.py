import sys
input = sys.stdin.readline

n = int(input())
meetings = [tuple(map(int, input().split())) for _ in range(n)]
meetings.sort(key=lambda x: (x[1], x[0]))

end_time = 0
result = 0
for start, end in meetings:
    if start >= end_time:
        end_time = end
        result += 1
print(result)