class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        elem = len(grid)*len(grid[0])
        k = k%elem
        rowlen = len(grid[0])
        shiftline = k//rowlen
        shiftelem = k%rowlen
        print(shiftline,shiftelem)
        ans = grid
        if shiftline != 0:
            ans = grid[len(grid)-shiftline:]+grid[:len(grid)-shiftline]
        if shiftelem != 0:
            temp = [i[shiftelem+1:] for i in ans]
            temp.insert(0,temp.pop())
            for i in range(len(grid)):
                ans[i] = temp[i]+ans[i][:shiftelem+1]
            
        return ans
       
        
# class Solution(object):
#     def shiftGrid(self, grid, k):
#         l = [num for row in grid for num in row]
#         m = len(grid)
#         n = len(grid[0])
#         k = k % (len(grid) * len(grid[0]))
        
#         l = l[-k:] + l[:-k]  # shift k times
#         return [l[i * n: i * n + n] for i in range(m)]  # list to grid
