class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = []
        
        def check(i,j):
            island = set()
            q = [(i,j)]
            
            while q:
                loc = q.pop()
                if 0<=loc[0]<len(grid) and 0<=loc[1]<len(grid[0]) and grid[loc[0]][loc[1]] == "1":
                    island.add((loc[0],loc[1]))
                    grid[loc[0]][loc[1]] = "#"
                    q.append((loc[0]+1,loc[1]))
                    q.append((loc[0],loc[1]+1))
                    q.append((loc[0]-1,loc[1]))
                    q.append((loc[0],loc[1]-1))
            islands.append(list(island))
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]=="1":
                    check(i,j)
                    
        return len(islands)
