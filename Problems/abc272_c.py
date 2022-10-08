N = int(input())
A = list(map(int, input().split()))
k = []
g = []
ans = -1
for i in A:
    if i % 2 != 0:
        k.append(i)
    else:
        g.append(i)
k.sort()
g.sort()
if len(k) > 1:
    ans = max(ans, k[-1] + k[-2])
if len(g) > 1:
    ans = max(ans, g[-1] + g[-2])
print(ans)