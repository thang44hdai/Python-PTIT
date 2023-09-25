def check(n):
    if len(n) % 2 == 0:
        return "NO"
    if len(n) == 1:
        return "YES"
    if n[0] == n[1]:
        return "NO"
    i = 0
    while i < len(n):
        if i+2 < len(n):
            if n[i] == n[i+2]:
                i += 2
            else:
                return "NO"
        else:
            break
    return "YES"
            
for _ in range(int(input())):
    n = input()
    print(check(n))
