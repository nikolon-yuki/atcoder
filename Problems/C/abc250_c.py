N, Q = map(int, input().split())
s = {}
lis = [i for i in range(N + 1)]
for i in range(1, N + 1):
    s[i] = i
for i in range(Q):
    n = int(input())
    if s[n] + 1 > N:
        ind = s[n]
        s[n], s[lis[(ind - 1)]] = s[lis[(ind - 1)]], ind
        lis[ind], lis[(ind - 1)] = lis[(ind - 1)], lis[ind]
    else:
        ind = s[n]
        s[n], s[lis[ind + 1]] = s[lis[ind + 1]], ind
        lis[ind], lis[ind + 1] = lis[ind + 1], lis[ind]
print(*lis[1:])
