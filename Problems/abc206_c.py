from collections import Counter

N = int(input())
A = list(map(int, input().split()))
s = 0
for i in range(N - 1):
    s += i + 1
newA = Counter(A)
s2 = 0
for i, j in newA.items():
    if j != 1:
        for x in range(j - 1):
            s2 += x + 1
print(s - s2)

# 以下のようにも計算できる
# s = N*(N-1)//2
# s2 = for i, j in newA.items():
#     j*(j-1)//2
# ans = s-s2
