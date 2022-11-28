N, Q = map(int, input().split())
dic = {}
lis = [[]]
for i in range(Q):
    t, a, b = map(int, input().split())
    if t == 1:
        if a not in dic:
            dic[a] = len(lis)
            lis.append([b])
        else:
            if b not in lis[dic[a]]:
                lis[dic[a]].append(b)
    if t == 2:
        if a in dic:
            if b in lis[dic[a]]:
                lis[dic[a]].remove(b)
    if t == 3:
        ans = False
        if a in dic and b in dic:
            if b in lis[dic[a]] and a in lis[dic[b]]:
                ans = True
        if ans:
            print('Yes')
        else:
            print('No')
                
    

        