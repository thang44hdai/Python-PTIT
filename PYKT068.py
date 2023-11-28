
class mh:
    def __init__(self, x, y, z):
        self.id = x
        self.name = y
        self.hinhthuc = z

    def __str__(self):
        return self.id+" "+self.name+" "+self.hinhthuc


vt = []
for _ in range(int(input())):
    x, y, z = input(), input(), input()
    vt.append(mh(x, y, z))

vt = sorted(vt, key=lambda x: x.id)
for i in vt:
    print(i)
