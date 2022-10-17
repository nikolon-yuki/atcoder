import sys
sys.setrecursionlimit(2000)
N, S = map(int, input().split())
L = []
for i in range(N):
    l = list(map(int, input().split()))
    L.append([l[0], l[1:]])
ans = 0
X = 1
index = 0


def recursion(lis, n, ind):
    global ans
    for i in range(lis[0]):
        seki = lis[1][i]
        if ind == N - 1:
            if n * seki == S:
                ans += 1
        else:
            recursion(L[ind + 1], n * seki, ind + 1)


recursion(L[index], X, index)
print(ans)
