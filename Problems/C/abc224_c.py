
N = int(input())
S = []
ans = 0
for i in range(N):
    x, y = map(int, input().split())
    S.append([x, y])
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            if (S[j][0]-S[i][0])*(S[k][1]-S[i][1])-(S[k][0]-S[i][0])*(S[j][1]-S[i][1]) != 0:
                ans += 1
print(ans)
