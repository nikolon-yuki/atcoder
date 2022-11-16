N = int(input())
dp = [[0] * 10 for i in range(N + 1)]
mod = 998244353
for i in range(1, 10):
    dp[1][i] = 1
for i in range(2, N + 1):
    for j in range(1, 10):
        if j == 1:
            dp[i][j] = dp[i - 1][j] + dp[i - 1][j + 1]
        elif 2 <= j <= 8:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j] + dp[i - 1][j + 1]
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
        dp[i][j] %= mod
ans = sum(dp[N]) % mod
print(ans)
