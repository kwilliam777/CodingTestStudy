for t in range(int(input())):
    n,x = list(map(int,input().split()))
    x = x*2+1
    print("#{} {}".format(t+1,n//x+1 if n%x!=0 else n//x))
