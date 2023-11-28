n, m, k = map(int, input().split())
vt = {}
for i in range(1, n+1):
    vt[i] = []
for i in range(m):
    x, y = map(int, input().split())
    vt[x].append(y)
    vt[y].append(x)
ok = [0]*(n+1)
ok[k] = 1


def bfs(u):
    q = []
    q.append(u)
    while len(q) > 0:
        top = q[-1]
        q.pop()
        for i in vt[top]:
            if ok[i] == 0:
                ok[i] = 1
                q.append(i)


bfs(k)
cnt = 0
for i in range(1, n+1):
    if ok[i] == 0:
        cnt += 1
        print(i)
if cnt == 0:
    print(0)
