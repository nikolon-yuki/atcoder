H, W = map(int, input().split())
X = [input() for i in range(H)]
ans = [0] * W
for i in range(W):
    for j in range(H):
        if X[j][i] == "#":
            ans[i] += 1
print(*ans)