class sv:
    def __init__(this, id, name, truong, team) -> None:
        this.id = "C" + str(id).zfill(3)
        this.name = name
        this.truong = truong
        this.team = team

    def __str__(this) -> str:
        return f"{this.id} {this.name} {this.team} {this.truong}"


dic = {}
for i in range(1, int(input())+1):
    x, y = input(), input()
    t = "Team"+str(i).zfill(2)
    dic[t] = [x, y]
a = []
for i in range(1, int(input())+1):
    x, y = input(), input()
    a.append(sv(i, x, dic[y][1], dic[y][0]))
a = sorted(a, key=lambda x: (x.name))
for i in a:
    print(i)
