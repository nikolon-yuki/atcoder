N, M = map(int, input().split())
G = [[] for i in range(N + 1)]
for i in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)
for i in G[1:]:
    if not i:
        print(0)
    else:
        ind = len(i)
        i.sort()
        i = [ind] + i
        print(*i)
