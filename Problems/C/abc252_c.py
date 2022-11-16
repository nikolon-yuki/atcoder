N = int(input())
lis = [[0] * N for i in range(10)]
s = [[0] * 10 for i in range(10)]
for i in range(N):
    q = input()
    for j in range(10):
        ind = int(q[j])
        if s[ind][j] == 0:
            lis[ind][i] = j
        else:
            lis[ind][i] = s[ind][j] * 10 + j
        s[ind][j] += 1
ans = 10**10
for i in lis:
    t = max(i)
    ans = min(ans, t)
print(ans)
