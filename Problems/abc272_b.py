N, M = map(int, input().split())
cnt = [[] for i in range(N)]
for i in range(M):
    m = list(map(int, input().split()))
    for a in m[1:]:
        a -= 1
        for b in m[1:]:
            b -= 1
            if a != b and b not in cnt[a]:
                cnt[a].append(b)
ans = True
for i in cnt:
    if len(i) < N - 1:
        ans = False
if ans:
    print("Yes")
else:
    print("No")
