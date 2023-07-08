from math import*
def main():
    for i in range(int(input())):
        n = input()
        if(n[:2]==n[-2:]):
            print("YES")
        else:
            print("NO")
            
if __name__ == "__main__":
    main()
    
