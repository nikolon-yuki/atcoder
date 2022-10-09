N = int(input())
A = list(map(int, input().split()))
vol = [False] * (N + 2)
sold = 0
for i in range(N):
    if A[i] >= len(vol):
        sold += 1
    elif vol[A[i]]:
        sold += 1
    else:
        vol[A[i]] = True
L = 1
R = N + 1
while True:
    while vol[L]:
        L += 1
    while (R != 0) and (not vol[R]):
        R -= 1
    if sold >= 2:
        sold -= 2
        vol[L] = True
    else:
        if L >= R:
            break
        vol[R] = False
        sold += 1
print(L-1)