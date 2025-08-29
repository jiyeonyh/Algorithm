import sys
input = sys.stdin.readline

n = int(input())
x_list = list(map(int, input().split()))
s = [0] * n 

for i in range(1, n):
    s[i] = s[i-1] + x_list[i]

result = 0
for i in range(n):
    result += x_list[i] * (s[n-1]- s[i])

print(result) 