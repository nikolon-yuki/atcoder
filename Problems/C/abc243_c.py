N = int(input())
s = {}
for i in range(N):
    x, y = map(int, input().split())
    if y not in s:
        s[y] = [(i, x)]
    else:
        s[y].append((i, x))
S = input()
ans = False
for i in s.values():
    r = []
    l = []
    if len(i) > 1:
        for x in i:
            if S[x[0]] == 'R':
                r.append(x[1])
            else:
                l.append(x[1])
    r.sort()
    l.sort()
    if r and l and min(r) <= max(l):
        ans = True
        break
if ans:
    print('Yes')
else:
    print('No')