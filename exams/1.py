N, S = 2, 40
L = [[3, [1, 8, 4]], [2, [10, 5]]]
ans = 0
X = 1
index = N - 1


def recursion(lis, n, ind):
    global ans
    for i in range(lis[0]):
        seki = lis[1][i]
        print(i)
        if not ind:
            if n * seki == S:
                ans += 1
        else:
            recursion(L[ind - 1], n * seki, ind - 1)


recursion(L[index], X, index)
