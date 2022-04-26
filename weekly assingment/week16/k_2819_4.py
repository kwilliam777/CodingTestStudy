for t in range(int(input())):
    grid = []
    for i in range(4):
        grid.append(list(input().split()))
    
    def subs(i,j,st):
        if 0<=i<4 and 0<=j<4:
            st+=grid[i][j]
            if len(st)==7:
                rec.add(st)
                return
            subs(i+1,j,st)
            subs(i,j+1,st)
            subs(i-1,j,st)
            subs(i,j-1,st)
        
    rec = set()
    for i in range(len(grid)):
        for j in range(len(grid)):
            subs(i,j,str())
    print("#{} {}".format(t+1,len(rec)))
