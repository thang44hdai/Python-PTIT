a = ['0', '1', '2']


def sol(x):
    for i in x:
        if i not in a:
            return "NO"
    return "YES"


for _ in range(int(input())):
    print(sol(input()))
