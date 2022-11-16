s = [[] for i in range(9)]
lis = []
for i in range(9):
    n = input()
    for j in range(9):
        if n[j] == "#":
            s[i].append(j)
    lis.append(n)
ans = 0


def ch(i, j):
    global ans
    for x in range(i, 9):
        for y in range(9):
            nx = 0
            ny = 0
            if (x != i) or (y != j):
                if lis[x][y] == "#":
                    nx = x - j
                    ny = y - i
                if (0 <= i - nx <= 8 and 0 <= j + ny <= 8) and (
                    0 <= x - nx <= 8 and 0 <= y + ny <= 8
                ):
                    if lis[i - nx][j + ny] == "#" and lis[x - nx][y + ny] == "#":
                        ans += 1
                        


for i in range(9):
    for j in s[i]:
        ch(i, j)
print(int(ans//2))