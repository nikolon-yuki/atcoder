import math
import copy
A, B = map(int, input().split())
x = 1
g = math.sqrt(x)
an = A / g
ans = copy.copy(an)
while True:
    x += 1
    a = B * (x - 1)
    ng = math.sqrt(x)
    ra = A / ng + a
    if ra >= ans:
        break
    else:
        ans = ra
print(ans)
