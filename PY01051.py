def check(n):
    n = str(n)
    if len(n) <= 1:
        return 'NO'
    if n != n[::-1]:
        return 'NO'
    else:
        return 'YES'


for _ in range(int(input())):
    n = input()
    total = sum(int(i) for i in n)
    print(check(total))