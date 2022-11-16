N, K = map(int, input().split())
S = [input() for i in range(N)]
ans = 0
for i in range(1 << N):
    s = {}
    cnt = 0
    for j in range(N):
        if (i & (1 << j)) != 0:
            for x in S[j]:
                if x not in s:
                    s[x] = 1
                else:
                    s[x] += 1
    for a, b in s.items():
        if b == K:
            cnt += 1
    ans = max(ans, cnt)
print(ans)
