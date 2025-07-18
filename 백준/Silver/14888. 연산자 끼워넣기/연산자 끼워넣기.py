import sys
input = sys.stdin.readline

operations = [
    lambda a, b: a + b,                           
    lambda a, b: a - b,                           
    lambda a, b: a * b,                           
    lambda a, b: int(a / b) if a * b >= 0 else -(-a // b)
]

min_result, max_result = 1_000_000_000, -1_000_000_000

def dfs(depth, result, op_counts, numbers):
    global min_result, max_result

    if depth == len(numbers) - 1:
        min_result = min(min_result, result)
        max_result = max(max_result, result)
        return

    for i in range(4):
        if op_counts[i] > 0:
            op_counts[i] -= 1
            dfs(depth+1, operations[i](result, numbers[depth+1]), op_counts, numbers)
            op_counts[i] += 1


def solve():
    n = int(input())
    numbers = list(map(int, input().split()))
    op_counts = list(map(int, input().split()))

    dfs(0, numbers[0], op_counts[:], numbers)

    print(max_result)
    print(min_result)
    

solve()