n, m = map(int, input().split())
a = [int(i) for i in input().split()]
dd = {}
for i in a:
    try:
        dd[i] += 1
    except:
        dd[i] = 1
ans = sorted(dd, key=lambda x: (-dd[x], x))
Max = dd[ans[0]]
check = True
for i in ans:
    if dd[i]<Max:
        check = False
        print(i)
        break
if check == True:
    print("NONE")