class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.found = False    
        def valid(pos):
            return True if 0 <= pos[0] < len(board) and 0 <= pos[1] < len(board[0]) else False
            
        def check(pos,ind,path):
            # print(path,self.found)
            ind+=1
            u = list(map(add,pos,[-1,0]))
            d = list(map(add,pos,[1,0]))
            r = list(map(add,pos,[0,1]))
            l = list(map(add,pos,[0,-1]))
            # print(u,d,r,l)
            
            
            if valid(r) and board[r[0]][r[1]] == word[ind] and r not in path:
                print("r")
                if ind == len(word)-1: 
                    self.found = True
                    return
                else:
                    path.append(r)
                    check(r,ind,path)
            if valid(d) and board[d[0]][d[1]] == word[ind] and d not in path:
                print("d")
                if ind == len(word)-1: 
                    self.found = True
                    return
                else:
                    path.append(d)
                    check(d,ind,path)
            if valid(l) and board[l[0]][l[1]] == word[ind] and  l not in path:
                print("l")
                if ind == len(word)-1: 
                    self.found = True
                    return
                else:
                    path.append(l)
                    check(l,ind,path)
            if valid(u) and board[u[0]][u[1]] == word[ind] and u not in path:
                print("u")
                if ind == len(word)-1: 
                    self.found = True
                    return
                else:
                    path.append(u)
                    check(u,ind,path)
            
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                ind = 0
                path = []
                if board[i][j] == word[ind]:
                    if ind == len(word)-1: return True
                    path.append([i,j])
                    check([i,j],ind,path)
                    
        return self.found
    
# class Solution:
#     def exist(self, board, word):
#         visited = {}

#         for i in range(len(board)):
#             for j in range(len(board[0])):
#                 if self.getWords(board, word, i, j, visited):
#                     return True
#         return False

#     def getWords(self, board, word, i, j, visited, pos = 0):
#         if pos == len(word):
#             return True

#         if i < 0 or i == len(board) or j < 0 or j == len(board[0]) or visited.get((i, j)) or word[pos] != board[i][j]:
#             return False

#         visited[(i, j)] = True
#         res = self.getWords(board, word, i, j + 1, visited, pos + 1) \
#                 or self.getWords(board, word, i, j - 1, visited, pos + 1) \
#                 or self.getWords(board, word, i + 1, j, visited, pos + 1) \
#                 or self.getWords(board, word, i - 1, j, visited, pos + 1)
#         visited[(i, j)] = False

#         return res
    
