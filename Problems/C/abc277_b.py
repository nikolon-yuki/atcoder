N = int(input())
ans = True
S = []
for i in range(N):
    s = input()
    s1 = s[0]
    s2 = s[1]
    if not (s1 == "H" or s1 == "D" or s1 == "C" or s1 == "S"):
        ans = False
        break
    if not (
        s2 == "A"
        or s2 == "2"
        or s2 == "3"
        or s2 == "4"
        or s2 == "5"
        or s2 == "6"
        or s2 == "7"
        or s2 == "8"
        or s2 == "9"
        or s2 == "T"
        or s2 == "J"
        or s2 == "Q"
        or s2 == "K"
    ):
        ans = False
        break
    if s in S:
        ans = False
        break
    S.append(s)
if ans:
    print('Yes')
else:
    print('No')