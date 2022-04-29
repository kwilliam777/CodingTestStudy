for t in range(1, int(input()) + 1):
    grid=[]
    m,n=list(map(int,input().split()))
    res = "YES"
    for i in range(m):
        grid.append([j for j in input()])
    
    for i in grid:
        if i.count("#")%2!=0: res = "NO"
            
    grid=list(zip(*grid[::-1]))
    for i in grid:
        if i.count("#")%2!=0: res = "NO"
    print("#{} {}".format(t,res))
