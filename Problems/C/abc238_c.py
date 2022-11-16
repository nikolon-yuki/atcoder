import sys

n = input()
if len(n) == 1:
    ans = 0
    for i in range(1, int(n) + 1):
        ans += i
    sys.exit()
l = [0] * (len(n) - 1)

for i in range(len(n) - 1):
    to = 0
    if i != 0:
        to = int("9" * i)
    num = 10 ** i
    num1 = num - to
    num2 = num * 10 - 1 - to
    a = num1 + num2
    b = num2 - num1 + 1
    l[i] = a * b // 2

a = 10 ** (len(n) - 1) - int("9" * (len(n) - 1))
b = int(n) - int("9" * (len(n) - 1))
x = a + b
y = b - a + 1
ans = ((x * y) // 2) + sum(l)
print(ans % 998244353)
