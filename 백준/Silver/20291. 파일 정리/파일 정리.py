from collections import defaultdict
import sys
input = sys.stdin.readline

n = int(input())
ext_count = defaultdict(lambda: 0)

for _ in range(n):
    extension = input().strip().split('.')[1]
    ext_count[extension] += 1

for key in sorted(ext_count.keys()):
    print(f"{key} {ext_count[key]}")