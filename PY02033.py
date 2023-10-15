import textwrap


n = input()
l = list(textwrap.wrap(n, 2))
dd = []
for i in l:
    if i not in dd and len(i)==2:
        print(i, end =" ")
        dd.append(i)