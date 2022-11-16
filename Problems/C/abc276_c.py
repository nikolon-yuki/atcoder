N = int(input())
P = list(map(int, input().split()))
for i in range(N - 1, -1, -1):
    if P[i] < P[i - 1]:
        st = P[i - 1]
        inds = 0
        che = P[i:]
        che.sort(reverse=True)
        for j in che:
            if st > j:
                inds = j
                break
        ind = P.index(inds)
        P[i - 1], P[ind] = P[ind], P[i - 1]
        newp = P[i:]
        newp.sort(reverse=True)
        ans = P[:i] + newp
        print(*ans)
        break
