import math


class triangle:
    def __init__(self, a, b, c):
        self.point1 = a
        self.point2 = b
        self.point3 = c

    def cv(self):
        d1 = self.point1.distance(self.point2)
        d2 = self.point1.distance(self.point3)
        d3 = self.point2.distance(self.point3)
        if d1+d2 > d3 and d1+d3 > d2 and d2+d3 > d1:
            ans = f'{(d1 + d2 + d3):.3f}'
            return ans
        else:
            return "INVALID"


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        d1 = self.x - other.x
        d2 = self.y - other.y
        d1 *= d1
        d2 *= d2
        return math.sqrt(d1+d2)
hi = []

for _ in range(int(input())):
    a = [float(i) for i in input().split()]
    x1 = Point(float(a[0]), float(a[1]))
    x2 = Point(float(a[2]), float(a[3]))
    x3 = Point(float(a[4]), float(a[5]))
    ans = triangle(x1, x2, x3)
    hi.append(ans.cv())
for i in hi:
    print(i)