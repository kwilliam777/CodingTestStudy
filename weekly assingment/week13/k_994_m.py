class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        count = 0
        done = False
        pre = grid
        
        def ones(grid):
            one = 0
            for i in grid:
                one += i.count(1)
            return one
        
        def valid(i,j):
            return True if 0<=i<len(grid) and 0<=j<len(grid[0]) else False
            
        def rot(i,j):
            if valid(i+1,j) and grid[i+1][j]==1 and [i+1,j] not in visited:
                grid[i+1][j] = 2
                visited.append([i+1,j])
            if valid(i-1,j) and grid[i-1][j]==1 and [i-1,j] not in visited:
                grid[i-1][j] = 2
                visited.append([i-1,j])
            if valid(i,j+1) and grid[i][j+1]==1 and [i,j+1] not in visited:
                grid[i][j+1] = 2
                visited.append([i,j+1])
            if valid(i,j-1) and grid[i][j-1]==1 and [i,j-1] not in visited:
                grid[i][j-1] = 2
                visited.append([i,j-1])
                            
                    
        if ones(grid) == 0:
            return 0
        
        while not done:
            visited = []
            pre = copy.deepcopy(grid)
            for i in range(len(grid)):
                for j in range(len(grid[i])):
                    if grid[i][j] == 2 and [i,j] not in visited:
                        rot(i,j)
            if grid == pre:
                break
            count += 1
            
        
        return -1 if ones(grid)>0 else count
    
    
    
    
    # def orangesRotting(self, grid: List[List[int]]) -> int:
    #     row, col = len(grid), len(grid[0])
    #     dirs = [(-1,0),(0,1),(1,0),(0,-1)]
    #     fresh_set=set()
    #     rotten = collections.deque()
    #     step = 0
    #     for x in range(row):
    #         for y in range(col):
    #             if grid[x][y]==1:
    #                 fresh_set.add((x,y))
    #             elif grid[x][y]==2:
    #                 rotten.append([x,y,step])
    #     while rotten:
    #         x,y,step = rotten.popleft()
    #         for dx, dy in dirs:
    #             if 0<=x+dx<row and 0<=y+dy<col and grid[x+dx][y+dy] == 1:
    #                 grid[x+dx][y+dy]=2
    #                 fresh_set.remove((x+dx,y+dy))
    #                 rotten.append([x+dx,y+dy,step+1])
    #     return step if not fresh_set else -1
