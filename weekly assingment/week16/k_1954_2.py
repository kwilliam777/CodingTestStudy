def prnt(t,grid):
    print("#{}".format(t+1))
    for i in grid:
        st = (" ").join(i)
        print(st)

for t in range(int(input())):
    n = int(input())
    grid = [[0 for i in range(n)] for i in range(n)]
    dire = [[0,1],[1,0],[0,-1],[-1,0]]
    look = 0
    ind = 1
    st = [0,0]
    
    while ind<=n*n:
        if grid[st[0]][st[1]] != 0: break
        grid[st[0]][st[1]] = str(ind)
        nxt = [sum(val) for val in zip(st,dire[look])]
        if not (0<=nxt[0]<len(grid) and 0<=nxt[1]<len(grid)) or grid[nxt[0]][nxt[1]]!=0:
            look+=1
            look%=4
            nxt = [sum(val) for val in zip(st,dire[look])]
        st = nxt
        ind+=1
   
    prnt(t,grid)
