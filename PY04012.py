class sv:
    def __init__(self, ma, name, lop):
        self.ma = ma
        self.name = name
        self.lop = lop

    def __str__(self):
        return self.ma+" "+self.name+" "+self.lop


def dem(n):
    sum = 10
    for i in n:
        if i == 'm':
            sum -= 1
        elif i == 'v':
            sum -= 2
    return sum


vt = []
mp = {}

n = int(input())
for _ in range(n):
    vt.append(sv(input(), input(), input()))
for _ in range(n):
    ma, dd = input().split()
    diem = dem(dd)
    if diem <= 0:
        mp[ma] = "0 KDDK"
    else:
        mp[ma] = diem
for i in range(n):
    print(vt[i], mp[vt[i].ma])
