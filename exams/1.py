n, x, y = 10,5,5
red = [0] * 11
blue = [0] * 11
red[n] += 1


def R(r, b, x, y):
    for i in range(10, 0, -1):
        if i == 1:
            return B(r, b, x, y)
        if r[i] != 0:
            r[i - 1] += r[i]
            b[i] += x * r[i]
            r[i] = 0


def B(r, b, x, y):
    for i in range(10, 0, -1):
        if i == 1:
            return b
        if b[i] != 0:
            r[i - 1] += b[i]
            b[i - 1] += y * b[i]
            b[i] = 0
            return R(r, b, x, y)

a = R(red, blue, x, y)
print(a[1])
