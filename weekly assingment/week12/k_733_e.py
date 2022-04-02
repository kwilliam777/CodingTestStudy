class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        color = image[sr][sc]
        image[sr][sc] = newColor
        visited=[[sr,sc]]
        
        def valid(ind):
            return True if 0<=ind[0]<len(image) and 0<=ind[1]<len(image[ind[0]]) else False
            
        def change(ind):
            u=list(map(add,ind,[-1,0]))
            d=list(map(add,ind,[1,0]))
            r=list(map(add,ind,[0,1]))
            l=list(map(add,ind,[0,-1]))
            
            if u not in visited and valid(u) and image[u[0]][u[1]]==color:
                image[u[0]][u[1]] = newColor
                visited.append(u)
                change(u)
            if d not in visited and valid(d) and image[d[0]][d[1]]==color:
                image[d[0]][d[1]] = newColor
                visited.append(d)
                change(d)
            if r not in visited and valid(r) and image[r[0]][r[1]]==color:
                image[r[0]][r[1]] = newColor
                visited.append(r)
                change(r)
            if l not in visited and valid(l) and image[l[0]][l[1]]==color:
                image[l[0]][l[1]] = newColor
                visited.append(l)
                change(l)
        change([sr,sc])
        return image
    
    
    
    
    
# class Solution:
#     def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
#         rows = len(image)
#         cols = len(image[0])
#         a = image[sr][sc]
        
#         def dfs(r, c):
#             nonlocal rows, cols, newColor, image
#             if r < 0 or c < 0 or r>rows-1 or c>cols-1 or image[r][c]==newColor or image[r][c]!=a:
#                 return
            
#             image[r][c] = newColor
#             dfs(r+1,c)
#             dfs(r-1,c)
#             dfs(r,c+1)
#             dfs(r,c-1)
        
#         dfs(sr, sc)
#         return image
