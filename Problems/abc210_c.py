N, K = map(int, input().split())
lis = list(map(int, input().split()))
s = {}
for i in range(K):
    if lis[i] not in s:
        s[lis[i]] = 1
    else:
        s[lis[i]] += 1
S = 1
F = K
ans = len(s)
while F < N:
    s[lis[S - 1]] -= 1
    if lis[F] not in s:
        s[lis[F]] = 1
    else:
        s[lis[F]] += 1
    if s[lis[S - 1]] == 0:
        s.pop(lis[S - 1])
    ans = max(ans, len(s))
    S += 1
    F += 1
print(ans)
