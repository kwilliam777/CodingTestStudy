for t in range(1, int(input())+1):
    n = int(input())
    grid = [list(input()) for _ in range(n)]
    emp = -n//2
    ans = 0
    ind = 0
    while ind < len(grid):
        temp = abs(emp+ind+1)
        ans += sum(list(map(int,grid[ind][temp:n-temp])))
        ind+=1
    print("#{} {}".format(t,ans))
            
