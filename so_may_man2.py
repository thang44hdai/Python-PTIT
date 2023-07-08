from math import*
def main():
    for i in range(int(input())):
        n = input()
        cnt = n.count("4") + n.count("7")
        if(cnt==len(n)):
            print("YES")
        else:
            print("NO")
if __name__ == "__main__":
    main()