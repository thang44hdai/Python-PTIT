f = open("DATA.in", "r")
ans = []
for i in f:
    for j in i.split():
        try:
            x = int(j)
            if x > int(2**63):
                ans.append(j)
        except:
            ans.append(j)
print(" ".join(sorted(ans)))
