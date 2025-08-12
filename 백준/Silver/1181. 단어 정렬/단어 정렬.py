import sys
input = sys.stdin.readline

n = int(input())
list = [set() for _ in range(51)]

for _ in range(n):
    word = input().rstrip()
    length = len(word)

    list[length].add(word)

for i in range(1, 51):
    sorted_set = sorted(list[i])
    if sorted_set:
        print('\n'.join(sorted_set))
