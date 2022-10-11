N, M = map(int, input().split())
X = [input() for i in range(2 * N)]
rank = [[0, i] for i in range(2 * N)]


def judge(a, b):
    if a == b:
        return -1
    if a == "G" and b == "P":
        return 1
    if a == "C" and b == "G":
        return 1
    if a == "P" and b == "C":
        return 1
    return 0


for i in range(M):
    for j in range(N):
        p1 = rank[2 * j][1]
        p2 = rank[2 * j + 1][1]
        res = judge(X[p1][i], X[p2][i])
        if res != -1:
            rank[2 * j + res][0] -= 1
    rank.sort()
for j ,i in rank:
    print(i+1)


# def sor(S):
#     dic = sorted(S.items(), key=lambda x: x[1])
#     res = []
#     for i, j in dic:
#         res.append(X[i])
#     for i in range(len(res)):
#         for j in range(i, len(res)):
#             if s[X.index(res[i])] == s[X.index(res[j])] and X.index(res[i]) > X.index(res[j]):
#                 res[i], res[j] = res[j], res[i]
#     return res


# for i in range(M):
#     for j in range(N):
#         n = 2 * j
#         if A[n][i] == A[n + 1][i]:
#             continue
#         elif A[n][i] == "P" and A[n + 1][i] == "G":
#             s[X.index(A[n])] += 1
#             s[X.index(A[n + 1])] -= 1
#         elif A[n][i] == "G" and A[n + 1][i] == "P":
#             s[X.index(A[n + 1])] += 1
#             s[X.index(A[n])] -= 1
#         elif A[n][i] == "G" and A[n + 1][i] == "C":
#             s[X.index(A[n])] += 1
#             s[X.index(A[n + 1])] -= 1
#         elif A[n][i] == "C" and A[n + 1][i] == "G":
#             s[X.index(A[n + 1])] += 1
#             s[X.index(A[n])] -= 1
#         elif A[n][i] == "C" and A[n + 1][i] == "P":
#             s[X.index(A[n])] += 1
#             s[X.index(A[n + 1])] -= 1
#         elif A[n][i] == "P" and A[n + 1][i] == "C":
#             s[X.index(A[n + 1])] += 1
#             s[X.index(A[n])] -= 1
#     A = sor(s)
# print(A)
