
def solve():
    n, m = map(int, input().split())
    name_set = set()
    result = []

    for _ in range(n):
        name = input()
        name_set.add(name)

    for _ in range(m):
        name = input()
        if name in name_set:
            result.append(name)

    print(len(result))
    result.sort()
    for item in result:
        print(item)

solve()