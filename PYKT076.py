class p:
    def __init__(this, x, y, z, t, k) -> None:
        this.id = "P" + str(x).zfill(3)
        this.tl = y
        this.date = z
        this.name = t
        this.sl = k
        q = this.date.split("/")
        this.day = int(q[0])
        this.m = int(q[1])
        this.y = int(q[2])

    def __str__(this) -> str:
        return f"{this.id} {this.tl} {this.date} {this.name} {this.sl}"


n, m = map(int, input().split())
dic = {}
for i in range(1, n+1):
    n = input()
    tl = "TL"
    tl += str(i).zfill(3)
    dic[tl] = n
a = []
for i in range(1, m+1):
    x, y, z, t, k = i, dic[input()], input(), input(), int(input())
    a.append(p(x, y, z, t, k))
a = sorted(a, key=lambda x: (x.y, x.m, x.day, x.name, -x.sl))
for i in a:
    print(i)
