import math
N, M = map(int, input().split())
B = [list(map(int, input().split())) for i in range(N)]
j = B[0][0] % 7
if j == 0:
    j = 7
i = math.ceil((B[0][0] - j) / 7)
ans = True
for a in range(N):
    for b in range(M):
        s = (i + a) * 7 + (j + b)
        if B[a][b] != s:
            ans = False
        if j + b > 7:
            ans = False
if ans:
    print('Yes')
else:
    print('No')