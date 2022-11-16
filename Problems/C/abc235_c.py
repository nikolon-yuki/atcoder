N, Q = map(int, input().split())
A = list(map(int, input().split()))
ans = []
S = {}
for i in range(N):
    if A[i] not in S:
        S[A[i]] = len(ans)
        ans.append([i + 1])
    else:
        ans[S[A[i]]].append(i + 1)
for i in range(Q):
    x, k = map(int, input().split())
    if x not in S:
        print(-1)
    elif len(ans[S[x]]) < k:
        print(-1)
    else:
        a = ans[S[x]][k - 1]
        print(a)
