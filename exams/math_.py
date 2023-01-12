from math import tan, sin, cos, pi, asin, acos, sqrt, atan2


def cartesian(polar):
    length, angle = polar[0], polar[1]
    return (length * cos(angle), length * sin(angle))


def length(*vectors):
    x, y = vectors[0], vectors[1]
    return sqrt((x ** 2) + (y ** 2))


def polar(*vectors):
    x, y = vectors[0], vectors[1]
    angle = atan2(y, x)
    return (length(x, y), angle)


angle = pi / (180 / 37)  # 180度に対しての37度の割合

print(cos(10*pi/6))