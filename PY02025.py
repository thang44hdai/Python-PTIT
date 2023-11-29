n, m = [int(i) for i in input().split()]
a = list(set(list(map(int, input().split()))))
b = list(set(list(map(int, input().split()))))
giao, hieu1, hieu2 = [[], [], []]
for i in a:
    if i in b:
        giao.append(i)
    else:
        hieu1.append(i)
for i in b:
    if i not in a:
        hieu2.append(i)
print(*sorted(giao))
print(*sorted(hieu1))
print(*sorted(hieu2))
