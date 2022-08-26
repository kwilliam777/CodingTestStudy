class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rec = sum(board,[])
        for i in word:
            if i not in rec:
                return False
            
        def check(i,j,ind,seen):
            if ind == len(word): return True
            if 0<=i<len(board) and 0<=j<len(board[0]) and (i,j) not in seen and board[i][j] == word[ind]:
                seen+=[(i,j)]
                if check(i,j+1,ind+1,seen) or check(i+1,j,ind+1,seen) or check(i-1,j,ind+1,seen) or check(i,j-1,ind+1,seen): return True
                else: seen.pop()
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if check(i,j,0,[]): return True
        return False
