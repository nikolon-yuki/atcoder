from collections import deque
import sys

sys.setrecursionlimit(10 ** 7)

N, X, Y = map(int, input().split())
G = [[] for i in range(N + 1)]
for i in range(N - 1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)
s = set()
d = deque()
d.append(X)
a = [X]


def graph(i, ans):
    s.add(i)
    if i == Y:
        print(ans)
        return ans
    if d:
        v = d.popleft()
        for j in G[v]:
            if j not in s:
                d.append(j)
                ans.append(j)
                graph(j, ans)
                ans.pop()



h = graph(X, a)
print(h)