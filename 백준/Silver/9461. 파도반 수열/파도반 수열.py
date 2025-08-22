import sys
input = sys.stdin.readline

def padovan(max_n):
    P = [0] * (max_n + 1)
    P[1]=P[2]=P[3]= 1
    for i in range(4, max_n + 1):
        P[i] = P[i - 2] + P[i - 3]
    return P

def solve():
    n = int(input())
    test_case = [int(input()) for _ in range(n)]
    max_val = max(test_case)

    P = padovan(max_val)

    print("\n".join(str(P[t]) for t in test_case))

solve()