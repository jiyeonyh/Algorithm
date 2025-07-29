import sys
input = sys.stdin.readline

line = input().strip()
stack = []
result = 0
before_c = '('

for c in line:
    if c == '(':
        stack.append(c)
    else:
        if before_c == '(':
            stack.pop()
            result += len(stack)
        else:
            stack.pop()
            result += 1
    before_c = c
print(result)
