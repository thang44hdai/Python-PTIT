
s = ''
regex = '\\.\\!\\?'
while True:
    try:
        s += input()
    except EOFError:
        break

l = s.split()
check = 0
for i in l:
    if check == 0:
        if i[-1] == "." or i[-1] == "?" or i[-1] == "!":
            print(i[:len(i)-1].title())
        else:
            print(i.title(), end=" ")
            check = 1
    else:
        if i[-1] == "." or i[-1] == "?" or i[-1] == "!":
            check = 0
            print(i[:len(i)-1].lower())
        else:
            print(i.lower(), end=" ")
            check = 1
