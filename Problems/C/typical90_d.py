H, W = map(int, input().split())
A = []
height = [0] * W
wide = [0] * H
for i in range(H):
    a = list(map(int, input().split()))
    wide[i] = sum(a)
    A.append(a)
for i in range(W):
    cnt = 0
    for j in range(H):
        cnt += A[j][i]
    height[i] = cnt
ans = [[0] * W for i in range(H)]
for i in range(H):
    for j in range(W):
        ans[i][j] = height[j] + wide[i] - A[i][j]
for i in ans:
    print(*i)
