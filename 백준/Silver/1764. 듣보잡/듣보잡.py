import sys
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    name_set = set()
    result = []

    for _ in range(n):
        name_set.add(input().strip())

    for _ in range(m):
        name = input().strip()
        if name in name_set:
            result.append(name)

    print(len(result))
    for name in sorted(result):
        print(name)

solve()