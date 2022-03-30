class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            if target in i:
                return True
        return False
    
    
# class Solution(object):   
#     def searchMatrix(self, matrix, target):
#         n=len(matrix)*len(matrix[0])
#         start=0
#         end=n-1
#         while start<=end:
#             mid=(start+end)//2
#             r=mid//len(matrix[0])
#             c=mid%len(matrix[0])
#             if matrix[r][c]==target:
#                 return True
#             if matrix[r][c]<target:
#                 start=mid+1
#             else:
#                 end=mid-1
#         return False
