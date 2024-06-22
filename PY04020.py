class hh:
    def __init__(this, x, y, z, t, k) -> None:
        this.id = x
        this.name = y
        this.sl = z
        this.dg = t
        this.ck = k
        this.tt = this.dg*this.sl - this.ck

    def __str__(this) -> str:
        return f"{this.id} {this.name} {this.sl} {this.dg} {this.ck} {this.tt}"


a = []
for _ in range(int(input())):
    x, y, z, t, k = input(), input(), int(input()), int(input()), int(input())
    a.append(hh(x, y, z, t, k))
a = sorted(a, key=lambda x: (-x.tt))
for i in a:
    print(i)

