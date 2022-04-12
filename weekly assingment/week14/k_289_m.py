class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        def cnt(i,j):
            return 1 if 0<=i<len(board) and 0<=j<len(board[0]) and board[i][j]==1 else
            
        record = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                n = cnt(i+1,j)+cnt(i-1,j)+cnt(i,j+1)+cnt(i,j-1)+
                cnt(i+1,j+1)+cnt(i+1,j-1)+cnt(i-1,j+1)+cnt(i-1,j-1)
                if board[i][j]==1:
                    if n < 2 or n > 3: record.append(([i,j],0))
                else:
                    if n == 3: record.append(([i,j],1))
                        
        for i in record:
            board[i[0][0]][i[0][1]] = i[1]
            
