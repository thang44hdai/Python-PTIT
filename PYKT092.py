def checkkv(n):
    if n == 1:
        return 1.5
    if n == 2:
        return 1
    return 0


class sv:
    def __init__(this, id,  ten, diem, dantoc, khuvuc) -> None:
        x = ten.strip().split()
        this.ten = " ".join(i.title() for i in x)
        this.id = "TS" + str(id).zfill(2)
        if dantoc.lower() == "kinh":
            this.diem = diem + checkkv(khuvuc)
        else:
            this.diem = diem + checkkv(khuvuc)+1.5
        if this.diem >= 20.5:
            this.tt = "Do"
        else:
            this.tt = "Truot"

    def __str__(this) -> str:
        return f"{this.id} {this.ten} {round(this.diem, 1)} {this.tt}"


a = []
for i in range(1, int(input())+1):
    ten, diem, dt, kv = input().strip(), float(
        input().strip()), input().strip(), int(input().strip())
    a.append(sv(i, ten, diem, dt, kv))
a = sorted(a, key=lambda x: (-x.diem, x.id))
for i in a:
    print(i)
