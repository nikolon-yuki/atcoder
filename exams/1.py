lis = [1,2,3,4]
s = {}
for i in range(3):
    if lis[i] not in s:
        s[lis[i]] = 1
    else:
        s[lis[i]] += 1
print(len(s))
