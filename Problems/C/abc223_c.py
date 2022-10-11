N = int(input())
A = []
B = []
t = 0
for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
    t += a/b
t = t/2
ans = 0
for i in range(N):
    if A[i]/B[i] <= t:
        t -= A[i]/B[i]
        ans += A[i]
    else:
        ans += t * B[i]
        break
print(ans)
        
        