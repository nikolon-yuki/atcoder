a = 26


def dec2bin(a):
    amari = []
    while a != 0:
        amari.append(a % 2)
        a = a // 2
    amari.reverse()
    return amari


result = dec2bin(a)
print(result)
