import sys

sys.setrecursionlimit(1000000)

N = int(input())
radder = []
s = {}
ans = 1
for i in range(N):
    a, b = map(int, input().split())
    if a not in s:
        s[a] = len(radder)
        radder.append([b])
    else:
        radder[s[a]].append(b)
    if b not in s:
        s[b] = len(radder)
        radder.append([a])
    else:
        radder[s[b]].append(a)
dic = sorted(s.items(), reverse=True)
# if 1 not in s:
#     print(1)
#     exit()


def Graph(num, Ri, ch):
    for x in Ri:
        if x == 1:
            return True
        else:
            if x not in ch:
                ch[x] = True
                if Graph(num, radder[s[x]], ch):
                    return True
ch = {}
for i, j in dic:
    if i == 1:
        ans = 1
        break
    if Graph(i, radder[j], ch):
        ans = i
        break
print(ans)
