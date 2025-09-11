import sys
input = sys.stdin.readline

mk_num = input().strip()
min_num, max_num = "", ""
cnt = 0

for n in mk_num:
    if n == "M":
        cnt += 1
    else:
        if cnt > 0:
            min_num += str((10 ** cnt) + 5)
            max_num += str(5 * (10 ** cnt))
        else:
            min_num += "5"
            max_num += "5"
        cnt = 0

if cnt > 0:
    min_num += str(10 ** (cnt-1))
    max_num += "1" * cnt

print(max_num)
print(min_num)