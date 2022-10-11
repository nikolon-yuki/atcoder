N = int(input())
A = list(map(int, input().split()))
X = int(input())
a = sum(A)
ans = (X // a) * N
m = X % a
for i in A:
    if m < 0:
        break
    ans += 1
    m -= i
print(ans)
