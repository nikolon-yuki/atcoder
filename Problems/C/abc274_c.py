N = int(input())
A = list(map(int, input().split()))
ans = [10**6] * (10**7)
check = [False] * (10**7)
for i in range(N):
    ans[A[i]] = i

for i in range(N):
    n = 2 * (i + 1)
    if i == 0:
        print(0)
    if not check[n]:
        ans[n] = min(ans[n] + 1, ans[A[i]] + 1)
        check[n] = True
        print(ans[n])
    if not check[n + 1]:
        ans[n + 1] = min(ans[n] + 1, ans[A[i]] + 1)
        check[n + 1] = True
        print(ans[n + 1])
    else:
        print(ans[A[i]] + 1)
        print(ans[A[i]] + 1)
    