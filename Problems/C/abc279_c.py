H, W = map(int, input().split())
S = [input() for i in range(H)]
X = [input() for i in range(H)]
s = {}
x = {}
for i in range(W):
    t = []
    for j in range(H):
        if S[j][i] == "#":
            t.append(j)
    t = tuple(t)
    if t not in s:
        s[t] = 1
    else:
        s[t] += 1

for i in range(W):
    t = []
    for j in range(H):
        if X[j][i] == "#":
            t.append(j)
    t = tuple(t)
    if t not in x:
        x[t] = 1
    else:
        x[t] += 1

for a, b in x.items():
    if a not in s:
        print("No")
        exit()
    if s[a] != b:
        print("No")
        exit()
print('Yes')
