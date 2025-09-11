import sys
input = sys.stdin.readline

n, k = map(int, input().split())
num = list(input())

stack = []
cnt = k

for i in range(n):
    while(cnt > 0 and stack and stack[-1] < num[i]):
        stack.pop()
        cnt-=1
    stack.append(num[i])
    
print(''.join(stack[:n-k]))