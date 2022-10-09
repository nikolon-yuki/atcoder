import sys
import bisect

sys.setrecursionlimit(10 ** 7)
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort()
ans = 10 ** 10

for i in range(N):
    x = bisect.bisect_right(B, A[i])
    if x < M:
        ans = min(ans, abs(A[i] - B[x]))
    if 0 <= x - 1:
        ans = min(ans, abs(A[i] - B[x - 1]))
print(ans)


def sp(x, m):
    mid = len(m) // 2
    left = m[:mid]
    right = m[mid:]
    if len(m) <= 2:
        s = 10 ** 10
        for i in m:
            s = min(s, abs(x - i))
        return s
    elif x < m[mid]:
        return sp(x, left)
    else:
        return sp(x, right)
