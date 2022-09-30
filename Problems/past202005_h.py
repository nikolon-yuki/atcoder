N, L = map(int, input().split())
X = list(map(int, input().split()))
T = list(map(int, input().split()))
H = [False] * (L + 1)
for i in X:
    H[i] = True
dp = [10 ** 100] * (L + 1)
dp[0] = 0
for i in range(1, L + 1):
    dp[i] = min(dp[i], dp[i - 1] + T[0])
    if i >= 2:
        dp[i] = min(dp[i], dp[i - 2] + T[0] + T[1])
    if i >= 4:
        dp[i] = min(dp[i], dp[i - 4] + T[0] + 3 * T[1])

    if H[i]:
        dp[i] += T[2]
ans = dp[L]
for i in [L - 3, L - 2, L - 1]:
    if i >= 0:
        ans = min(ans, dp[i] + T[0] // 2 + T[1] * (2 * (L - i) - 1) // 2)
print(ans)
