from collections import Counter
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check(arr):
            result = Counter(arr)
            for i in result:
                if i!="." and result[i]>1:
                    return False
            return True
        
        
        for i in board:
            if check(i) == False: return False
        
        other = list(zip(*board[::-1]))
        for i in other:
            if check(i) == False: return False
        
        temp = [[0] for i in range(9)]
        for i in range(len(board)):
            ind = i//3*3
            temp[ind].extend(board[i][:3])
            temp[ind+1].extend(board[i][3:6])
            temp[ind+2].extend(board[i][6:9])
            
        for i in temp:
            if check(i) == False: return False
        
        return True

# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:
#         col = collections.defaultdict(set)
#         row = collections.defaultdict(set)
#         square = collections.defaultdict(set)
        
#         for r in range(9):
#             for c in range(9):
#                 if board[r][c] == '.':
#                     continue
                
#                 if board[r][c] in col[c] or board[r][c] in row[r] or board[r][c] in square[(c//3, r//3)]:
#                     return False
                
#                 col[c].add(board[r][c])
#                 row[r].add(board[r][c])
#                 square[c//3, r//3].add(board[r][c])
#         return True
