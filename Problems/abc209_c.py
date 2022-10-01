N = int(input())
C = list(map(int, input().split()))
C.sort()
ans = 1
for i in range(N):
    if (C[i] - i) > 0:
        ans = ans * (C[i] - i) % (10 ** 9 + 7)
    else:
        ans = 0
print(ans)