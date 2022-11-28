s = input()
t = input()
ls = len(s)
lt = len(t)
if s == t:
    print("Yes")
    exit()
if ls <= lt:
    print("No")
    exit()
for i in range(ls - lt + 1):
    if s[i : i + lt] == t:
        print("Yes")
        exit()
print("No")
