N, x, y = map(int, input().split())
A = list(map(int, input().split()))
p1x, p1y = 0, 0
p2x, p2y = A[0], 0
height = True
X, Y = abs(p2x - x), abs(p2y - y)
for i in range(1, N):
    if height:
        if Y == 0:
            break
        Y -= abs(A[i])
        height = False
    else:
        if X == 0:
            break
        X -= abs(A[i])
        height = True
if X == 0 and Y == 0:
    print('Yes')
else:
    print('No')
