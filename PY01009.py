n = input()
cnt = 0
for i in n:
    if 'a' <= i <= 'z':
        cnt += 1
if cnt >= len(n)-cnt:
    print(n.lower())
else:
    print(n.upper())
