N, M, K = map(int, input().split())
dp = [[0] * (K + 1) for i in range(N + 1)]
mod = 998244353
for i in range(1, M + 1):
    dp[1][i] = 1
for i in range(2, N + 1):
    for j in range(1, K + 1):
        for x in range(j - M, j):
            if x < 1:
                continue
            dp[i][j] += dp[i - 1][x]
            dp[i][j] %= mod
ans = 0
for i in range(1, K + 1):
    ans += dp[N][i]
    ans %= mod
print(ans)
