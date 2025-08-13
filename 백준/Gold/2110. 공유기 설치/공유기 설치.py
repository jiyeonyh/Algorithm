import sys
input = sys.stdin.readline

n, c = map(int, input().split())
houses = [int(input()) for _ in range(n)]
houses.sort()

start = 1
end = houses[-1] - houses[0]
result = 0

while start <= end:
    mid = (start + end) // 2
    cnt = 1
    val = houses[0]
    for i in range(1, n):
        if houses[i] >= val + mid:
            val = houses[i]
            cnt += 1
    if cnt >= c:
        start = mid + 1
        result = mid
    else:
        end = mid - 1
print(result)