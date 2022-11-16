N = int(input())
S = []
row = [0] * N
ans = False
for i in range(N):
    cnt = 0
    s = input()
    for j in range(N):
        if s[j] == "#":
            cnt += 1
            row[j] += 1
    if cnt >= 4:
        ans = True
    S.append(s)
for i in row:
    if i >= 4:
        ans = True
w = 0
while w < N:
    cnt = 0
    for i in range(N):
        x, y = i, i + w
        if y == N:
            break
        if S[x][y] == "#":
            cnt += 1
    if cnt >= 4:
        ans = True
        break
    else:
        w += 1
w = 1
while w < N:
    cnt = 0
    for i in range(N):
        x, y = i + w, i
        if x == N:
            break
        if S[x][y] == "#":
            cnt += 1
    if cnt >= 4:
        ans = True
        break
    else:
        w += 1
        
w = N - 1
while 0 <= w:
    cnt = 0
    for i in range(N):
        x, y = i, w - i
        if y == -1:
            break
        if S[x][y] == "#":
            cnt += 1
    if cnt >= 4:
        ans = True
        break
    else:
        w -= 1        

w = N - 2
while 0 <= w:
    cnt = 0
    for i in range(N):
        x, y = i + 1, N - 1 - i
        if x == N - 1:
            break
        if S[x][y] == "#":
            cnt += 1
    if cnt >= 4:
        ans = True
        break
    else:
        w -= 1        
        

if ans:
    print('Yes')
else:
    print('No')