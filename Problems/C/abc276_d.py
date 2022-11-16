N = int(input())
A = list(map(int, input().split()))
if all(val == A[0] for val in A):
    print(0)
    exit()


def GCD(a, b):
    while a >= 1 and b >= 1:
        if b > a:
            b = b % a
        else:
            a = a % b
    if a >= 1:
        return a
    else:
        return b


point = GCD(A[0], A[1])
for i in A[2:]:
    point = GCD(point, i)
if point == 1:
    for i in A:
        if i % 2 != 0 and i % 3 != 0 and i != 1:
            print(-1)
            exit()
cnt = 0
for i in A:
    if i == point:
        continue
    else:
        if i % 6 == 0:
            n = i
            while point < n:
                n = n // 6
                cnt += 2
        elif i % 3 == 0:
            n = i
            while point < n:
                n = n // 3
                cnt += 1
        elif i % 2 == 0:
            n = i
            while point < n:
                n = n // 2
                cnt += 1
print(cnt)