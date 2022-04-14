class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        brdr = set()
        seen = set()
        orig = grid[row][col]
         
        def isBorder(i,j):
            
            if not (0<=i<len(grid) and 0<=j<len(grid[0])) or (i,j) in seen: return False
            seen.add((i,j))
            if ((i==0 or i==len(grid)) and (j==0  or j==len(grid[0]))) or (not (isBorder(i-1,j) and isBorder(i+1,j) and isBorder(i,j-1) and isBorder(i,j+1))):
                brdr.add((i,j))
            isBorder(i+1,j)
            isBorder(i,j+1)
            isBorder(i-1,j)
            isBorder(i,j-1)
            return

        isBorder(row,col)

        for r,c in brdr:
            grid[r][c] = color
        
        print(brdr,seen)
        return grid   
#XXXXXXXXXXXXXXXXXX
# class Solution:
#     def colorBorder(self, grid: List[List[int]], r0: int, c0: int, color: int) -> List[List[int]]:
#         def dfs(r, c, current, border, seen):
#             if r<0 or c<0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] != current or (r,c) in seen:
#                 return
            
#             seen.add((r,c))
#             if (r==0 or c==0 or r==len(grid)-1 or c==len(grid[0])-1 or grid[r-1][c] != current or grid[r+1][c] != current or grid[r][c-1] != current or grid[r][c+1] != current):
#                 border.add((r,c))
                
#             dfs(r-1, c, current, border, seen)
#             dfs(r+1, c, current, border, seen)
#             dfs(r, c-1, current, border, seen)
#             dfs(r, c+1, current, border, seen)
#             return
        
#         if not grid: return grid
        
#         current = grid[r0][c0]
#         border = set()
#         seen = set()
#         dfs(r0, c0, current, border, seen)
        
#         for elem in border:
#             grid[elem[0]][elem[1]] = color
        
#         return grid
