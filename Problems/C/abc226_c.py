import sys

sys.setrecursionlimit(10 ** 7)
N = int(input())
T = []
K = []
A = []
for i in range(N):
    lis = list(map(int, input().split()))
    T.append(lis[0])
    K.append(lis[1])
    A.append(lis[2:])
point = [[] for i in range(N)]
check = [0] * N
ans = 0


def gl(n, s):
    for i in s:
        i -= 1
        point[n].append(i)
    for i in point[n]:
        if K[i] == 0:
            if check[i] == 0:
                check[i] = T[i]
        else:
            if check[i] == 0:
                check[i] = T[i]
                gl(i, A[i])


gl(N - 1, A[N - 1])
check[N - 1] = T[N - 1]
print(sum(check))
