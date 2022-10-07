H, W, N = map(int, input().split())
A = []
B = []
for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

adict = {a: i + 1 for i, a in enumerate(sorted(list(set(A))))}
bdict = {b: i + 1 for i, b in enumerate(sorted(list(set(B))))}

for i in range(N):
    print(adict[A[i]], bdict[B[i]])
