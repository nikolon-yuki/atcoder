N, K = map(int, input().split())
K -= 1
P = []
lis = []
ans = [False] * N
for i in range(N):
    a, b, c = map(int, input().split())
    P.append((a + b + c))
    lis.append((a + b + c))
lis.sort(reverse=True)
for i in range(N):
    if P[i] + 300 >= lis[K]:
        ans[i] = True
for i in ans:
    if i:
        print('Yes')
    else:
        print('No')
