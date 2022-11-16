N, K, X = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
ans = sum(A)
chk = [0] * N
mod = [0] * N
for i in range(N):
    chk[i] = A[i] // X
    mod[i] = A[i] % X
ind = 0
for i in range(N):
    if chk[i] != 0:
        ind = i
        break
for i in range(ind, N):
    if K == 0:
        break
    if K - chk[i] >= 0:
        ans -= chk[i] * X
        K -= chk[i]
    else:
        ans -= K * X
        K = 0
        break
if K != 0:
    mod.sort(reverse=True)
    for i in mod:
        if K == 0:
            break
        else:
            ans -= i
            K -= 1
if ans <= 0:
    print(0)
else:
    print(ans)