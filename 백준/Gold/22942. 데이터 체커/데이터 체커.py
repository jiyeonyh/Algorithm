import sys
input = sys.stdin.readline

n = int(input())
circles = []

for i in range(n):
    x, r = map(int, input().split())
    circles.append((x-r, i))
    circles.append((x+r, i))
circles.sort()

stack = []
for i in range(len(circles)):
    if stack:
        if stack[-1][1] == circles[i][1]:
            stack.pop()
        else:
            stack.append(circles[i])
    else:
        stack.append(circles[i])
    
if len(stack) == 0:
    print("YES")
else:
    print("NO")