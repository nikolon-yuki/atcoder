N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ans = True
a = [False] * N
b = [False] * N
a[0] = True
b[0] = True


def check(s, x):
    if abs(s - x) <= K:
        return True
    else:
        return False


for i in range(N - 1):
    if not a[i] and not b[i]:
        ans = False
        break
    if a[i]:
        if check(A[i], A[i + 1]):
            a[i + 1] = True
        if check(A[i], B[i + 1]):
            b[i + 1] = True
    if b[i]:
        if check(B[i], A[i + 1]):
            a[i + 1] = True
        if check(B[i], B[i + 1]):
            b[i + 1] = True
            
if not a[N - 1] and not b[N - 1]:
    ans = False
if ans:
    print("Yes")
else:
    print("No")
