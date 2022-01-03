class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        m = len(matrix)
        n = len(matrix[0])
        
        answer = [[0 for i in range(n+1)] for j in range (m+1)]

                
        for i in range(1,m+1) :
            for j in range(1,n+1) :
                if matrix[i-1][j-1] == "0" :
                    answer[i][j]=0
                else :
                    answer[i][j]= min(answer[i-1][j],answer[i][j-1],answer[i-1][j-1])+1
                    #answer[i][j]= 1
                    
        M_answer=0
        
        for i in range(1,m+1) :
            for j in range(1,n+1) :
                if M_answer <answer[i][j] :
                    M_answer=answer[i][j]
        
        return M_answer*M_answer
                