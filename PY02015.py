while True:
    a = [int(i) for i in input().split()]
    if a == [0, 0, 0, 0]:
        break
    cnt = 0
    while (True):
        if a[0] == a[1] == a[2] == a[3]:
            break
        b = [i for i in a]
        a[0] = abs(b[0]-b[1])
        a[1] = abs(b[1]-b[2])
        a[2] = abs(b[3]-b[2])
        a[3] = abs(b[3]-b[0])
        cnt += 1
    print(cnt)
