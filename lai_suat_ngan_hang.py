from math import*
def main():
    n, x, m = map(float, input().split())
    ans = log(m/n, e) / log(1+x/100, e)
    print(ceil(ans))
if __name__ == "__main__":
    for i in range(int(input())):
        main()
    
