ans = []
dd = []
cnt = -1
for i in range(int(input())):
    n = input()
    if n != "":
        if cnt == -1:
            ans.append(n)
            cnt += 1
        else:
            cnt += 1
    else:
        dd.append(cnt)
        cnt = -1
dd.append(cnt)
for i in range(len(ans)):
    print(f"{ans[i]}: {dd[i]} ")
