N, Q = map(int, input().split())
ans = [["N"] * N for i in range(N)]

for i in range(Q):
    lis = list(map(int, input().split()))

    if lis[0] == 1:
        ans[lis[1] - 1][lis[2] - 1] = "Y"

    if lis[0] == 2:
        for j, i in enumerate(ans):
            if i[lis[1] - 1] == "Y":
                ans[lis[1] - 1][j] = "Y"

    if lis[0] == 3:
        to_follow = []
        for x, y in enumerate(ans[lis[1] - 1]):
            if y == "Y":
                for a, b in enumerate(ans[x]):
                    if b == "Y":
                        to_follow.append(a)

        for i in to_follow:
            ans[lis[1] - 1][i] = "Y"


for i in ans:
    print(''.join(i))
