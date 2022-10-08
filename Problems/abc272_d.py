import math

N, M = map(int, input().split())
lis = [[100] * N for i in range(N)]
lis[0][0] = 0
a = [0]
b = [0]
for _ in range(N*400):
    for i in range(a[0],N + a[0]):
        for j in range(b[0],N + b[0]):
            x = ((a[0] + 1) - (i % N + 1)) ** 2 + ((b[0] + 1) - (j % N + 1)) ** 2
            h = math.sqrt(x)
            if h == math.sqrt(M):
                lis[i % N][j % N] = min(lis[i % N][j % N], lis[a[0]][b[0]] + 1)
                a.append(i % N)
                b.append(j % N)
    a = a[1:]
    b = b[1:]
for i in lis:
    print(*i)
