n = int(input())
lis = list(map(int, input().split()))
Q = int(input())
sell = 0

z = 0
s = 0

min_s = 10000000000
min_z = 10000000000

for i in range(n):
    if i % 2 == 0:
        min_s = min(lis[i], min_s)
    else:
        min_z = min(lis[i], min_z)

for _ in range(Q):
    query = list(map(int, input().split()))

    if query[0] == 1:
        x = query[1] - 1
        a = query[2]

        if x % 2 == 0:
            card_x = lis[x] - z - s
        else:
            card_x = lis[x] - z

        if card_x >= a:
            lis[x] -= a
            sell += a

            if x % 2 == 0:
                min_s = min(lis[x], min_s)
            else:
                min_z = min(lis[x], min_z)

    elif query[0] == 2:
        a = query[1]
        if min_s - s - z >= a:
            s += a

    elif query[0] == 3:
        a = query[1]
        if min(min_s - s - z, min_z - z) >= a:
            z += a

for i in range(n):
    if i % 2 == 0:
        sell += s

sell += z * n

print(sell)

# 要点
# 最小値を求めればいいから、for文ではなく、minを更新していくと計算量を探索できる。s,zに足し上げていく。
