class Solution:
    def minimumTotal(self, tri: List[List[int]]) -> int:   
        if len(tri) == 1: return tri[0][0]
        count = tri[0][0]
        def deep(row,ind):
            print(row,ind)
            if row == len(tri)-1: return tri[row][ind]
            return tri[row][ind] + min(deep(row+1,ind),deep(row+1,ind+1))
                
                
        count += min(deep(1,0),deep(1,1))
        return count
    
    
    
    
#     def minimumTotal(self, triangle: List[List[int]]) -> int:
        
#         for level in range(1, len(triangle)):
#             for i in range(level+1):
#                 triangle[level][i] += min(triangle[level-1][min(i, level-1)], triangle[level-1][max(i-1,0)])
#         return min(triangle[-1])
    
#     def minimumTotal(self, triangle: List[List[int]]) -> int:
#         for level in range(len(triangle)-2,-1,-1):
#             for i in range(level+1):
#                 triangle[level][i] += min(triangle[level+1][i], triangle[level+1][i+1])
#         return triangle[0][0]
    
#     def minimumTotal(self, triangle: List[List[int]]) -> int:
#         n = len(triangle)
#         cur_row, prev_row = [0]*n, [0]*n
#         prev_row[0] = triangle[0][0]  
#         for level in range(1, n):
#             for i in range(level+1):
#                 cur_row[i] = triangle[level][i] + min(prev_row[min(i, level-1)], prev_row[max(i-1,0)])
#             cur_row, prev_row = prev_row, cur_row
#         return min(prev_row)
    
#     def minimumTotal(self, triangle: List[List[int]]) -> int:
#         n = len(triangle)
#         cur_row, next_row = [0]*n, triangle[n-1]        
#         for level in range(n-2,-1,-1):
#             for i in range(level+1):
#                 cur_row[i] = triangle[level][i] + min(next_row[i], next_row[i+1])
#             cur_row, next_row = next_row, cur_row
#         return next_row[0]
