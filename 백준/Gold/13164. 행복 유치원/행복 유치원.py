import sys
input = sys.stdin.readline

n, k = map(int,input().split())
data = list(map(int,input().split()))
dif = [0] * (n - 1)

for i in range(len(data)-1):
    dif[i] = data[i+1] - data[i]

dif.sort()
print(sum(dif[:n-k]))