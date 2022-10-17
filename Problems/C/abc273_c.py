N = int(input())
A = list(map(int, input().split()))
A.sort()
S = set(A)
h = []
s = {}
for i in range(N):
    if A[i] not in s:
        s[A[i]] = 0
        h.append(A[i])
    else:
        s[A[i]] += 1
ans = [0] * N
for i in range(len(h)):
    ans[i] = s[h[(i + 1) * -1]] + 1
for i in ans:
    print(i)
