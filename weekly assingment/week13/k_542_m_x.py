class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rec = [[0 for j in range(len(mat[i]))] for i in range(len(mat))]
        visited = []
        
        def find(i,j):
            if [i,j] in visited:
                return 100000
            visited.append([i,j])
            if 0<=i<len(mat) and 0<=j<len(mat[0]):
                if rec[i][j] != 100000:
                    return rec[i][j]
                else:
                    temp = min(find(i+1,j),find(i-1,j),find(i,j+1),find(i,j-1))+1
                    rec[i][j] = temp
                    return temp
            else:
                return 100000
            
        
        for i in range(len(rec)):
            for j in range(len(rec[i])):
                if mat[i][j] != 0:
                    rec[i][j] = 100000
        
        for i in range(len(rec)):
            for j in range(len(rec[i])):
                if rec[i][j] == 100000:
                    rec[i][j] = find(i,j)
        
        return rec
    
#     def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
#         if len(matrix) == 0: return []
        
#         rows = len(matrix)
#         cols = len(matrix[0])
#         mx = rows+cols
#         dis = [[mx for _ in range(cols)] for _ in range(rows)]

#         for i in range(rows-1, -1, -1):
#             for j in range(cols-1, -1, -1):
#                 if matrix[i][j] == 0:
#                     dis[i][j] = 0
#                 else:
#                     right = dis[i][j+1] if j+1 < cols else mx
#                     down =  dis[i+1][j] if i+1 < rows else mx
#                     dis[i][j] = 1 + min(right, down)

#         for i in range(rows):
#             for j in range(cols):
#                 if matrix[i][j] == 0:
#                     dis[i][j] = 0
#                 else:
#                     left = dis[i][j-1] if j-1 >= 0 else mx 
#                     top =  dis[i-1][j] if i-1 >= 0  else mx 
#                     dis[i][j] = min(dis[i][j], 1 + min(left, top)) # pay attention here

#         return dis
