N = int(input())
ans = ""
for i in range(120):
    if N == 0:
        break
    if N % 2 == 0:
        N = N // 2
        ans = "B" + ans
    else:
        N -= 1
        ans = "A" + ans
print(ans)