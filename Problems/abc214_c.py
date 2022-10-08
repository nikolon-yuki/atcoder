N = int(input())
S = list(map(int, input().split()))
T = list(map(int, input().split()))
ans = [0] * N
minit = T.index(min(T))
ans[minit] = T[minit]
n = minit
while n < N + minit:
    i = (n + 1) % N
    ans[i] = min(T[i], ans[i - 1] + S[i - 1])
    n += 1
for i in ans:
    print(i)
    
# for x in range(2):
#     n = 0
#     while n < N:
#         i = (n + 1) % N
#         ans[i] = min(T[i], ans[i - 1] + S[i - 1])
#         n += 1
