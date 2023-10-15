def tong_kt(n):
    sum = 0
    for i in n:
        sum += ord(i)-ord('A')
    return sum


def rotate(n, k):
    s = ""
    for i in n:
        x = ord(i)-ord('A')
        x += k
        x %= 26
        x += ord('A')
        s += chr(x)
    return s


def merge(n, n1):
    s = ""
    for i in range(len(n)):
        x = ord(n[i])-ord('A')
        k = ord(n1[i])-ord('A')
        x += k
        x %= 26
        x += ord("A")
        s += chr(x)
    return s


for _ in range(int(input())):
    n = input()
    n1 = n[:int(len(n)/2)]
    n2 = n[int(len(n)/2):]
    n1 = rotate(n1, tong_kt(n1))
    n2 = rotate(n2, tong_kt(n2))
    n1 = merge(n1, n2)
    print(n1)