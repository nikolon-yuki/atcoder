N, Q = map(int, input().split())
L = [list(map(int, input().split())) for i in range(N)]
for i in range(Q):
    s, t = map(int, input().split())
    s -= 1
    print(L[s][t])
