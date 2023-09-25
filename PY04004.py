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

    def __add__(self, z):
        tsc = self.ts * z.ms + self.ms*z.ts
        msc = self.ms*z.ms
        return phanSo(tsc, msc)


x, y, z, t = [int(i) for i in input().split()]
a = phanSo(x, y)
b = phanSo(z, t)
print(a+b)

# class PhanSo:
#     def __init__(self, x, y):
#         uc = gcd(x, y)
#         x /= uc
#         y /= uc
#         self.tuso = int(x)
#         self.mauso = int(y)

#     def __add__(self, other):
#         tuso_moi = self.tuso * other.mauso + other.tuso * self.mauso
#         mauso_moi = self.mauso * other.mauso
#         return PhanSo(tuso_moi, mauso_moi)

#     def __str__(self):
#         return f"{self.tuso}/{self.mauso}"


# x, y, z, t = [int(i) for i in input().split()]
# ps1 = PhanSo(x, y)
# ps2 = PhanSo(z, t)
# tong = ps1 + ps2
# print(ps1 + ps2)
