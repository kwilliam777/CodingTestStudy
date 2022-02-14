class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        answer=[[0 for i in range(len(text1)+1)] for j in range (len(text2)+1)]
                         
        for i in range(1,len(text2)+1) :
            for j in range(1,len(text1)+1):
                if text1[j-1] != text2[i-1] :
                    answer[i][j]=max(answer[i-1][j],answer[i][j-1])
                
                else :
                    answer[i][j]=answer[i-1][j-1]+1
                    
                                
        print(answer)
                            
        return answer[-1][-1]
    
        