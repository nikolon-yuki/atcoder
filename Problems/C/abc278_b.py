h, m = input().split()
if len(h) == 1:
    h = "0" + h
if len(m) == 1:
    m = '0' + m
if h[0] == '2':
    if int(m[0]) <= 3:
        print(h, m)
        exit()
    else:
        if int(h[1]) == 3:
            print(0,0)
            exit()
        else:
            print(int(h) + 1, 0)
            exit()
else:
    if int(h[1]) <= 5:
        print(h, m)
        exit()
    else:
        h0 = str(int(h[0]) + 1) + "0"
        print(h0, 0)
        exit()
