N, X = map(int, input().split())
A = []
B = []
for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
dp = [[False] * (X + 1) for i in range(N + 1)]
dp[0][0] = True
for i in range(N):
    for j in range(X + 1):
        if dp[i][j]:
            if j + A[i] <= X:
                dp[i + 1][j + A[i]] = True
            if j + B[i] <= X:
                dp[i + 1][j + B[i]] = True
if dp[N][X]:
    print(('Yes'))
else:
    print('No')