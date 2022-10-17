import bisect

N, Q = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
for i in range(Q):
    a = int(input())
    ind = bisect.bisect_left(A, a)
    print(N - ind)
