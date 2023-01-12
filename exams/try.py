T = int(input())
N = int(input())
num = [0]*(T+1)
for i in range(N):
  a,b = map(int,input().split())
  num[a] += 1
  num[b] -= 1
ans = 0
for i in range(T+1):
  ans += num[i]
  print(ans)