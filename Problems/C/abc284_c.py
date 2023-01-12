import queue
N, M = map(int, input().split())
U = [[] for i in range(N)]
ch = [False] * N

for i in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    U[a].append(b)
    U[b].append(a)
ans = 0
q = queue.Queue()
for i in range(N):
    if ch[i]:
        continue
    else:
        ans += 1
        ch[i] = True
        q.put(i)
        while not q.empty():
            c = q.get()
            for d in U[c]:
                if ch[d]:
                    continue
                else:
                    ch[d] = True
                    q.put(d)
print(ans)
        
        
