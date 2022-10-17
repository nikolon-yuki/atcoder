import itertools

N, M = map(int, input().split())
T = [[] for i in range(N)]
A = [[] for i in range(N)]
l = [i for i in range(N)]
new_a = itertools.permutations(l)
for i in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    T[a].append(b)
    T[b].append(a)
for i in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    A[a].append(b)
    A[b].append(a)
ans = False
for p in new_a:
    a = True
    for j in range(N):
        t = T[j]
        for x in t:
            if p[x] not in A[p[j]] and t:
                a = False
    if a:
        ans = True
if M == 0:
    print('Yes')
elif ans:
    print('Yes')
else:
    print(('No'))