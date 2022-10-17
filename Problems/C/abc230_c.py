N, A, B = map(int, input().split())
P, Q, R, S = map(int, input().split())
mak1 = max(1 - A, 1 - B)
mik1 = min(N - A, N - B)
mak2 = max(1 - A, B - N)
mik2 = max(N - A, B - 1)
height = Q - P
wide = S - R
ans = [[False] * (wide + 1) for i in range(height + 1)]
for i in range(P, Q + 1):
    k = i - A
    if mak1 <= k <= mik1:
        for j in range(R, S + 1):
            l = j - B
            if l == k:
                ans[i - P][j - R] = True
    if mak2 <= k <= mik2:
        for j in range(R, S + 1):
            l1 = B - j
            if l1 == k:
                ans[i - P][j - R] = True
for i in ans:
    a = ""
    for j in i:
        if j:
            a += '#'
        else:
            a += '.'
    print(a)
