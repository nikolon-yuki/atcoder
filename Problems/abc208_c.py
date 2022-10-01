N, K = map(int, input().split())
lis = list(map(int, input().split()))
m = 0
if N < K:
    m += K // N
dic = {}
for i in lis:
    dic[i] = m
lis.sort()
for i in range(K % N):
    dic[lis[i]] += 1
for i in dic.values():
    print(i)
