N = int(input())
S = [input() for i in range(N)]
T = [input() for i in range(N)]
f = False
check = -1
s = []
t1, t2, t3, t4 = [], [], [], []
check1, check2, check3, check4 = -1, -1, -1, -1
f1, f2, f3, f4 = False, False, False, False
lis = [t1, t2, t3, t4]
for i in range(N):
    for j in range(N):
        if check >= 0:
            check += 1
        if not f and S[i][j] == "#":
            f = True
            check = 0
        elif S[i][j] == "#":
            s.append(check)
            check = 0
for i in range(N):
    for j in range(N):
        if check1 >= 0:
            check1 += 1
        if not f1 and T[i][j] == "#":
            f1 = True
            check1 = 0
        elif T[i][j] == "#":
            t1.append(check1)
            check1 = 0
for i in range(N - 1, -1, -1):
    for j in range(N):
        if check2 >= 0:
            check2 += 1
        if not f2 and T[j][i] == "#":
            f2 = True
            check2 = 0
        elif T[j][i] == "#":
            t2.append(check2)
            check2 = 0
for i in range(N - 1, -1, -1):
    for j in range(N - 1, -1, -1):
        if check3 >= 0:
            check3 += 1
        if not f3 and T[i][j] == "#":
            f3 = True
            check3 = 0
        elif T[i][j] == "#":
            t3.append(check3)
            check3 = 0
for i in range(N):
    for j in range(N):
        if check4 >= 0:
            check4 += 1
        if not f4 and T[j][i] == "#":
            f4 = True
            check4 = 0
        elif T[j][i] == "#":
            t4.append(check4)
            check4 = 0

ans = False
for i in lis:
    if s == i:
        ans = True
if ans:
    print("Yes")
else:
    print("No")
