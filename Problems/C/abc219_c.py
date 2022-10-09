X = input()
N = int(input())
s = [[] for i in range(N)]
for i in range(N):
    n = input()
    for j in n:
        s[i].append(X.index(j))
ans = []
s.sort()
for i in s:
    A = ''
    for j in i:
        A += X[j]
    ans.append(A)
for i in ans:
    print(i)
