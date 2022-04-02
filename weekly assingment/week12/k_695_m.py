class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = []
        islands = []
        self.count = 0
        def island(i,j):
            if i<0 or j<0 or i>len(grid)-1 or j>len(grid[0])-1 or [i,j] in visited:
                return
            if grid[i][j]==1:
                self.count+=1
                visited.append([i,j])
                island(i-1,j)
                island(i+1,j)
                island(i,j-1)
                island(i,j+1)

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]==1:
                    self.count=0
                    island(i,j)
                    islands.append(self.count)
        return max(islands) if len(islands)>0 else 0

    
    
# class Solution(object):
#     def maxAreaOfIsland(self, grid):
#         seen = set()
#         def area(r, c):
#             if not (0 <= r < len(grid) and 0 <= c < len(grid[0])
#                     and (r, c) not in seen and grid[r][c]):
#                 return 0
#             seen.add((r, c))
#             return (1 + area(r+1, c) + area(r-1, c) +
#                     area(r, c-1) + area(r, c+1))

#         return max(area(r, c)
#                    for r in range(len(grid))
#                    for c in range(len(grid[0])))
