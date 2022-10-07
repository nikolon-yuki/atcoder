S = input()
N = len(S)
S = "0" + S
T = "0chokudai"
dp = [[0] * 9 for i in range(N + 1)]
for i in range(N + 1):
    for j in range(9):
        if j == 0:
            dp[i][j] = 1
        elif S[i] != T[j]:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]
        dp[i][j] %= 10 ** 9 + 7
print(dp[N][8])
