class Rectangle:
    def __init__(self, x, y, z):
        self.cd = x
        self.cr = y
        self.mau = z

    def check(self):
        if self.cd <= 0 or self.cr <= 0:
            return False
        return True

    def perimeter(self):
        if self.check() == True:
            return (self.cd+self.cr)*2
        return ""

    def area(self):
        if self.check() == True:
            return self.cd*self.cr
        return ""

    def color(self):
        if self.check() == True:
            return self.mau.title()
        return "INVALID"


arr = input().split()
r = Rectangle(int(arr[0]), int(arr[1]), arr[2])
print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))
