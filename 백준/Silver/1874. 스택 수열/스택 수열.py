import sys
from collections import deque
input = sys.stdin.readline

def run(num_list):
    PUSH, POP = '+', '-' 
    
    result = []
    stack = deque()

    cur_index = 0
    for i in range(1, len(num_list)+1):
        stack.append(i)
        result.append(PUSH)

        while stack and stack[-1] == num_list[cur_index]:
            stack.pop()
            result.append(POP)
            cur_index += 1
        
        if stack and stack[-1] > num_list[cur_index]:
            return "NO"
    
    if cur_index < len(num_list):
        return "NO"
    
    return result

def solve():
    n = int(input())
    num_list = [int(input()) for _ in range(n)]

    result = run(num_list)
    
    if result == "NO":
        print(result)
    else:
        print("\n".join(result))

solve()

