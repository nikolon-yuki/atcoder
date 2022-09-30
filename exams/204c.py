N, M = 3, 3
inp = [[1, 2], [2, 3], [3, 2]]
G = [[] for i in range(N)]
for i, j in inp:
    i -= 1
    j -= 1
    G[i].append(j)
anss = 0


def root(x, dn, ans):
    global anss
    anss += 1
    dn[x] = True
    for i in G[x]:
        if not dn[i]:
            root(i, dn, ans)
    return ans


for i in range(N):
    d = [False] * N
    root(i, d, anss)
print(anss)
