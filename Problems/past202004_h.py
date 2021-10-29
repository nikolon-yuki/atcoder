N, M = map(int, input().split())
A = [list(input()) for i in range(N)]
group = []
for i in range(11):
    group.append([])
for i in range(N):
    for j in range(M):
        if A[i][j] == "S":
            n = 0
        elif A[i][j] == "G":
            n = 10
        else:
            n = int(A[i][j])
        group[n].append([i, j])

cost = [[10 ** 100] * M for i in range(N)]

si, sj = group[0][0]
cost[si][sj] = 0

for n in range(1, 11):
    for i, j in group[n]:
        for i2, j2 in group[n - 1]:
            cost[i][j] = min(cost[i][j], cost[i2][j2] + abs(i - i2) + abs(j - j2))

gi, gj = group[10][0]
ans = cost[gi][gj]
if ans == 10 ** 100:
    ans = -1
print(ans)


# 座標の値と座標を保存し、値をループさせ、１つ下の値とのマンハッタン距離（2点間の距離）を蓄積していき、Gの座標がans。
