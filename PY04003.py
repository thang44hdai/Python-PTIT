from math import gcd


class phanSo:
    def __init__(self, x, y):
        uc = gcd(x, y)
        x /= uc
        y /= uc
        self.ts = int(x)
        self.ms = int(y)

    def __str__(self):
        return str(self.ts)+"/"+str(self.ms)


x, y = [int(i) for i in input().split()]
a = phanSo(x, y)
print(a)
