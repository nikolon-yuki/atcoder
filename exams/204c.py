N, M = 3, 3
inp = [[1, 2], [2, 3], [3, 2]]
G = [[] for i in range(N)]
for i, j in inp:
    i -= 1
    j -= 1
    G[i].append(j)
s = 0


def root(x):
    dn[x] = True
    for i in G[x]:
        if not dn[i]:
            root(i)


for i in range(N):
    dn = [False] * N
    root(i)
    s += sum(dn)
print(s)
